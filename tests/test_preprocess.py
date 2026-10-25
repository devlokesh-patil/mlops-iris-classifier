import pandas as pd
from src.pipeline.preprocess import preprocess


def test_preprocess_removes_duplicates(tmp_path):
    data = {
        "sepal length (cm)": [5.0, 5.0],
        "sepal width (cm)": [3.0, 3.0],
        "petal length (cm)": [1.5, 1.5],
        "petal width (cm)": [0.2, 0.2],
        "species": ["setosa", "setosa"],
    }

    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    pd.DataFrame(data).to_csv(input_file, index=False)

    result = preprocess(str(input_file), str(output_file))

    assert len(result) == 1


def test_preprocess_fills_missing_numeric_values(tmp_path):
    data = {
        "sepal length (cm)": [5.0, None, 7.0],
        "sepal width (cm)": [3.0, 3.1, 3.2],
        "petal length (cm)": [1.5, 1.6, 4.5],
        "petal width (cm)": [0.2, 0.3, 1.5],
        "species": ["setosa", "setosa", "versicolor"],
    }

    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    pd.DataFrame(data).to_csv(input_file, index=False)

    result = preprocess(str(input_file), str(output_file))

    assert result["sepal length (cm)"].isna().sum() == 0


def test_preprocess_removes_rows_with_missing_species(tmp_path):
    data = {
        "sepal length (cm)": [5.0, 6.0],
        "sepal width (cm)": [3.0, 3.1],
        "petal length (cm)": [1.5, 4.0],
        "petal width (cm)": [0.2, 1.2],
        "species": ["setosa", None],
    }

    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    pd.DataFrame(data).to_csv(input_file, index=False)

    result = preprocess(str(input_file), str(output_file))

    assert len(result) == 1
    assert result["species"].iloc[0] == "setosa"


def test_preprocess_removes_collected_at_column(tmp_path):
    data = {
        "sepal length (cm)": [5.0],
        "sepal width (cm)": [3.0],
        "petal length (cm)": [1.5],
        "petal width (cm)": [0.2],
        "species": ["setosa"],
        "collected_at": ["2026-01-01"],
    }

    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    pd.DataFrame(data).to_csv(input_file, index=False)

    result = preprocess(str(input_file), str(output_file))

    assert "collected_at" not in result.columns
    assert output_file.exists()
