import pandas as pd
import pytest
from src.pipeline.features import engineer_features


def test_engineer_features_calculates_areas_and_ratio(tmp_path):
    data = {
        "sepal length (cm)": [5.0],
        "sepal width (cm)": [3.0],
        "petal length (cm)": [2.0],
        "petal width (cm)": [0.5],
        "species": ["setosa"],
    }

    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    pd.DataFrame(data).to_csv(input_file, index=False)

    result = engineer_features(str(input_file), str(output_file))

    assert result.loc[0, "sepal_area"] == pytest.approx(15.0)
    assert result.loc[0, "petal_area"] == pytest.approx(1.0)
    assert result.loc[0, "sepal_to_petal_length_ratio"] == pytest.approx(2.5)
    assert output_file.exists()


def test_engineer_features_assigns_petal_length_bins(tmp_path):
    data = {
        "sepal length (cm)": [5.0, 6.0, 7.0],
        "sepal width (cm)": [3.0, 3.0, 3.0],
        "petal length (cm)": [1.5, 3.0, 5.0],
        "petal width (cm)": [0.2, 1.0, 2.0],
        "species": ["setosa", "versicolor", "virginica"],
    }

    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    pd.DataFrame(data).to_csv(input_file, index=False)

    result = engineer_features(str(input_file), str(output_file))

    assert result["petal_length_bin"].astype(str).tolist() == [
        "short", "medium", "long"
    ]


def test_engineer_features_zero_petal_length_produces_missing_ratio(tmp_path):
    data = {
        "sepal length (cm)": [5.0],
        "sepal width (cm)": [3.0],
        "petal length (cm)": [0.0],
        "petal width (cm)": [0.2],
        "species": ["setosa"],
    }

    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    pd.DataFrame(data).to_csv(input_file, index=False)

    result = engineer_features(str(input_file), str(output_file))

    assert pd.isna(result.loc[0, "sepal_to_petal_length_ratio"])
