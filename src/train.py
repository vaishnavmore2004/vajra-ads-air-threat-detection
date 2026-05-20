"""
VAJRA ADS
Realistic AI Training Engine V2
"""

import logging
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# ============================================
# Logging
# ============================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)

log = logging.getLogger()

RANDOM_STATE = 42

# ============================================
# Load dataset
# ============================================

log.info("Loading processed dataset...")

df = pd.read_csv("data/processed_data.csv")

log.info(
    "Loaded %d targets",
    len(df)
)

# ============================================
# Required columns
# ============================================

required = [

    "Speed",
    "Altitude",
    "Distance",
    "Direction",
    "Acceleration",
    "RadarSignature",
    "TrajectoryAngle",
    "ThreatLevel"

]

missing = []

for col in required:

    if col not in df.columns:

        missing.append(col)

if missing:

    raise ValueError(
        f"Missing columns: {missing}"
    )

# ============================================
# Features
# ============================================

FEATURES = [

    "Speed",

    "Altitude",

    "Distance",

    "Direction",

    "Acceleration",

    "RadarSignature",

    "TrajectoryAngle"

]

TARGET = "ThreatLevel"

X = df[FEATURES]

y = df[TARGET]

# ============================================
# Train Test Split
# ============================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=RANDOM_STATE,

    stratify=y

)

log.info(
    "Training samples: %d",
    len(X_train)
)

log.info(
    "Testing samples: %d",
    len(X_test)
)

# ============================================
# Model
# ============================================

model = RandomForestClassifier(

    n_estimators=300,

    max_depth=12,

    min_samples_split=5,

    min_samples_leaf=2,

    class_weight="balanced",

    random_state=RANDOM_STATE,

    n_jobs=-1
)

log.info(
    "Training VAJRA AI..."
)

model.fit(
    X_train,
    y_train
)

# ============================================
# Prediction
# ============================================

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n")
print("="*50)
print("VAJRA AI RESULTS")
print("="*50)

print(
    f"\nAccuracy: {accuracy:.4f}"
)

print(
    "\nClassification Report:\n"
)

print(
    classification_report(
        y_test,
        predictions
    )
)

# ============================================
# Feature Importance
# ============================================

importance = pd.DataFrame({

    "Feature": FEATURES,

    "Importance":
    model.feature_importances_

})

importance = importance.sort_values(

    by="Importance",

    ascending=False

)

print(
    "\nFeature Importance:\n"
)

print(
    importance.to_string(
        index=False
    )
)

# ============================================
# Confusion Matrix
# ============================================

cm = confusion_matrix(
    y_test,
    predictions
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot()

plt.title(
    "VAJRA Threat Confusion Matrix"
)

# save graph too
plt.savefig(
    "models/confusion_matrix.png"
)

plt.show()

# ============================================
# Save model
# ============================================

joblib.dump(
    model,
    "models/vajra_model.pkl"
)

log.info(
    "Model saved successfully"
)

print(
    "\nSaved:"
)

print(
    "models/vajra_model.pkl"
)