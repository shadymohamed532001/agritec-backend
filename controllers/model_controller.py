from flask import request, jsonify
from helpers.class_names import class_names
from helpers.is_plant import is_plant
from helpers.upload_images import upload_file
from helpers.disease_info import get_disease_information
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np

from models.products import get_products_by_tag


def get_plants_by_name(final_class):
    '''Return the bilingual (EN + AR) description and recommended treatment
    for the predicted disease/plant class.'''
    return get_disease_information(final_class)


def model_data(filename):
    model = tf.keras.models.load_model(
        './models/AI_Models/plant_model_v2.h5')
    img_path = 'public/plants/' + filename
    img = tf.keras.preprocessing.image.load_img(
        img_path, target_size=(256, 256))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    confidence = round(100*(np.max(prediction[0])), 2)
    final_class = class_names()[np.argmax(prediction)]
    return final_class, confidence


def get_products(final_class):
    '''Return a flat, de-duplicated list of treatment products whose tags
    contain the exact predicted class name.'''
    products = get_products_by_tag(final_class)
    if not products:
        return []
    seen = set()
    unique = []
    for p in products:
        if p["id"] not in seen:
            seen.add(p["id"])
            unique.append(p)
    return unique


def classify_image():
    '''Function to classify the input image'''
    try:
        if 'file' not in request.files:
            return jsonify({'message': 'No file part in the request'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'message': 'No file selected for uploading'}), 400
        plantPath = upload_file('file', 'plants')
        filename = secure_filename(file.filename)

        if (is_plant('public/plants/' + filename)):
            final_class, confidence = model_data(filename)
            all_products = get_products(final_class)
            information = get_plants_by_name(final_class)
            return jsonify(
                {
                    "status": True,
                    "message": "success",
                    "data":
                        {
                            'predictions': final_class,
                            "confidence": confidence,
                            "image": plantPath,
                            "products": all_products,
                            "information": information
                        }
                }), 200
        else:
            return jsonify({
                "status": False,
                'message': 'This is not a plant',
                'data': None
            }), 400
    except Exception as e:
        return jsonify({
            "status": False,
            "message": "Something went wrong",
            "data": e
        }), 500
