"""
VAJRA ADS
Preprocessing Module
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

log=logging.getLogger()

log.info("Loading threat dataset...")

df=pd.read_csv(
    "data/threat_data.csv"
)

# =========================
# Encode categorical data
# =========================

direction_encoder=LabelEncoder()

object_encoder=LabelEncoder()

threat_encoder=LabelEncoder()

df["Direction"]=direction_encoder.fit_transform(
    df["Direction"]
)

df["ObjectType"]=object_encoder.fit_transform(
    df["ObjectType"]
)

df["ThreatLevel"]=threat_encoder.fit_transform(
    df["ThreatLevel"]
)

# =========================
# Save encoders
# =========================

joblib.dump(
    direction_encoder,
    "models/direction_encoder.pkl"
)

joblib.dump(
    object_encoder,
    "models/object_encoder.pkl"
)

joblib.dump(
    threat_encoder,
    "models/threat_encoder.pkl"
)

# =========================
# Save processed data
# =========================

df.to_csv(
    "data/processed_data.csv",
    index=False
)

log.info(
    "Preprocessing complete"
)

print("\nEncoded Sample:\n")

print(df.head())