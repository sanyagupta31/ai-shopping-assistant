AI Shopping Assistant

This is an AI-powered shopping assistant built using Streamlit and Gemini Pro by Google.

You can type what you're looking for (like "mujhe pink frock chahiye") and get smart product search links from platforms like Amazon, Flipkart, Myntra, AJIO, Nykaa, and Meesho.



Features

- AI understands shopping requests in casual or Hindi-style language
- Gives links from Amazon, Flipkart, Myntra, AJIO, Nykaa, and Meesho
- Optionally supports product preview images (Amazon & Flipkart)
- Lightweight and fast interface using Streamlit

Demo

[Streamlit Cloud](https://sanyagupta31-ai-shopping-assistant-app-4i6so9.streamlit.app/)

Tech Stack

- Streamlit
- Gemini API (Google Generative AI)
- Python
- dotenv for key management

Setup Instructions

1. Clone this project

   git clone https://github.com/sanyagupta31/ai-shopping-assistant
   cd ai-shopping-assistant

2. Create a .env file and add your Gemini API key

   GEMINI_API_KEY=your_api_key_here

3. Install dependencies

   pip install -r requirements.txt

4. Run the app

   streamlit run app.py

Project Structure

app.py              → Main Streamlit app  
.env                → Your API key (do not upload this)  
requirements.txt    → Python dependencies  
.gitignore          → Files/folders to exclude from GitHub  
README.md           → Project documentation

Example Prompts You Can Try

- mujhe pink frock chahiye  
- white crop top  
- college bag under 1000  
- blue hoodie for winter  
- bridal lehenga

Author

Made by Sanya Gupta  


