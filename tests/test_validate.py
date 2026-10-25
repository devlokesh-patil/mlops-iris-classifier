import pandas as pd
import pytest
from src.pipeline.validate import validate, DataValidationError


@pytest.fixture
def valid_data():
    return pd.DataFrame({
        "sepal length (cm)": [5.1, 6.0, 6.5],
        "sepal width (cm)": [3.5, 3.0, 3.2],
        "petal length (cm)": [1.4, 4.0, 5.5],
        "petal width (cm)": [0.2, 1.0, 2.0],
        "species": ["setosa", "versicolor", "virginica"],
        "sepal_area": [17.85, 18.0, 20.8],
        "petal_area": [0.28, 4.0, 11.0],
        "sepal_to_petal_length_ratio": [3.64, 1.5, 1.18],
        "petal_length_bin": ["short", "medium", "long"],
    })


def test_validate_accepts_valid_data(tmp_path, valid_data):
    input_file = tmp_path / "valid.csv"
    valid_data.to_csv(input_file, index=False)

    result = validate(str(input_file))

    assert len(result) == 3


def test_validate_rejects_unexpected_species(tmp_path, valid_data):
    valid_data.loc[0, "species"] = "unknown"
    input_file = tmp_path / "invalid_species.csv"
    valid_data.to_csv(input_file, index=False)

    with pytest.raises(DataValidationError):
        validate(str(input_file))


def test_validate_rejects_null_values(tmp_path, valid_data):
    valid_data.loc[0, "sepal width (cm)"] = None
    input_file = tmp_path / "null_values.csv"
    valid_data.to_csv(input_file, index=False)

    with pytest.raises(DataValidationError):
        validate(str(input_file))


def test_validate_rejects_out_of_range_measurements(tmp_path, valid_data):
    valid_data.loc[0, "sepal length (cm)"] = 20.0
    input_file = tmp_path / "out_of_range.csv"
    valid_data.to_csv(input_file, index=False)

    with pytest.raises(DataValidationError):
        validate(str(input_file))


def test_validate_rejects_missing_expected_column(tmp_path, valid_data):
    valid_data = valid_data.drop(columns=["sepal_area"])
    input_file = tmp_path / "missing_column.csv"
    valid_data.to_csv(input_file, index=False)

    with pytest.raises(DataValidationError):
        validate(str(input_file))
