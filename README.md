# Inference Client SDK for Python

The Inference Client SDK provides a convenient way to interact with the inference services of our application. This SDK allows developers to launch inferences, retrieve outputs, and manage network configurations seamlessly.

## Features

- **Launch Inference**: Easily start an inference process using various model configurations.
- **Get Inference Output**: Retrieve the output of the launched inferences.
- **Network Configuration**: Fetch network details and deployed contract addresses dynamically.

## Installation

You can install the SDK via pip. Run the following command in your terminal:

```bash
pip install git+https://github.com/yourusername/inference-client-sdk-python.git
```

Or clone the repository and install it locally:

```bash
git clone https://github.com/yourusername/inference-client-sdk-python.git
cd inference-client-sdk-python
pip install -r requirements.txt
```

## Usage

### Initialize the Inference Client

To start using the SDK, first initialize the `InferenceClient` with your Bearer token.

```python
from lib.InferenceClient import InferenceClient

# Initialize the client with the Bearer token
client = InferenceClient(app_key='YOUR_BEARER_TOKEN')
```

### Launch an Inference

You can launch an inference by providing the necessary parameters:

```python
response = client.launch_inference(
    model_id=1,
    user_input="Your input here",
    system_prompt="System prompt here",
    temperature=0.7,
    max_tokens=150,
    network_name="aizel"
)

print("Inference Request ID:", response['requestId'])
```

### Get Inference Output

To retrieve the output of a launched inference, use the following method:

```python
output_response = client.get_output(request_id="YOUR_REQUEST_ID")
print("Inference Output:", output_response)
```

## API Endpoints

The SDK interacts with the following API endpoints:

- **Model List**: `http://34.142.156.174:7878/model/list`
- **Launch Inference**: `http://34.142.156.174:7878/inference/launch`
- **Get Inference Output**: `http://34.124.144.235:8080/api/v1/inferences/output`

## Development

To contribute to the SDK, clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/inference-client-sdk-python.git
cd inference-client-sdk-python
pip install -r requirements.txt
```

Run the tests to ensure everything works correctly:

```bash
python -m unittest discover lib/test
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any inquiries or support, please reach out to [your-email@example.com].
```
