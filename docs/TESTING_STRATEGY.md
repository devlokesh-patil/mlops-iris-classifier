# Testing Strategy

## 1. Objective

The objective of this testing strategy is to verify the correctness and reliability of the Iris classification project's data preprocessing, feature engineering, data validation, model training, and prediction functions.

## 2. Testing Framework

- **pytest:** Used to execute automated unit tests.
- **pytest-cov:** Used to measure code coverage.
- **pandas:** Used to prepare and validate test datasets.
- **scikit-learn:** Used to train and evaluate the classification model.

## 3. Test Modules

### 3.1 Preprocessing Tests

File: `tests/test_preprocess.py`

Tests verify that:
- Duplicate records are removed.
- Missing numerical values are imputed.
- Rows with missing species labels are removed.
- The `collected_at` column is removed when present.

### 3.2 Feature Engineering Tests

File: `tests/test_features.py`

Tests verify that:
- Engineered areas and ratios are calculated correctly.
- Petal lengths are assigned to the appropriate categories.
- Zero petal length produces a missing ratio rather than an invalid division result.

### 3.3 Data Validation Tests

File: `tests/test_validate.py`

Tests verify that:
- Valid datasets are accepted.
- Unexpected species labels are rejected.
- Null values are rejected.
- Out-of-range measurements are rejected.
- Missing required columns are rejected.

### 3.4 Training Pipeline Tests

File: `tests/test_training_pipeline.py`

Tests verify that:
- Data is divided into training and testing sets.
- The training function produces a usable model.
- Model evaluation returns accuracy and a classification report.

### 3.5 Model Quality Tests

File: `tests/test_model_quality.py`

Tests verify that:
- The model meets the configured minimum accuracy.
- Predictions contain valid class labels.
- Predicted class probabilities are within the valid range and sum to approximately one.

## 4. Test Execution

Run the automated tests using:

```bash
python -m pytest -v tests
```

Measure test coverage using:

```bash
python -m pytest --cov=src --cov-report=term-missing tests
```

## 5. Test Results

The initial test run completed successfully:

- Total tests executed: 18
- Tests passed: 18
- Tests failed: 0

All five test modules passed.

## 6. Coverage Analysis

The initial coverage report showed:

| Module | Coverage |
|---|---:|
| `src/pipeline/preprocess.py` | 83% |
| `src/pipeline/features.py` | 75% |
| `src/pipeline/validate.py` | 81% |
| `src/train.py` | 70% |
| Overall `src/` directory | 23% |

The overall percentage includes scripts outside the scope of the current test suite. Additional tests can improve coverage of both the pipeline modules and the other source files.

## 7. Continuous Integration

The test suite can be incorporated into a continuous integration workflow. Automated tests should run whenever relevant code changes are submitted. A failed test should cause the workflow to report a failure so that defects can be investigated before changes are accepted.

## 8. Conclusion

The initial testing phase successfully executed 18 automated tests, with all 18 passing. The tests cover preprocessing, feature engineering, data validation, model training, and model quality. The coverage report identifies areas where additional tests can improve the project's test coverage.
