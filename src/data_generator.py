import random
import pandas as pd

objects = ["Drone", "Fighter", "Missile", "Helicopter", "Unknown"]

data = []

for i in range(100):

    obj = random.choice(objects)

    if obj == "Drone":
        speed = random.randint(50,150)
        altitude = random.randint(100,500)
        distance = random.randint(5,30)

    elif obj == "Fighter":
        speed = random.randint(700,1200)
        altitude = random.randint(8000,15000)
        distance = random.randint(20,100)

    elif obj == "Missile":
        speed = random.randint(1000,3000)
        altitude = random.randint(500,10000)
        distance = random.randint(10,80)

    elif obj == "Helicopter":
        speed = random.randint(150,300)
        altitude = random.randint(500,3000)
        distance = random.randint(10,40)

    else:
        speed = random.randint(50,2500)
        altitude = random.randint(100,15000)
        distance = random.randint(5,100)

    direction = random.choice(
        ["Towards","Away"]
    )

    data.append(
        [speed,
         altitude,
         distance,
         direction,
         obj]
    )

df = pd.DataFrame(
    data,
    columns=[
        "Speed",
        "Altitude",
        "Distance",
        "Direction",
        "ObjectType"
    ]
)

print(df.head())

df.to_csv(
    "data/radar_data.csv",
    index=False
)

print("Radar dataset generated successfully")