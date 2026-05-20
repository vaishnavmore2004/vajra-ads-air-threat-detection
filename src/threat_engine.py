"""
VAJRA ADS - Threat Analysis Engine V1
-------------------------------------
Purpose:
Assign threat levels to detected aerial objects.

Features:
✓ Logging
✓ Validation
✓ Configurable thresholds
✓ Distance-aware logic
✓ Clean beginner-friendly structure
✓ Saves threat_data.csv
"""

import pandas as pd
import logging

# ==============================
# Logging Setup
# ==============================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)

log = logging.getLogger()

# ==============================
# Configuration
# ==============================

FIGHTER_SPEED_THRESHOLD = 900
CRITICAL_DISTANCE = 50

# ==============================
# Load Dataset
# ==============================

log.info("Loading radar data...")

df = pd.read_csv("data/radar_data.csv")

# ==============================
# Validation
# ==============================

required_columns = [
    "Speed",
    "Distance",
    "ObjectType",
    "Direction"
]

missing=[]

for col in required_columns:

    if col not in df.columns:
        missing.append(col)

if missing:

    raise ValueError(
        f"Missing columns: {missing}"
    )

log.info(
    "Loaded %d targets",
    len(df)
)

# ==============================
# Threat Logic
# ==============================

def assign_threat(row):

    speed=row["Speed"]

    distance=row["Distance"]

    obj=row["ObjectType"]

    direction=row["Direction"]


    # Missile approaching

    if obj=="Missile" and direction=="Towards":

        if distance<CRITICAL_DISTANCE:

            return "Critical"

        return "High"


    # Fighter approaching

    elif obj=="Fighter":

        if speed>FIGHTER_SPEED_THRESHOLD and direction=="Towards":

            if distance<CRITICAL_DISTANCE:

                return "Critical"

            return "High"

        return "Medium"


    # Drone

    elif obj=="Drone":

        if direction=="Towards":

            return "Low"

        return "Unknown"


    # Helicopter

    elif obj=="Helicopter":

        return "Medium"


    else:

        return "Unknown"


# ==============================
# Apply Logic
# ==============================

df["ThreatLevel"]=df.apply(
    assign_threat,
    axis=1
)

# ==============================
# Summary
# ==============================

log.info(
    "\n%s",
    df["ThreatLevel"].value_counts()
)

# ==============================
# Save
# ==============================

df.to_csv(
    "data/threat_data.csv",
    index=False
)

log.info(
    "Saved to data/threat_data.csv"
)

print("\nSample Output:\n")

print(
    df[
        [
            "ObjectType",
            "Speed",
            "Distance",
            "Direction",
            "ThreatLevel"
        ]
    ].head(10)
)