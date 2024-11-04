import requests

API_BASE_URL = "http://34.124.144.235:8081/api/v1"

def get_network_config(network_name):
    """Fetches network configuration from the API based on the network name."""
    url = f"{API_BASE_URL}/network/{network_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.HTTPError as err:
        raise Exception(f"HTTP error occurred: {err}")  # Handle HTTP errors
    except Exception as e:
        raise Exception(f"An error occurred: {e}")  # Handle other errors

def get_model_list():
    """Fetches the list of models from the API."""
    url = "http://34.142.156.174:7878/model/list"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"HTTP error occurred: {err}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

def launch_inference(data):
    """Launches an inference request to the API."""
    url = "http://34.142.156.174:7878/inference/launch"
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"HTTP error occurred: {err}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

def get_inference_output(request_id):
    """Fetches the output of a launched inference using the request ID."""
    url = "http://34.142.156.174:7878/inference/output"
    headers = {'Authorization': 'Bearer YOUR_BEARER_TOKEN'}  # Replace with actual token logic
    try:
        response = requests.post(url, headers=headers, json={"requestId": request_id})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"HTTP error occurred: {err}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

# Example usage:
# network_config = get_network_config("aizel")
# model_list = get_model_list()
# inference_response = launch_inference({"model_id": 1, "input": "data"})
# output_response = get_inference_output("request_id_here")
