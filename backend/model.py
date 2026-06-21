from sklearn.model_selection import (
    train_test_split
)

from sklearn.preprocessing import (
    LabelEncoder
)

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.metrics import (
    accuracy_score
)


def preprocess_workforce_data(
    dataframe
):
    """Encode categorical features."""

    ml_df = dataframe.copy()

    categorical_cols = (
        ml_df
        .select_dtypes(
            include="object"
        )
        .columns
    )

    encoders = {}

    for col in categorical_cols:

        encoder = LabelEncoder()

        ml_df[col] = (
            encoder.fit_transform(
                ml_df[col]
            )
        )

        encoders[col] = encoder

    return ml_df, encoders


def split_features_target(
    dataframe
):
    """Split features & target."""

    X = dataframe.drop(
        "Attrition",
        axis=1
    )

    y = dataframe[
        "Attrition"
    ]

    return X, y


def create_train_test_split(
    X,
    y
):
    """Generate train-test split."""

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


def train_random_forest(
    X_train,
    y_train
):
    """Train Random Forest model."""

    rf_model = (
        RandomForestClassifier(
            n_estimators=200,
            random_state=42
        )
    )

    rf_model.fit(
        X_train,
        y_train
    )

    return rf_model


def evaluate_model(
    model,
    X_test,
    y_test
):
    """Evaluate prediction accuracy."""

    y_pred = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    return round(
        accuracy,
        4
    )


def train_workforce_model(
    dataframe
):
    """End-to-end workforce model pipeline."""

    ml_df, encoders = (
        preprocess_workforce_data(
            dataframe
        )
    )

    X, y = (
        split_features_target(
            ml_df
        )
    )

    (
        X_train,
        X_test,
        y_train,
        y_test
    ) = create_train_test_split(
        X,
        y
    )

    model = (
        train_random_forest(
            X_train,
            y_train
        )
    )

    accuracy = (
        evaluate_model(
            model,
            X_test,
            y_test
        )
    )

    return {
        "model": model,
        "accuracy": accuracy,
        "X": X,
        "encoders": encoders
    }