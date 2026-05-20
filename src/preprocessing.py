"""
VAJRA ADS V3
Command Centre Preprocessing Pipeline
"""

import pandas as pd
import joblib
import logging

from sklearn.preprocessing import LabelEncoder

# =======================================
# Logging
# =======================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)

log=logging.getLogger()

log.info(
    "Loading threat dataset..."
)

df=pd.read_csv(
    "data/threat_data.csv"
)

# =======================================
# Validation
# =======================================

required=[

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
"ApproachScore",

"ThreatLevel"

]

missing=[]

for col in required:

    if col not in df.columns:

        missing.append(col)

if missing:

    raise ValueError(
        f"Missing columns: {missing}"
    )

# =======================================
# Encoders
# =======================================

direction_encoder=LabelEncoder()

threat_encoder=LabelEncoder()

df["Direction"]=\
direction_encoder.fit_transform(
df["Direction"]
)

df["ThreatLevel"]=\
threat_encoder.fit_transform(
df["ThreatLevel"]
)

# =======================================
# Save encoders
# =======================================

joblib.dump(
direction_encoder,
"models/direction_encoder.pkl"
)

joblib.dump(
threat_encoder,
"models/threat_encoder.pkl"
)

# =======================================
# Save processed dataset
# =======================================

df.to_csv(
"data/processed_data.csv",
index=False
)

log.info(
"Preprocessing complete"
)

print("\nProcessed Sample:\n")

print(

df[
[
"Speed",
"Distance",
"Direction",
"ApproachScore",
"ThreatLevel"
]
].head(10)

)