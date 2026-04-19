import json
import sqlite3
import os

def seed():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plantName TEXT NOT NULL UNIQUE,
            plantShortDescription TEXT NOT NULL UNIQUE,
            plantMediumDescription TEXT NOT NULL UNIQUE,
            plantLongDescription TEXT NOT NULL UNIQUE,
            minimumdegrees TEXT NOT NULL,
            stateofTemperature TEXT NOT NULL,
            numberOfWater TEXT NOT NULL,
            plantCareInstruct TEXT NOT NULL,
            plantImage1 TEXT NOT NULL,
            plantImage2 TEXT NOT NULL
        )
    ''')

    with open('models/plants_data/data.json', 'r') as f:
        plants = json.load(f)

    inserted = 0
    skipped = 0

    for plant in plants:
        name = plant['plantName']
        cursor.execute("SELECT id FROM plants WHERE plantName=?", (name,))
        if cursor.fetchone():
            skipped += 1
            continue

        cursor.execute('''
            INSERT INTO plants
            (plantName, plantShortDescription, plantMediumDescription, plantLongDescription,
             minimumdegrees, stateofTemperature, numberOfWater, plantCareInstruct,
             plantImage1, plantImage2)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            name,
            plant['plantShortDescription'],
            plant['plantMediumDescription'],
            plant['plantLongDescription'],
            plant['minimumdegrees'],
            plant['stateofTemperature'],
            plant['numberOfWater'],
            plant['plantCareInstruct'],
            f"/uploads/plants_photos1/{name}.png",
            f"/uploads/plants_photos2/{name}.jpeg"
        ))
        inserted += 1
        print(f"  + {name}")

    conn.commit()
    conn.close()
    print(f"\nDone: {inserted} inserted, {skipped} skipped.")

if __name__ == "__main__":
    seed()
