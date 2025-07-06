from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("API KEY:", api_key)

if not api_key:
    print("❌ API key is missing or not loaded correctly.")
else:
    genai.configure(api_key=api_key)
    try:
        models = genai.list_models()
        for m in models:
            print("✅ Available model:", m.name)
    except Exception as e:
        print("❌ Error fetching models:", e)
