import sqlite3

plant_images = {
    "Tomato": (
        "https://images.pexels.com/photos/533280/pexels-photo-533280.jpeg?w=400",
        "https://images.pexels.com/photos/1327838/pexels-photo-1327838.jpeg?w=400"
    ),
    "Wheat": (
        "https://images.pexels.com/photos/326082/pexels-photo-326082.jpeg?w=400",
        "https://images.pexels.com/photos/265216/pexels-photo-265216.jpeg?w=400"
    ),
    "Rice": (
        "https://images.pexels.com/photos/4110251/pexels-photo-4110251.jpeg?w=400",
        "https://images.pexels.com/photos/2589457/pexels-photo-2589457.jpeg?w=400"
    ),
    "Maize": (
        "https://images.pexels.com/photos/547263/pexels-photo-547263.jpeg?w=400",
        "https://images.pexels.com/photos/1459534/pexels-photo-1459534.jpeg?w=400"
    ),
    "Potato": (
        "https://images.pexels.com/photos/144248/potatoes-vegetables-erdfrucht-bio-144248.jpeg?w=400",
        "https://images.pexels.com/photos/4087609/pexels-photo-4087609.jpeg?w=400"
    ),
    "Onion": (
        "https://images.pexels.com/photos/4197447/pexels-photo-4197447.jpeg?w=400",
        "https://images.pexels.com/photos/175414/pexels-photo-175414.jpeg?w=400"
    ),
    "Garlic": (
        "https://images.pexels.com/photos/4197444/pexels-photo-4197444.jpeg?w=400",
        "https://images.pexels.com/photos/3051412/pexels-photo-3051412.jpeg?w=400"
    ),
    "Cucumber": (
        "https://images.pexels.com/photos/2329440/pexels-photo-2329440.jpeg?w=400",
        "https://images.pexels.com/photos/37528/cucumber-salad-food-healthy-37528.jpeg?w=400"
    ),
    "Pepper": (
        "https://images.pexels.com/photos/1435904/pexels-photo-1435904.jpeg?w=400",
        "https://images.pexels.com/photos/128536/pexels-photo-128536.jpeg?w=400"
    ),
    "Eggplant": (
        "https://images.pexels.com/photos/4551488/pexels-photo-4551488.jpeg?w=400",
        "https://images.pexels.com/photos/3590797/pexels-photo-3590797.jpeg?w=400"
    ),
    "Carrot": (
        "https://images.pexels.com/photos/143133/pexels-photo-143133.jpeg?w=400",
        "https://images.pexels.com/photos/1306559/pexels-photo-1306559.jpeg?w=400"
    ),
    "Lettuce": (
        "https://images.pexels.com/photos/1199562/pexels-photo-1199562.jpeg?w=400",
        "https://images.pexels.com/photos/4893/food-healthy-meal-salad.jpg?w=400"
    ),
    "Spinach": (
        "https://images.pexels.com/photos/2325843/pexels-photo-2325843.jpeg?w=400",
        "https://images.pexels.com/photos/5765/food-salad-healthy-vegetables.jpg?w=400"
    ),
    "Cabbage": (
        "https://images.pexels.com/photos/2518893/pexels-photo-2518893.jpeg?w=400",
        "https://images.pexels.com/photos/8448322/pexels-photo-8448322.jpeg?w=400"
    ),
    "Cauliflower": (
        "https://images.pexels.com/photos/6316513/pexels-photo-6316513.jpeg?w=400",
        "https://images.pexels.com/photos/4963988/pexels-photo-4963988.jpeg?w=400"
    ),
    "Broccoli": (
        "https://images.pexels.com/photos/1353564/pexels-photo-1353564.jpeg?w=400",
        "https://images.pexels.com/photos/918643/pexels-photo-918643.jpeg?w=400"
    ),
    "Pea": (
        "https://images.pexels.com/photos/255469/pexels-photo-255469.jpeg?w=400",
        "https://images.pexels.com/photos/1667071/pexels-photo-1667071.jpeg?w=400"
    ),
    "Sunflower": (
        "https://images.pexels.com/photos/46216/sunflower-flowers-bright-yellow-46216.jpeg?w=400",
        "https://images.pexels.com/photos/33044/sunflower-sun-summer-yellow.jpg?w=400"
    ),
    "Strawberry": (
        "https://images.pexels.com/photos/70746/strawberries-red-fruit-royalty-free-70746.jpeg?w=400",
        "https://images.pexels.com/photos/934066/pexels-photo-934066.jpeg?w=400"
    ),
    "Mint": (
        "https://images.pexels.com/photos/2260118/pexels-photo-2260118.jpeg?w=400",
        "https://images.pexels.com/photos/1413643/pexels-photo-1413643.jpeg?w=400"
    ),
    "Basil": (
        "https://images.pexels.com/photos/4750274/pexels-photo-4750274.jpeg?w=400",
        "https://images.pexels.com/photos/568470/pexels-photo-568470.jpeg?w=400"
    ),
    "Watermelon": (
        "https://images.pexels.com/photos/1414110/pexels-photo-1414110.jpeg?w=400",
        "https://images.pexels.com/photos/2280545/pexels-photo-2280545.jpeg?w=400"
    ),
    "Mango": (
        "https://images.pexels.com/photos/918643/pexels-photo-918643.jpeg?w=400",
        "https://images.pexels.com/photos/2294471/pexels-photo-2294471.jpeg?w=400"
    ),
    "Banana": (
        "https://images.pexels.com/photos/1093038/pexels-photo-1093038.jpeg?w=400",
        "https://images.pexels.com/photos/2316466/pexels-photo-2316466.jpeg?w=400"
    ),
}

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

updated = 0
for name, (img1, img2) in plant_images.items():
    cursor.execute(
        "UPDATE plants SET plantImage1=?, plantImage2=? WHERE plantName=?",
        (img1, img2, name)
    )
    if cursor.rowcount:
        print(f"  + {name}")
        updated += 1

conn.commit()
conn.close()
print(f"\nDone: {updated} plants updated with Pexels image URLs.")
