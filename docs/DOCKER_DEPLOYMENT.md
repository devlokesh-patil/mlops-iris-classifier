# Practical 10: Containerization of the ML Application Using Docker

## 1. Aim

To containerize the Iris machine learning classification application using Docker and verify its execution through a prediction API.

## 2. Project Overview

The application predicts the species of an Iris flower using a trained Random Forest classifier.

The model uses seven features:
- Sepal length
- Sepal width
- Petal length
- Petal width
- Sepal area
- Petal area
- Sepal-to-petal length ratio

## 3. Technologies Used

- Python 3.11
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Docker
- HTTP REST API

## 4. Files Created

- `Dockerfile`: Defines the multi-stage Docker image build.
- `.dockerignore`: Excludes unnecessary files from the Docker build context.
- `requirements-serving.txt`: Specifies the Python dependency versions.
- `src/train_final_model.py`: Trains and saves the model and label encoder.
- `src/serve.py`: Provides health-check and prediction endpoints.

## 5. Docker Image Creation

The Docker image was built using:

    docker build -t iris-classifier:v1 .

The multi-stage build installs the dependencies, trains the model, and copies the required model files and serving application into the runtime image.

The image was created successfully with the tag `iris-classifier:v1`.

## 6. Running the Container

The container was started using:

    docker run -d --name iris-classifier-container -p 8000:8000 iris-classifier:v1

The container was verified using:

    docker ps

The container was running with port 8000 mapped to the host, and its health status was reported as healthy.

## 7. Health Endpoint Test

Request:

    curl http://localhost:8000/health

Response:

    {"status": "healthy"}

Result: Passed.

## 8. Prediction API Test

A POST request was sent to `/predict` with the following sample features:

    {
      "sepal length (cm)": 5.1,
      "sepal width (cm)": 3.5,
      "petal length (cm)": 1.4,
      "petal width (cm)": 0.2,
      "sepal_area": 17.85,
      "petal_area": 0.28,
      "sepal_to_petal_length_ratio": 3.642857
    }

The application returned:

    {
      "prediction": "setosa",
      "probabilities": {
        "setosa": 1.0,
        "versicolor": 0.0,
        "virginica": 0.0
      }
    }

Result: Passed.

## 9. Invalid Input Test

A POST request containing an empty JSON object was sent to `/predict`.

The application returned HTTP 400 Bad Request and reported the missing required features.

Result: Passed.

## 10. Container Health and Logs

The container health was checked using:

    docker inspect --format='{{.State.Health.Status}}' iris-classifier-container

The result was:

    healthy

The container logs confirmed that the server started successfully and handled health checks and prediction requests.

The image layers were inspected using:

    docker history iris-classifier:v1

## 11. Conclusion

The Iris machine learning application was successfully containerized using Docker. The image was built, the container was started, and the health endpoint, valid prediction request, and invalid input handling were tested successfully.
