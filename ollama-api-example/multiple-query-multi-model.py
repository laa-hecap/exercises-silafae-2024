import requests
import json

def main():
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}

    # Read models and queries
    with open("models.txt", "r") as fm:
        models = [line.strip() for line in fm if line.strip()]

    with open("queries.txt", "r") as fq:
        queries = [line.strip() for line in fq if line.strip()]

    # For each model and query
    for model_name in models:
        for query in queries:
            data = {
                "model": model_name,
                "prompt": query,
                "stream": False
            }
            response = requests.post(url, headers=headers, data=json.dumps(data))
            if response.status_code == 200:
                result = json.loads(response.text)
                print(f"Model: {model_name}\nQuery: {query}\nAnswer: {result['response']}\n")
            else:
                print(f"Error with model {model_name}, query '{query}': {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()