"""
Compare the latest Grid Search and Random Search runs tracked in MLflow.
Keeps all historical MLflow runs; only displays the latest run per method.
"""

import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://127.0.0.1:5000")
client = MlflowClient()

experiment = client.get_experiment_by_name("iris-hyperparameter-tuning")

if experiment is None:
    raise RuntimeError("MLflow experiment 'iris-hyperparameter-tuning' not found.")

runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["attributes.start_time DESC"],
)

latest_by_name = {}

for run in runs:
    name = run.data.tags.get("mlflow.runName", "unknown")

    if name not in latest_by_name:
        latest_by_name[name] = run

print(f"{'Run Name':<30}{'CV Macro F1':<15}{'Test Accuracy':<16}{'Total Fits':<12}")
print("-" * 73)

for name, run in sorted(latest_by_name.items()):
    cv_score = run.data.metrics.get(
        "cv_f1_macro_mean",
        run.data.metrics.get("best_cv_f1_macro", 0.0),
    )
    test_accuracy = run.data.metrics.get("test_accuracy", 0.0)

    combinations = (
        run.data.params.get("total_combinations")
        or run.data.params.get("n_iter")
        or "1"
    )
    cv_folds = int(run.data.params.get("cv_folds", "5"))
    total_fits = int(combinations) * cv_folds

    print(
        f"{name:<30}{cv_score:<15.4f}"
        f"{test_accuracy:<16.4f}{total_fits:<12}"
    )
