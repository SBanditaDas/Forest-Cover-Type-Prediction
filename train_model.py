import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

from src.preprocessing import preprocess_data

def main():
    
    df = pd.read_csv("data/train.csv")

    # Preprocess
    df = preprocess_data(df)
    X = df.drop("Cover_Type", axis=1)
    y = df["Cover_Type"]

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Saving the model
    joblib.dump(model, "models/random_forest_model.pkl")

if __name__ == "__main__":
    main()