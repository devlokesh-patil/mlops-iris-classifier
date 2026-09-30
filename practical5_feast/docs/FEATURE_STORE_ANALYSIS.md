# Feature Store Analysis

## 1. Feature Store Implementation

Feast was used to create a local feature repository for the Iris dataset.

The feature repository contains:

- Entity: `sample_id`
- Feature View: `iris_measurements`
- Feature View: `iris_engineered_features`
- Feature Service: `iris_feature_service`
- SQLite online store
- Parquet offline source

## 2. Online Feature Retrieval

The online retrieval test successfully retrieved the registered features for `sample_id = 1`.

Retrieved features included:

- Sepal measurements
- Petal measurements
- `sepal_area`
- `petal_area`
- `sepal_to_petal_length_ratio`
- `petal_length_bin`

This demonstrates low-latency online feature retrieval.

## 3. Offline / Historical Feature Retrieval

Historical feature retrieval was performed using Feast's
`get_historical_features` API.

The experiment retrieved 5 historical records using the entity
timestamp information.

The retrieved records contained the original Iris measurements and
the registered engineered features.

This demonstrates point-in-time historical feature retrieval.

## 4. Feature Reusability

The `iris_feature_service` was reused to retrieve the same registered
features for another model use case.

No separate implementation of the engineered features was required.

The Feature Service successfully returned all registered features for
`sample_id = 1`.

## 5. Benefits of the Feature Store

### Elimination of Training-Serving Skew

The same registered feature definitions are used for both online and
offline retrieval. This helps maintain consistency between features
used during training and features available during serving.

### Feature Reusability

Registered features can be reused by different models without
re-implementing the same feature engineering logic.

### Centralized Governance

The feature definitions are maintained centrally in `features.py`.
This provides a single source of truth for the registered features.

## 6. Conclusion

The experiment demonstrated the creation of a Feast feature repository,
feature registration, data materialization into the online store,
online feature retrieval, historical feature retrieval, and feature
reuse through a Feature Service.