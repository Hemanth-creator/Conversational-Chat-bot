import os
import replicate
# setting up the Api token in the local environment variables.
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

os.environ["REPLICATE_API_TOKEN"] = "r8_KT4eZI***********tU3USacPe1FuI8W"

def chat(query):
    char = ""
    output = replicate.run(
    "mistralai/mixtral-8x7b-instruct-v0.1",
    input={
        "debug": False,
        "top_k": 50,
        "top_p": 1,
        "prompt": query,
        "temperature": 0.7,
        "system_prompt": """You will be playing the role of a specified character. Your goal is to have natural conversations while staying true to that character's persona, background, and traits. 
Provide clear and concise guidance according to your profession. Style: Short, natural responses mimicking human conversation. Offer elaborations only when the User shows specific interest. Clarification is necessary for understanding. Always Omit greetings and self-introductions.""",
        "max_new_tokens": 1024,
        "min_new_tokens": -1
    }
)
    for item in output:
        char += item
        #print(item, end="")
    return char