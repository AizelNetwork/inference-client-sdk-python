import requests

class InferenceClient:
    def __init__(self, base_url, app_key):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {app_key}",
            "Content-Type": "application/json"
        }

    def launch_inference(self, model_id, user_input, system_prompt=None, temperature=0.5, max_tokens=150, network_name="aizel"):
        url = f"{self.base_url}/inference/launch"
        payload = {
            "model_id": model_id,
            "user_input": user_input,
            "system_prompt": system_prompt,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "network_name": network_name
        }
        response = requests.post(url, json=payload, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()  # Assuming the API returns JSON
        else:
            response.raise_for_status()

    def get_model_list(self):
        url = f"{self.base_url}/model/list"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_inference_list(self):
        url = f"{self.base_url}/inference/list"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_inference_output(self, request_id):
        url = f"{self.base_url}/inferences/output"
        payload = {
            "requestId": request_id
        }
        response = requests.post(url, json=payload, headers=self.headers)

        if response.status_code == 200:
            return response.json()  # Assuming the API returns JSON
        else:
            response.raise_for_status()
