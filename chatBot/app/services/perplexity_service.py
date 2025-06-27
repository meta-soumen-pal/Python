from together import Together
import os
from dotenv import load_dotenv


load_dotenv()


client = Together(api_key=os.getenv("PERPLEXITY_API_KEY"))


def perplexity_service(query):
    response = client.chat.completions.create(
        model="perplexity-ai/r1-1776",
        messages=[
        {
            "role": "user",
            "content": query
        }
        ]
    )
    return response.choices[0].message.content


