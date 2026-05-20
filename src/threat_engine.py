"""
VAJRA ADS V3
Command Centre Threat Evaluation Engine
"""

import logging
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)

log=logging.getLogger()

log.info(
    "Loading radar tracks..."
)

df=pd.read_csv(
    "data/radar_data.csv"
)

# ===================================
# Threat Logic
# ===================================

def evaluate_threat(row):

    speed=row["Speed"]

    distance=row["Distance"]

    direction=row["Direction"]

    acceleration=row["Acceleration"]

    maneuver=row["Maneuverability"]

    electronic=row["ElectronicSignature"]

    tti=row["TimeToImpact"]

    obj=row["ObjectType"]


    # Friendly traffic

    if obj=="FriendlyAircraft":

        return "Safe"


    if obj=="CivilianAircraft":

        return "Safe"


    if obj=="FalsePositive":

        return "Ignore"


    # Critical incoming threat

    if (

        direction=="Towards"

        and speed>1000

        and distance<50

        and acceleration>8

        and tti<0.10

    ):

        return "Critical"


    # Aggressive approaching target

    elif (

        direction=="Towards"

        and maneuver>7

        and electronic>6

        and distance<80

    ):

        return "High"


    # Suspicious object

    elif (

        direction=="Towards"

        and distance<100

    ):

        return "Medium"


    return "Low"


# ===================================

df["ThreatLevel"]=df.apply(
    evaluate_threat,
    axis=1
)

# ===================================
# Threat score
# ===================================

score=[]

for _,row in df.iterrows():

    value=0

    value+=row["ApproachScore"]*4

    value+=row["Acceleration"]*2

    value+=row["ElectronicSignature"]*3

    value+=row["Maneuverability"]*2

    if row["Direction"]=="Towards":

        value+=15

    score.append(
        round(value)
    )

df["ThreatScore"]=score

df=df.sort_values(
    by="ThreatScore",
    ascending=False
)

df["PriorityRank"]=range(
    1,
    len(df)+1
)

# ===================================
# Recommendation Engine
# ===================================

def recommend(row):

    level=row["ThreatLevel"]

    if level=="Critical":

        return "LongRangeInterceptor"

    elif level=="High":

        return "SurfaceToAirMissile"

    elif level=="Medium":

        return "ElectronicMonitoring"

    elif level=="Low":

        return "TrackTarget"

    return "Ignore"

df["RecommendedDefense"]=\
df.apply(
recommend,
axis=1
)

df.to_csv(
    "data/threat_data.csv",
    index=False
)

print(
df[
[
"TargetID",
"ObjectType",
"ThreatLevel",
"ThreatScore",
"PriorityRank",
"RecommendedDefense"
]
].head(15)
)

log.info(
"Threat analysis complete"
)