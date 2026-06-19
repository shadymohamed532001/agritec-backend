from flask import request, jsonify
from dotenv import load_dotenv
import os
import requests
import base64
import uuid

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
IMAGEN_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "imagen-3.0-generate-002:predict"
)


def generate_product_image():
    '''Generate an image for a product using Gemini Imagen and save it to public/plants_photos1/'''
    try:
        if not GEMINI_API_KEY:
            return jsonify({
                "status": False,
                "message": "GEMINI_API_KEY is not configured.",
                "data": None
            }), 503

        name = request.form.get('name') or request.json.get('name') if request.is_json else request.form.get('name')
        description = request.form.get('description') or (request.json.get('description') if request.is_json else None)

        if not name:
            return jsonify({
                "status": False,
                "message": "Product name is required.",
                "data": None
            }), 400

        prompt = f"A high-quality product photo of {name}"
        if description:
            prompt += f": {description}"
        prompt += ". Clean white background, professional product photography."

        payload = {
            "instances": [{"prompt": prompt}],
            "parameters": {"sampleCount": 1}
        }

        response = requests.post(
            f"{IMAGEN_URL}?key={GEMINI_API_KEY}",
            json=payload,
            timeout=30
        )

        if response.status_code != 200:
            return jsonify({
                "status": False,
                "message": f"Image generation failed: {response.text}",
                "data": None
            }), response.status_code

        result = response.json()
        image_b64 = result["predictions"][0]["bytesBase64Encoded"]
        image_bytes = base64.b64decode(image_b64)

        save_folder = "public/plants_photos1"
        os.makedirs(save_folder, exist_ok=True)

        filename = f"{uuid.uuid4().hex}.png"
        file_path = os.path.join(save_folder, filename)
        with open(file_path, "wb") as f:
            f.write(image_bytes)

        image_url = f"/uploads/plants_photos1/{filename}"
        return jsonify({
            "status": True,
            "message": "Image generated successfully.",
            "data": {"imageUrl": image_url}
        }), 200

    except Exception as e:
        return jsonify({
            "status": False,
            "message": "Image generation failed.",
            "data": str(e)
        }), 500
