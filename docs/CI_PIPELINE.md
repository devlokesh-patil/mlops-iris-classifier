# Continuous Integration (CI) Pipeline

## 1. Objective

The objective of this practical is to set up a Continuous Integration (CI) pipeline using GitHub Actions for the Iris Classifier project. The pipeline automatically checks code quality, runs automated tests, and verifies model quality when changes are pushed to GitHub or submitted through a pull request.

## 2. Tools and Technologies

- Python 3.11
- Git and GitHub
- GitHub Actions
- Pytest
- Flake8
- pytest-cov

## 3. Workflow Configuration

The CI workflow is defined in `.github/workflows/ci.yml`.

It runs automatically when code is pushed to, or a pull request targets, the `main` or `develop` branch.

## 4. Pipeline Jobs

### Job 1: Build and Lint

- Checks out the repository.
- Sets up Python 3.11.
- Installs project dependencies.
- Checks Python syntax using `compileall`.
- Checks source-code style using Flake8.

### Job 2: Test Suite

- Installs the required dependencies.
- Runs the data pipeline, including data collection, preprocessing, feature engineering, and validation.
- Executes automated tests using Pytest.
- Generates test results and code coverage reports.
- Uploads the test and coverage reports as workflow artifacts.

### Job 3: Model Quality Gate

- Installs project dependencies.
- Runs `tests/test_model_quality.py`.
- Checks whether the model meets the minimum acceptable accuracy defined in the test.

The model-quality test uses a minimum acceptable accuracy threshold of 0.80.

## 5. Execution Results

The latest GitHub Actions workflow run completed successfully, as indicated by the green check mark on GitHub.

The pipeline provides automated checks for syntax, code style, data processing, automated tests, and model quality.

## 6. Conclusion

The CI pipeline was implemented using GitHub Actions. It automates code validation, testing, and model-quality verification, helping identify issues early and maintain the reliability of the Iris Classifier project.
