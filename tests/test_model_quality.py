import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from src.train import train_model


MIN_ACCEPTABLE_ACCURACY = 0.999


def test_model_meets_minimum_accuracy():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=0.2,
        random_state=42,
        stratify=iris.target,
    )

    model = train_model(X_train, y_train, n_estimators=100)
    accuracy = model.score(X_test, y_test)

    assert accuracy >= MIN_ACCEPTABLE_ACCURACY, (
        f"Model accuracy {accuracy:.3f} is below "
        f"the required {MIN_ACCEPTABLE_ACCURACY:.3f}"
    )


def test_model_predictions_are_valid_classes():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    model = train_model(X_train, y_train, n_estimators=100)
    predictions = model.predict(X_test)

    assert set(np.unique(predictions)).issubset(set(iris.target))


def test_model_probabilities_are_valid():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    model = train_model(X_train, y_train, n_estimators=100)
    probabilities = model.predict_proba(X_test)

    assert np.all(probabilities >= 0.0)
    assert np.all(probabilities <= 1.0)
    assert np.allclose(probabilities.sum(axis=1), 1.0)
