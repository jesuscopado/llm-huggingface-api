from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline

app = Flask(__name__)

model_name = "bigscience/bloomz-3b"
print(f"Loading {model_name} model from HuggingFace...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
quantization_config = BitsAndBytesConfig(llm_int8_enable_fp32_cpu_offload=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    load_in_8bit=True,
    quantization_config=quantization_config,
    temperature=0,
)
generator = pipeline(
    task="text-generation",
    model=model,
    tokenizer=tokenizer,
)


def detect_language(text: str) -> str:
    """Detect the language of a given text.

    Args:
        text (str): Input text whose language needs to be detected.

    Returns:
        str: Detected language in BCP-47 language code.
    """

    prompt = f'''Detect the language of a sentence in BCP-47 language code.

    Sentence: Hello, how are you?
    Language: en

    Sentence: Hola, ¿cómo estás?
    Language: es

    Sentence: Das ist sehr interessant.
    Language: de

    Sentence: Je suis ravi de vous rencontrer.
    Language: fr

    Sentence: Questo è un esempio di frase in italiano.
    Language: it

    Sentence: {text}
    Language:'''

    generated_text = generator(prompt, max_new_tokens=1)[0]['generated_text']
    return generated_text.split()[-1]


def named_entities(text: str) -> list:
    """Extract named entities and count their occurrences from a given text.

    Args:
        text (str): Input text from which named entities are to be extracted.

    Returns:
        list: Named entities and their occurrence count.
    """

    prompt = f'''Extract named entities and count their occurrences from the corresponding texts below.

    Text: Barack Obama was born in Hawaii.
    Named Entities: Barack Obama (1), Hawaii (1)

    Text: Apple Inc. is based in Cupertino, California. Apple Inc. is a technology company.
    Named Entities: Apple Inc. (2), Cupertino (1), California (1)

    Text: The Eiffel Tower is in Paris. Paris is the capital of France.
    Named Entities: Eiffel Tower (1), Paris (2), France (1)

    Text: {text}
    Named Entities:'''

    generated_text = generator(
        prompt,
        max_new_tokens=100,
        early_stopping=True,
    )[0]['generated_text']
    return generated_text.split('Named Entities: ')[-1].split(', ')


@app.route('/detect_language', methods=['POST'])
def detect_language_endpoint():
    """Flask endpoint to detect language of the input text."""
    text = request.json['text']
    language = detect_language(text)
    return jsonify({'language': language})


@app.route('/named_entities', methods=['POST'])
def named_entities_endpoint():
    """Flask endpoint to extract named entities from the input text."""
    text = request.json['text']
    entities = named_entities(text)
    return jsonify({'entities': entities})


if __name__ == '__main__':
    app.run(debug=True)
