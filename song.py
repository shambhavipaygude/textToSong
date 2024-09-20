import random
from transformers import pipeline
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('GEMINI_KEY')

def generate_lyrics(input_text):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Create a rap verse that incorporates the keywords. The lyrics should have a strong rhythm and flow, using internal rhymes and a consistent rhyme scheme. Make sure all the keywords are used naturally in the lyrics. The keywords are : "+input_text)
    print(response.text)
    return response.text

def main():
    input_text = "Hydrogen, Helium, Lithium, Beryllium, Carbon"
    generated_lyrics = generate_lyrics(input_text)

if __name__ == "__main__":
    main()
