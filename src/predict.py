"""
VAJRA ADS
AI-Powered Air Threat Detection & Prioritization System
Backend Freeze v1
"""

import random
import uuid
from datetime import datetime

import joblib
import pandas as pd


# =========================================================
# LOAD TRAINED MODELS
# =========================================================

model = joblib.load(
    "models/vajra_model.pkl"
)

threat_encoder = joblib.load(
    "models/threat_encoder.pkl"
)


# =========================================================
# FIXED DIRECTION MAP
# =========================================================

direction_map = {

    "Away":0,

    "Towards":1

}


# =========================================================
# TARGET TYPES
# =========================================================

TARGET_TYPES=[

    "Missile",

    "Drone",

    "Fighter",

    "Helicopter",

    "FriendlyAircraft",

    "CivilianAircraft",

    "Unknown",

    "FalsePositive"

]


targets=[]


# =========================================================
# GENERATE TARGETS
# =========================================================

for _ in range(6):

    obj=random.choice(
        TARGET_TYPES
    )

    if obj=="Missile":

        speed=random.randint(
            1200,
            3000
        )

        altitude=random.randint(
            1000,
            12000
        )

        acceleration=random.randint(
            10,
            20
        )

        radar=random.randint(
            6,
            10
        )

        trajectory=random.randint(
            60,
            90
        )

        size=random.randint(
            2,
            5
        )

        electronic=random.randint(
            7,
            10
        )

        maneuver=random.randint(
            8,
            10
        )

    elif obj=="Drone":

        speed=random.randint(
            50,
            150
        )

        altitude=random.randint(
            100,
            1000
        )

        acceleration=random.randint(
            1,
            4
        )

        radar=random.randint(
            1,
            3
        )

        trajectory=random.randint(
            5,
            30
        )

        size=random.randint(
            1,
            3
        )

        electronic=random.randint(
            1,
            4
        )

        maneuver=random.randint(
            5,
            8
        )

    elif obj=="Fighter":

        speed=random.randint(
            700,
            1500
        )

        altitude=random.randint(
            5000,
            15000
        )

        acceleration=random.randint(
            5,
            12
        )

        radar=random.randint(
            7,
            10
        )

        trajectory=random.randint(
            20,
            70
        )

        size=random.randint(
            5,
            9
        )

        electronic=random.randint(
            7,
            10
        )

        maneuver=random.randint(
            7,
            10
        )

    elif obj=="Helicopter":

        speed=random.randint(
            150,
            350
        )

        altitude=random.randint(
            100,
            4000
        )

        acceleration=random.randint(
            2,
            5
        )

        radar=random.randint(
            4,
            7
        )

        trajectory=random.randint(
            10,
            40
        )

        size=random.randint(
            5,
            8
        )

        electronic=random.randint(
            3,
            6
        )

        maneuver=random.randint(
            2,
            5
        )

    elif obj=="FriendlyAircraft":

        speed=random.randint(
            500,
            900
        )

        altitude=random.randint(
            5000,
            12000
        )

        acceleration=random.randint(
            3,
            7
        )

        radar=random.randint(
            5,
            9
        )

        trajectory=random.randint(
            10,
            60
        )

        size=random.randint(
            6,
            10
        )

        electronic=random.randint(
            2,
            5
        )

        maneuver=random.randint(
            3,
            6
        )

    elif obj=="CivilianAircraft":

        speed=random.randint(
            500,
            850
        )

        altitude=random.randint(
            7000,
            13000
        )

        acceleration=random.randint(
            2,
            5
        )

        radar=random.randint(
            5,
            8
        )

        trajectory=random.randint(
            5,
            30
        )

        size=random.randint(
            7,
            10
        )

        electronic=random.randint(
            1,
            4
        )

        maneuver=random.randint(
            1,
            4
        )

    elif obj=="FalsePositive":

        speed=random.randint(0,80)
        altitude=random.randint(0,300)
        acceleration=random.randint(0,2)
        radar=random.randint(0,2)
        trajectory=random.randint(0,10)
        size=random.randint(0,2)
        electronic=random.randint(0,1)
        maneuver=random.randint(0,2)

    else:

        speed=random.randint(50,2500)
        altitude=random.randint(100,15000)
        acceleration=random.randint(1,20)
        radar=random.randint(1,10)
        trajectory=random.randint(0,90)
        size=random.randint(1,10)
        electronic=random.randint(1,10)
        maneuver=random.randint(1,10)

    direction=random.choice(
        ["Towards","Away"]
    )

    distance=random.randint(
        5,
        150
    )

    target={

        "TargetID":
        "T-"+str(uuid.uuid4())[:6],

        "Timestamp":
        datetime.now().strftime("%H:%M:%S"),

        "ObjectType":
        obj,

        "Speed":
        speed,

        "Altitude":
        altitude,

        "Distance":
        distance,

        "Direction":
        direction,

        "Acceleration":
        acceleration,

        "RadarSignature":
        radar,

        "TrajectoryAngle":
        trajectory,

        "HeadingAngle":
        random.randint(0,360),

        "TargetSize":
        size,

        "ElectronicSignature":
        electronic,

        "Maneuverability":
        maneuver,

        "TimeToImpact":
        round(
            distance/(speed+1),
            3
        ),

        "ApproachScore":
        round(
            speed/(distance+1),
            2
        )
    }

    targets.append(target)


sample=pd.DataFrame(targets)

sample["Direction"]=sample[
"Direction"
].map(
direction_map
)

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

X=sample[FEATURES]

pred=model.predict(X)

prob=model.predict_proba(X)

sample["ThreatLevel"]=(
threat_encoder.inverse_transform(pred)
)

sample["Confidence"]=(
prob.max(axis=1)
)

# =========================================================
# RULE ENGINE
# =========================================================

def adjust_threat(row):

    obj=row["ObjectType"]

    speed=row["Speed"]

    distance=row["Distance"]

    direction=row["Direction"]

    electronic=row[
    "ElectronicSignature"
    ]

    maneuver=row[
    "Maneuverability"
    ]

    if obj in [
    "FriendlyAircraft",
    "CivilianAircraft"
    ]:
        return "Safe"

    if obj=="FalsePositive":
        return "Ignore"

    if obj=="Missile":

        if direction==1:

            if speed>1000 and distance<80:

                return "Critical"

            return "High"

        return "Medium"


    if obj=="Fighter":

        if (
            speed>1200
            and distance<30
            and direction==1
            and electronic>7
            and maneuver>7
        ):

            return "Critical"


        if (
            speed>900
            and
            (
                electronic>7
                or maneuver>7
            )
        ):

            return "High"

        return "Medium"


    if obj=="Drone":

        if (
            distance<30
            or direction==1
            or maneuver>7
        ):

            return "Medium"

        return "Low"


    if obj=="Helicopter":

        if distance<50 or direction==1:

            return "Medium"

        return "Low"


    if obj=="Unknown":

        indicators=0

        if speed>1000:
            indicators+=1

        if electronic>7:
            indicators+=1

        if maneuver>7:
            indicators+=1

        if distance<50:
            indicators+=1

        if direction==1:
            indicators+=1

        if indicators>=4:
            return "High"

        if indicators>=2:
            return "Medium"

        return "Low"

    return row["ThreatLevel"]


sample["ThreatLevel"]=sample.apply(
adjust_threat,
axis=1
)

# =========================================================
# SCORE
# =========================================================

def calculate_score(row):

    level=row["ThreatLevel"]

    if level=="Ignore":
        return 0

    if level=="Safe":
        return 5

    base={

        "Critical":80,
        "High":60,
        "Medium":40,
        "Low":20

    }

    score=base.get(level,20)

    score += min(
        row["Speed"]/300,
        10
    )

    score += min(
        (150-row["Distance"])/15,
        10
    )

    score += row[
        "ElectronicSignature"
    ]

    score += row[
        "Maneuverability"
    ]

    if row["Direction"]==1:
        score+=10

    if row["TimeToImpact"]<0.05:
        score+=10

    return round(
        min(score,100)
    )


sample["ThreatScore"]=sample.apply(
calculate_score,
axis=1
)

sample=sample.sort_values(
by="ThreatScore",
ascending=False
)

sample["PriorityRank"]=range(
1,
len(sample)+1
)

# =========================================================
# DEFENSE
# =========================================================

def defense(row):

    obj = row["ObjectType"]
    level = row["ThreatLevel"]

    if obj == "Missile":

        if level == "Critical":
            return "LongRangeInterceptor"

        return "SurfaceToAirMissileReady"

    mapping = {

        "High":"SurfaceToAirMissile",

        "Medium":"ElectronicMonitoring",

        "Low":"TrackTarget",

        "Safe":"NoAction",

        "Ignore":"Ignore"

    }

    return mapping.get(
        level,
        "ManualReview"
    )


sample["Defense"] = sample.apply(
    defense,
    axis=1
)


# =========================================================
# EXPLAINABILITY
# =========================================================

def reason(row):

    obj = row["ObjectType"]

    if obj=="FriendlyAircraft":
        return "IFF authenticated"

    if obj=="CivilianAircraft":
        return "Civilian corridor"

    if obj=="FalsePositive":
        return "Sensor anomaly"

    reasons=[]

    if row["Speed"]>1000:
        reasons.append(
            "High speed"
        )

    if row["Distance"]<50:
        reasons.append(
            "Close range"
        )

    if row["ElectronicSignature"]>7:
        reasons.append(
            "Electronic activity"
        )

    if row["Maneuverability"]>7:
        reasons.append(
            "Aggressive maneuvers"
        )

    if row["Direction"]==1:
        reasons.append(
            "Approaching protected zone"
        )

    if not reasons:
        reasons.append(
            "Routine behavior"
        )

    return ", ".join(reasons)


sample["Reason"] = sample.apply(
    reason,
    axis=1
)


# =========================================================
# COMMAND CENTRE OUTPUT
# =========================================================

print("\n"+"="*70)

print("VAJRA COMMAND CENTRE")

print("="*70)

for _, row in sample.iterrows():

    print()

    print(
        f"Target ID: {row['TargetID']}"
    )

    print(
        f"Target Type: {row['ObjectType']}"
    )

    print(
        f"Threat: {row['ThreatLevel']}"
    )

    print(
        f"Confidence: {row['Confidence']:.2%}"
    )

    print(
        f"Threat Score: {row['ThreatScore']}/100"
    )

    print(
        f"Priority Rank: {row['PriorityRank']}"
    )

    print(
        f"Defense: {row['Defense']}"
    )

    print(
        f"Reason: {row['Reason']}"
    )

print("\n"+"="*70) 
