import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from src.train import load_data, train_model, evaluate_model


def test_load_data_returns_training_and_test_sets():
    X_train, X_test, y_train, y_test = load_data()

    assert len(X_train) > 0
    assert len(X_test) > 0
    assert len(X_train) == len(y_train)
    assert len(X_test) == len(y_test)


def test_train_model_produces_usable_model():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    model = train_model(X_train, y_train, n_estimators=10)

    predictions = model.predict(X_test)

    assert predictions.shape == y_test.shape
    assert set(np.unique(predictions)).issubset(set(iris.target))


def test_evaluate_model_returns_accuracy_and_report():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    model = train_model(X_train, y_train, n_estimators=10)
    accuracy, report = evaluate_model(model, X_test, y_test)

    assert 0.0 <= accuracy <= 1.0
    assert isinstance(report, str)
    assert "precision" in report
