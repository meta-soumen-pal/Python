from together import Together
import os
from dotenv import load_dotenv


load_dotenv()


client = Together(api_key=os.getenv("LAMA_API_KEY"))

def lama_service(query):
    response = client.chat.completions.create(
        model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        messages=[{"role": "user", "content": f"{query} in markdown format"}]
    )
    
    return response.choices[0].message.content