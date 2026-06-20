import requests
import os
from dotenv import load_dotenv

load_dotenv()


def is_plant(photo):
    '''Function to check if the image is a plant or not.

    Uses the PlantNet API as a pre-filter. This check is best-effort:
    if no API key is configured, or the API call fails for any reason,
    we "fail open" (return True) so the local classification model still
    runs. Without this, a missing/expired key would cause every image to
    be rejected as "This is not a plant".
    '''
    api_key = os.getenv('PLANT_API_KEY')

    # No key configured -> skip the external check and let the model run.
    if not api_key:
        print("[is_plant] PLANT_API_KEY not set; skipping PlantNet check.")
        return True

    try:
        url = (
            "https://my-api.plantnet.org/v2/identify/all"
            "?include-related-images=false&no-reject=true&lang=en"
            f"&api-key={api_key}"
        )

        with open(photo, 'rb') as f:
            files = [('images', ('file', f, 'image/png'))]
            response = requests.post(url, files=files, data={}, timeout=15)

        return response.status_code == 200
    except Exception as e:
        # On any network/API error, don't block the user's request.
        print(f"[is_plant] PlantNet check failed ({e}); allowing image.")
        return True
