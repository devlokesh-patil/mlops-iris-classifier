"""HTTP prediction server for the Dockerized Iris classifier."""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import joblib
import pandas as pd

MODEL_DIR = "models"

FEATURE_COLS = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
    "sepal_area",
    "petal_area",
    "sepal_to_petal_length_ratio",
]

model = joblib.load(os.path.join(MODEL_DIR, "final_model.joblib"))
label_encoder = joblib.load(
    os.path.join(MODEL_DIR, "label_encoder.joblib")
)


class PredictionHandler(BaseHTTPRequestHandler):
    def send_json(self, status_code, data):
        response = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        if self.path == "/health":
            self.send_json(200, {"status": "healthy"})
        else:
            self.send_json(404, {"error": "Not found"})

    def do_POST(self):
        if self.path != "/predict":
            self.send_json(404, {"error": "Not found"})
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            if content_length <= 0:
                raise ValueError("Request body is empty")

            payload = json.loads(
                self.rfile.read(content_length).decode("utf-8")
            )

            if not isinstance(payload, dict):
                raise ValueError("JSON body must be an object")

            missing = [name for name in FEATURE_COLS if name not in payload]
            if missing:
                raise ValueError(
                    "Missing required features: " + ", ".join(missing)
                )

            values = {}
            for name in FEATURE_COLS:
                value = payload[name]
                if isinstance(value, bool):
                    raise ValueError(f"Invalid numeric value for {name}")

                number = float(value)
                if not pd.notna(number):
                    raise ValueError(f"Invalid numeric value for {name}")

                values[name] = number

            features = pd.DataFrame([values], columns=FEATURE_COLS)
            prediction = model.predict(features)[0]
            probabilities = model.predict_proba(features)[0]
            species = label_encoder.inverse_transform([prediction])[0]

            self.send_json(
                200,
                {
                    "prediction": str(species),
                    "probabilities": {
                        str(label_encoder.classes_[index]): float(probability)
                        for index, probability in enumerate(probabilities)
                    },
                },
            )

        except (ValueError, TypeError, json.JSONDecodeError) as error:
            self.send_json(400, {"error": str(error)})

    def log_message(self, format_string, *args):
        print(f"{self.address_string()} - {format_string % args}")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    server = HTTPServer(("0.0.0.0", port), PredictionHandler)
    print(f"Iris prediction server listening on port {port}")
    server.serve_forever()
