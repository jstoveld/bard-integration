import httpx
import json
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file
load_dotenv()

# Define your Google Cloud API key
API_KEY = os.getenv("API_KEY")

# Define Bard API endpoint for question answering
ENDPOINT_URL = "https://us-central1-language.googleapis.com/v1/projects/bard-project/locations/global/inference:answer"

# Function to generate a question and send it to Bard API
async def ask_bard_question(question):
    # ... rest of your function ...
    """
    Sends a question to Bard API and returns the response.

    Args:
        question (str): The question to be asked.

    Returns:
        dict: The response dictionary containing answer and confidence score.
    """

    # Prepare the request body
    request_body = json.dumps({"query": question, "model": "bard"})

    # Set headers with API key
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    # Send the POST request to Bard API
    async with httpx.AsyncClient() as client:
        response = await client.post(ENDPOINT_URL, headers=headers, data=request_body)

    # Check for successful response
    if response.status_code == 200:
        # Parse the JSON response and return answer information
        response_data = json.loads(response.content)
        return {
        "answer": response_data["answer"]["text"],
        "confidence_score": response_data["answer"]["confidenceScore"],
        }
    else:
        raise Exception(f"Error sending request to Bard API: {response.text}")

# Example usage
user_question = "What is the capital of France?"

async def main():
    answer_data = await ask_bard_question(user_question)
    print(f"Question: {user_question}")
    print(f"Answer: {answer_data['answer']}")
    print(f"Confidence Score: {answer_data['confidence_score']}")

# Run the main function
asyncio.run(main())
