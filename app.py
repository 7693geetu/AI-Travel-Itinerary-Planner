from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__)

# Mock function to simulate AI response
def generate_itinerary(user_input):
    return {
        "destination": user_input.get("destination", "Unknown"),
        "days": user_input.get("days", 3),
        "budget": user_input.get("budget", "Moderate"),
        "activities": ["Visit a museum", "Explore local food", "Sightseeing"],
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-itinerary', methods=['POST'])
def get_itinerary():
    user_input = request.json
    itinerary = generate_itinerary(user_input)
    return jsonify(itinerary)

#if __name__ == '__main__':
   # app.run(debug=True)

import streamlit as st
import openai

# Set up OpenAI API
openai_client = openai.OpenAI(api_key="your-api-key")

# Streamlit UI
st.title("AI Travel Planner ✈️")

# User Input
destination = st.text_input("Enter your travel destination:")
days = st.number_input("How many days?", min_value=1, max_value=30, value=3)

if st.button("Generate Itinerary"):
    if destination:
        # OpenAI API call
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Plan a {days}-day itinerary for {destination}"}]
        )
        
        itinerary = response.choices[0].message["content"]
        
        # Display the output
        st.subheader("Your AI-Generated Travel Plan:")
        st.write(itinerary)
    else:
        st.warning("Please enter a destination!")

