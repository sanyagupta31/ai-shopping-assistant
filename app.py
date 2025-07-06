import streamlit as st
from google.generativeai import GenerativeModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash-latest")

st.set_page_config("🛍️ Fashion Chatbot")
st.title("🛍️ AI Shopping Assistant")

platform = st.selectbox("Choose a shopping platform:", ["Amazon", "Flipkart", "Myntra", "AJIO", "Nykaa", "Meesho"])

user_input = st.text_input("What are you looking for today?")

if user_input:
    with st.spinner("Finding the best options..."):
        # Generate clean search query
        response = model.generate_content(
            f"Convert this into a short search query for shopping sites (no quotes, no explanation): '{user_input}'"
        )
        search_query = response.text.strip().replace('"', '')

        # Platform URLs
        urls = {
            "Amazon": f"https://www.amazon.in/s?k={search_query.replace(' ', '+')}",
            "Flipkart": f"https://www.flipkart.com/search?q={search_query.replace(' ', '%20')}",
            "Myntra": f"https://www.myntra.com/{search_query.replace(' ', '%20')}",
            "AJIO": f"https://www.ajio.com/search/?text={search_query.replace(' ', '%20')}",
            "Nykaa": f"https://www.nykaa.com/search/result/?q={search_query.replace(' ', '%20')}",
            "Meesho": f"https://www.meesho.com/search?q={search_query.replace(' ', '%20')}",
        }

        st.success("Here’s your search result!")
        st.markdown(f"🔗 [See on {platform}]({urls[platform]})")

        
        
        st.write("Happy shopping! 🛒")