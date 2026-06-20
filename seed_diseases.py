# -*- coding: utf-8 -*-
'''
Seed the `products` table with real treatment products for every plant disease
the model can predict.

Each product is owned by a dedicated store account and tagged with the EXACT
disease class names it treats, so the existing tag-based lookup
(`get_products_by_tag`) returns the right medicines for a prediction.

Run from the BackEnd directory:  python seed_diseases.py
The script is idempotent: it removes the store's old treatment products and
re-inserts them on every run.
'''
import sqlite3
import bcrypt

from helpers.disease_info import TREATMENT_PRODUCTS

DB = "database.db"
STORE_EMAIL = "store@agritech360.com"
STORE_NAME = "Agri-Tech 360 Store"
STORE_PIC = "https://cdn-icons-png.freepik.com/512/3033/3033143.png"


def ensure_store_user(cur):
    '''Create the store seller account if it does not already exist.'''
    cur.execute("SELECT email FROM users WHERE email=?", (STORE_EMAIL,))
    if cur.fetchone():
        return
    hashed = bcrypt.hashpw("Store#12345".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    cur.execute(
        "INSERT INTO users (fullName, email, password, city, phoneNumber, profilePic) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (STORE_NAME, STORE_EMAIL, hashed, "Cairo", "0100000000", STORE_PIC),
    )
    print(f"Created store seller account: {STORE_EMAIL}")


def seed_products():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    ensure_store_user(cur)

    # Idempotent: clear this store's existing treatment products.
    cur.execute("DELETE FROM products WHERE seller=?", (STORE_EMAIL,))
    print(f"Removed {cur.rowcount} old treatment product(s).")

    inserted = 0
    for p in TREATMENT_PRODUCTS:
        name = f"{p['name_en']} | {p['name_ar']}"
        description = f"{p['desc_en']}\n\n{p['desc_ar']}"
        tags = ",".join(p["tags"])              # exact class names, comma separated
        image = p["image"]
        images = f"['{image}']"
        cur.execute(
            "INSERT INTO products (name, price, description, seller, image, images, tags) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (name, p["price"], description, STORE_EMAIL, image, images, tags),
        )
        inserted += 1

    conn.commit()
    conn.close()
    print(f"Inserted {inserted} treatment product(s) for {STORE_EMAIL}.")


if __name__ == "__main__":
    seed_products()
