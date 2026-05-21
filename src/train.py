"""
VAJRA ADS V3
Command Centre AI Training Engine
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

# =======================================
# Logging
# =======================================

logging.basicConfig(

level=logging.INFO,

format="%(asctime)s | %(levelname)s | %(message)s",

datefmt="%H:%M:%S"

)

log=logging.getLogger()

RANDOM_STATE=42

# =======================================
# Load data
# =======================================

log.info(
"Loading processed data..."
)

df=pd.read_csv(
"data/processed_data.csv"
)

log.info(
"Loaded %d tracks",
len(df)
)

# =======================================
# Features
# =======================================

FEATURES=[

"Speed",

"Altitude",

"Distance",

"Direction",

"Acceleration",

"RadarSignature",

"TrajectoryAngle",

"HeadingAngle",

"TargetSize",

"ElectronicSignature",

"Maneuverability",

"TimeToImpact",

"ApproachScore"

]

TARGET="ThreatLevel"

X=df[FEATURES]

y=df[TARGET]

# =======================================
# Split
# =======================================

X_train,\
X_test,\
y_train,\
y_test=\
train_test_split(

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

# =======================================
# Model
# =======================================

model=RandomForestClassifier(

n_estimators=400,

max_depth=14,

min_samples_split=5,

min_samples_leaf=2,

class_weight="balanced",

n_jobs=-1,

random_state=RANDOM_STATE

)

log.info(
"Training VAJRA AI..."
)

model.fit(
X_train,
y_train
)

# =======================================
# Predict
# =======================================

pred=model.predict(
X_test
)

accuracy=accuracy_score(
y_test,
pred
)

print("\n")
print("="*50)

print(
"VAJRA COMMAND AI RESULTS"
)

print("="*50)

print(
f"\nAccuracy:{accuracy:.4f}"
)

print(
"\nClassification Report:\n"
)

print(
classification_report(
y_test,
pred
)
)

# =======================================
# Importance
# =======================================

importance=pd.DataFrame({

"Feature":
FEATURES,

"Importance":
model.feature_importances_

})

importance=\
importance.sort_values(

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

# =======================================
# Confusion Matrix
# =======================================

cm=confusion_matrix(
y_test,
pred
)

disp=\
ConfusionMatrixDisplay(
confusion_matrix=cm
)

disp.plot()

plt.title(
"VAJRA Command AI Matrix"
)

plt.savefig(
"models/confusion_matrix.png"
)

plt.show()

# =======================================
# Save
# =======================================

joblib.dump(

model,

"models/vajra_model.pkl"

)

log.info(
"VAJRA AI saved"
)