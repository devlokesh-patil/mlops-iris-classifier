# Hyperparameter Tuning Analysis

## 1. Objective

The objective of this experiment is to develop a baseline model and systematically improve model performance using Grid Search and Random Search hyperparameter tuning with cross-validation. All experiments are tracked using MLflow for comparison and analysis.

## 2. Baseline Model Performance

The baseline model used was a `DecisionTreeClassifier`.

- Cross-Validation F1 Macro: **0.9663**
- Test Accuracy: **0.9000**
- Total Fits: **5**

The baseline provides a reference point for evaluating the improvement obtained through hyperparameter tuning.

## 3. Grid Search Results

Grid Search was performed using a Random Forest classifier.

- Hyperparameter combinations: **72**
- Cross-validation folds: **5**
- Total fits: **360**
- Best CV F1 Macro: **0.9663**
- Test Accuracy: **0.9667**

Best parameters:

- `n_estimators`: **50**
- `max_depth`: **3**
- `min_samples_split`: **2**
- `max_features`: **sqrt**

Grid Search exhaustively evaluates all specified hyperparameter combinations and selects the configuration with the best cross-validation score.

## 4. Random Search Results

Random Search was performed using a Random Forest classifier.

- Iterations: **30**
- Cross-validation folds: **5**
- Total fits: **150**
- Best CV F1 Macro: **0.9663**
- Test Accuracy: **0.9667**

Best parameters:

- `n_estimators`: **100**
- `max_depth`: **3**
- `min_samples_split`: **6**
- `max_features`: **sqrt**

Random Search evaluates a selected number of randomly sampled configurations instead of exhaustively evaluating every possible combination.

## 5. Comparative Analysis

| Method | CV F1 Macro | Test Accuracy | Total Fits |
|---|---:|---:|---:|
| Baseline Decision Tree | 0.9663 | 0.9000 | 5 |
| Grid Search Random Forest | 0.9663 | 0.9667 | 360 |
| Random Search Random Forest | 0.9663 | 0.9667 | 150 |

Both tuned Random Forest approaches achieved higher test accuracy than the baseline model.

Grid Search evaluated **360 fits**, while Random Search evaluated only **150 fits**, which is less than half the number of Grid Search fits.

In this experiment, Grid Search and Random Search achieved the same CV F1 Macro and test accuracy. Therefore, Random Search provided the same observed performance while requiring substantially fewer model fits.

## 6. Conclusion

Hyperparameter tuning improved the test accuracy from **0.9000** for the baseline Decision Tree to **0.9667** for both tuned Random Forest approaches.

Grid Search provides exhaustive evaluation of the defined parameter space, whereas Random Search explores a limited number of configurations. For this experiment, Random Search achieved the same observed performance as Grid Search with **150 fits compared with 360 fits**, making it more computationally efficient.

All three experiments were tracked using MLflow under the `iris-hyperparameter-tuning` experiment