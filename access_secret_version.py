import os
from google.cloud import secretmanager
import logging

def access_secret_version(secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{os.getenv('GOOGLE_PROJECT_ID')}/secrets/{secret_id}/versions/latest"
    try:
        response = client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")
    except Exception as e:
        logging.error(f"Failed to access secret {secret_id}: {e}")
        return None

OAUTH_CLIENT_ID = os.getenv('OAUTH_CLIENT_ID')
OAUTH_CLIENT_SECRET = os.getenv('OAUTH_CLIENT_SECRET')

if not OAUTH_CLIENT_ID or not OAUTH_CLIENT_SECRET:
    raise EnvironmentError("OAuth credentials are not set.")
