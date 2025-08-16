import functions_framework
import logging
import json
import base64

logging.basicConfig(level=logging.INFO)

@functions_framework.cloud_event
def hello_pubsub(cloud_event):
    """
    Logs the Pub/Sub message.
    """
    
    # Log the entire cloud event data
    logging.info(f"Cloud Event: {cloud_event.data}")
    
    # Decode and log the message data
    try:
        message_data = base64.b64decode(cloud_event.data['message']['data']).decode('utf-8')
        logging.info(f"Pub/Sub Message: {message_data}")
    except Exception as e:
        logging.error(f"Error processing Pub/Sub message: {e}")

@functions_framework.http
def hello_http(request):
    """
    Logs the request body and headers.
    """
    
    # Log request headers
    logging.info(f"Request Headers: {json.dumps(dict(request.headers), indent=2)}")
    
    # Log request body
    try:
        request_json = request.get_json(silent=True)
        if request_json:
            logging.info(f"Request Body: {json.dumps(request_json, indent=2)}")
        else:
            logging.info("Request body is not JSON or is empty.")
    except Exception as e:
        logging.error(f"Error processing request body: {e}")

    return "Hello, World!"
