import random
import pandas as pd

data=[]

for i in range(10000):

    obj=random.choice(
        [
            "Drone",
            "Fighter",
            "Missile",
            "Helicopter",
            "Unknown"
        ]
    )

    if obj=="Drone":

        speed=random.randint(50,150)
        altitude=random.randint(100,500)
        acceleration=random.randint(1,4)
        signature=random.randint(1,3)
        trajectory=random.randint(0,30)

    elif obj=="Fighter":

        speed=random.randint(700,1200)
        altitude=random.randint(8000,15000)
        acceleration=random.randint(6,12)
        signature=random.randint(7,10)
        trajectory=random.randint(30,70)

    elif obj=="Missile":

        speed=random.randint(1200,3000)
        altitude=random.randint(500,12000)
        acceleration=random.randint(10,20)
        signature=random.randint(4,8)
        trajectory=random.randint(70,90)

    elif obj=="Helicopter":

        speed=random.randint(150,300)
        altitude=random.randint(500,3000)
        acceleration=random.randint(2,5)
        signature=random.randint(5,8)
        trajectory=random.randint(10,40)

    else:

        speed=random.randint(50,2500)
        altitude=random.randint(100,15000)
        acceleration=random.randint(1,20)
        signature=random.randint(1,10)
        trajectory=random.randint(0,90)

    distance=random.randint(
        5,
        100
    )

    direction=random.choice(
        [
            "Towards",
            "Away"
        ]
    )

    data.append([
        speed,
        altitude,
        distance,
        direction,
        acceleration,
        signature,
        trajectory,
        obj
    ])

df=pd.DataFrame(

    data,

    columns=[

        "Speed",
        "Altitude",
        "Distance",
        "Direction",
        "Acceleration",
        "RadarSignature",
        "TrajectoryAngle",
        "ObjectType"
    ]
)

df.to_csv(
    "data/radar_data.csv",
    index=False
)

print(df.head())

print(
    "\nRealistic radar data generated"
)