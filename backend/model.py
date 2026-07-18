import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def preprocess_workforce_data(dataframe):
    """Label-encode categorical features for tree-based modeling."""

    ml_df = dataframe.copy()
    categorical_cols = ml_df.select_dtypes(include="object").columns

    encoders = {}

    for col in categorical_cols:
        encoder = LabelEncoder()
        ml_df[col] = encoder.fit_transform(ml_df[col])
        encoders[col] = encoder

    return ml_df, encoders


def split_features_target(dataframe):
    """Split the encoded frame into features (X) and target (y)."""

    return dataframe.drop("Attrition", axis=1), dataframe["Attrition"]


def train_random_forest(X_train, y_train):
    """Train the Random Forest attrition classifier."""

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    return model


def evaluate_model(model, X_test, y_test):
    """Evaluate held-out prediction accuracy."""

    return round(accuracy_score(y_test, model.predict(X_test)), 4)


@st.cache_resource(show_spinner=False)
def train_workforce_model(dataframe):
    """End-to-end workforce attrition model pipeline.

    Cached on the input dataframe's content so switching between dashboard
    pages or filters doesn't retrain the model on every rerun.
    """

    ml_df, encoders = preprocess_workforce_data(dataframe)
    X, y = split_features_target(ml_df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = train_random_forest(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)

    return {"model": model, "accuracy": accuracy, "X": X, "encoders": encoders}