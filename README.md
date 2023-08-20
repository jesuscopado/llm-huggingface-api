# Language Detection and Named Entity Recognition API

A simple REST API that can detect the language of a given text and identify named entities in a given text, using the Bloom (BigScience) Large Language Model (LLM) from Hugging Face.

## Setup and Run Application

### Prerequisites

- Docker
- Docker-compose
- Min. 8GB RAM allocated to Docker

### Steps to Run

1. Clone this repository:
```bash
git clone https://github.com/jesuscopado/llm-huggingface-api.git
cd llm-huggingface-api
```

2. Build and run the Docker container:

```bash
docker-compose up
```

The API will be available at http://localhost:5001

## Reasoning for Choice of LLM

For this application, the [bigscience/bloomz-3b model](https://huggingface.co/bigscience/bloomz-3b) from the BLOOMZ family was chosen for several reasons:

1. Multilingual Capabilities: The BLOOMZ family of models has been specifically fine-tuned for multilingual tasks. The language detection task and named entity recognition tasks require a model with comprehensive understanding of multiple languages, making BLOOMZ an excellent fit.
2. Instruction Following Ability: BLOOMZ models are designed to follow human instructions expressed in natural language. This is key for the API as it is structured around processing and responding to human-like prompts.
3. Crosslingual Generalization: The fine-tuning process for BLOOMZ involved a crosslingual task mixture, which has resulted in models that are capable of generalizing to unseen tasks and languages. This is valuable for the API as it ensures robust and versatile performance.
4. Pre-trained on Diverse Data: BLOOMZ is built upon pretrained multilingual language models. These underlying models have been trained on a wide variety of text data, providing them with a strong foundational understanding of language.
5. Balance of Size and Performance: With approximately 3 billion parameters, the `bigscience/bloomz-3b` model strikes a good balance between computational efficiency and prediction accuracy. It is large enough to understand complex contexts, yet small enough to be deployed easily in a practical, real-world setting.

## Strategies for Improving API Functionality

- Investigate Language-Specific Models: For the task of Named Entity Recognition, consider evaluating and deploying language-specific models that may yield better performance for certain languages than a multilingual model.
- Implement Caching Mechanism: Utilize a caching strategy, like Redis, to store recent queries and their responses. This reduces redundant processing for frequently requested data.
- Optimize Model Loading and Inference Time: Explore further quantization and optimization techniques to reduce model size without significantly compromising accuracy. This would lead to faster start-up times and lower memory usage.
- Add Security and Rate Limiting: Apply API keys, OAuth, or another authentication system to secure endpoints. Implement rate limits to prevent abuse and ensure fair usage.
- Load Balancing and Scalability: Introduce a load balancer, like Nginx, to distribute incoming traffic across multiple instances of the application. This ensures high availability and resilience under heavy loads, facilitating smooth horizontal scaling as demand grows.

## Evaluating the Application

- Comprehensive Test Dataset: Craft a diverse dataset with various languages, entity types, and linguistic complexities. Ensure inclusion of edge cases and ground truth labels for rigorous testing.
- Larger Model for Validation: Employ a more capable, larger language model as a "golden" reference. Compare the API output against this standard to assess relative performance.
- Automated Testing & Continuous Integration: Establish an automated testing pipeline that triggers unit, integration, and end-to-end tests upon every code change, using the comprehensive test dataset.
- Performance Metrics: Define key metrics such as precision, recall, F1 score for named entity recognition, and language detection accuracy. Monitor latency, throughput, and resource utilization to evaluate efficiency.

## API Endpoints

### Detect Language

- POST /detect_language
- Request Body: {"text": "your text here"}

### Named Entity Recognition

- POST /named_entities
- Request Body: {"text": "your text here"}

## Example Usage

Request:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text":"Hello, how are you?"}' http://localhost:5001/detect_language
```

Response:

```bash
{"language": "en"}
```