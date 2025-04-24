import openai
import os
import random
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load prompts
with open("prompts.json", "r") as file:
    prompts = json.load(file)

# Pick random input prompts
city_question = random.choice(prompts["city_questions"])
pet_question = random.choice(prompts["pet_questions"])

# Get user input
print("Welcome to the AI-Powered Band Name Generator!\n")
city = input(city_question + "\n")
pet = input(pet_question + "\n")

# Format the AI prompt
prompt_template = prompts["ai_prompt_template"]
ai_prompt = prompt_template.format(city=city, pet=pet)

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": ai_prompt}
    ]
)

band_name = response.choices[0].message.content.strip()

print(f"\nYour AI-generated band name is:\n{band_name}")
