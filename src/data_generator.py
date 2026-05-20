"""
VAJRA ADS V3
Realistic Multi-Target Radar Generator
"""

import random
import uuid
from datetime import datetime
import pandas as pd

NUM_TARGETS = 10000

objects = [

    "Drone",
    "Missile",
    "Fighter",
    "Helicopter",
    "FriendlyAircraft",
    "CivilianAircraft",
    "Unknown",
    "FalsePositive"

]

data=[]

for i in range(NUM_TARGETS):

    target_id="T-"+str(uuid.uuid4())[:8]

    timestamp=\
    datetime.now().strftime(
        "%H:%M:%S"
    )

    obj=random.choice(objects)

    if obj=="Drone":

        speed=random.randint(50,150)
        altitude=random.randint(100,500)
        acceleration=random.randint(1,4)
        radar_signature=random.randint(1,3)
        trajectory=random.randint(5,30)
        heading=random.randint(0,360)
        target_size=random.randint(1,3)
        electronic=random.randint(1,3)
        maneuver=random.randint(5,8)

    elif obj=="Missile":

        speed=random.randint(1200,3000)
        altitude=random.randint(500,12000)
        acceleration=random.randint(10,20)
        radar_signature=random.randint(5,9)
        trajectory=random.randint(60,90)
        heading=random.randint(0,360)
        target_size=random.randint(2,5)
        electronic=random.randint(6,10)
        maneuver=random.randint(8,10)

    elif obj=="Fighter":

        speed=random.randint(700,1200)
        altitude=random.randint(8000,15000)
        acceleration=random.randint(6,12)
        radar_signature=random.randint(7,10)
        trajectory=random.randint(20,70)
        heading=random.randint(0,360)
        target_size=random.randint(6,10)
        electronic=random.randint(7,10)
        maneuver=random.randint(7,10)

    elif obj=="Helicopter":

        speed=random.randint(150,300)
        altitude=random.randint(500,3000)
        acceleration=random.randint(2,5)
        radar_signature=random.randint(5,8)
        trajectory=random.randint(5,40)
        heading=random.randint(0,360)
        target_size=random.randint(5,8)
        electronic=random.randint(4,6)
        maneuver=random.randint(2,5)

    elif obj=="FriendlyAircraft":

        speed=random.randint(500,900)
        altitude=random.randint(5000,12000)
        acceleration=random.randint(4,8)
        radar_signature=random.randint(5,9)
        trajectory=random.randint(10,60)
        heading=random.randint(0,360)
        target_size=random.randint(6,10)
        electronic=random.randint(3,6)
        maneuver=random.randint(4,7)

    elif obj=="CivilianAircraft":

        speed=random.randint(600,900)
        altitude=random.randint(8000,13000)
        acceleration=random.randint(2,5)
        radar_signature=random.randint(6,9)
        trajectory=random.randint(5,30)
        heading=random.randint(0,360)
        target_size=random.randint(8,10)
        electronic=random.randint(2,5)
        maneuver=random.randint(1,4)

    elif obj=="FalsePositive":

        speed=random.randint(0,80)
        altitude=random.randint(0,300)
        acceleration=random.randint(0,2)
        radar_signature=random.randint(0,2)
        trajectory=random.randint(0,10)
        heading=random.randint(0,360)
        target_size=random.randint(0,2)
        electronic=random.randint(0,1)
        maneuver=random.randint(0,2)

    else:

        speed=random.randint(50,2500)
        altitude=random.randint(100,15000)
        acceleration=random.randint(1,20)
        radar_signature=random.randint(1,10)
        trajectory=random.randint(0,90)
        heading=random.randint(0,360)
        target_size=random.randint(1,10)
        electronic=random.randint(1,10)
        maneuver=random.randint(1,10)

    distance=random.randint(
        5,
        150
    )

    direction=random.choice(
        [
            "Towards",
            "Away"
        ]
    )

    time_to_impact=round(
        distance/(speed+1),
        2
    )

    approach_score=round(
        speed/(distance+1),
        2
    )

    data.append([

        target_id,
        timestamp,

        speed,
        altitude,
        distance,
        direction,

        acceleration,
        radar_signature,
        trajectory,
        heading,

        target_size,
        electronic,
        maneuver,

        time_to_impact,
        approach_score,

        obj

    ])

df=pd.DataFrame(

data,

columns=[

"TargetID",
"Timestamp",

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

"ObjectType"

])

df.to_csv(
"data/radar_data.csv",
index=False
)

print(df.head())

print(
"\nVAJRA realistic radar data generated"
)