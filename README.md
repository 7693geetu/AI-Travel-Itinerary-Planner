# AI Travel Itinerary Planner

## 🌍 Objective
Building an AI-powered travel planner that assists travelers in planning their trips and inquiries, ultimately generating a personalized travel itinerary.

## 🚀 Scenario
This project is designed to provide users with highly customized travel itineraries. The AI-powered system will simulate a conversation to gather user preferences, utilize web-search tools for relevant suggestions, and create a detailed travel plan. The application will be deployed on a free hosting platform like Streamlit or Gradio for user testing.

---

## 📌 Features
✔ **User Context Understanding**
   - Extract key details such as:
     - Budget
     - Trip duration & travel dates
     - Destination & starting location
     - Purpose of travel
     - User preferences (e.g., adventure, luxury, cultural experiences, etc.)
   - Chain prompts to refine unclear inputs and generate an organized day-by-day itinerary.

✔ **Intelligent Prompting System**
   - **Input Refinement:**
     - Collect additional preferences such as dietary needs, mobility concerns, accommodation type, etc.
   - **Activity Suggestions:**
     - Utilize web-search tools to generate accurate and up-to-date recommendations.
     - Align activity suggestions with user preferences (e.g., “Hidden Gems,” adventure spots, local cuisine, etc.).
   - **Itinerary Generation:**
     - Develop a well-structured n-day itinerary with logical groupings and time allocations.

✔ **User-Friendly Experience**
   - The AI system refines vague or incomplete inputs and asks for clarification.
   - Generates itinerary suggestions based on flexible input formats.

✔ **Live Deployment**
   - Hosted on **Streamlit/Gradio** for user testing and feedback.

---

## 🛠️ Technologies Used
- **Python** (Flask for backend logic)
- **HTML, CSS, JavaScript** (Frontend UI)
- **OpenAI API** (For AI-generated itinerary suggestions)
- **Web Search Tools** (To fetch live recommendations)
- **Streamlit/Gradio** (For free hosting & testing)
- **Git & GitHub** (For version control and collaboration)

---

## 📋 Implementation Steps
### Step 1: Understanding the User Context
- Extract user input details such as budget, trip duration, travel purpose, and preferences.
- Chain prompts effectively to refine unclear information.
- Structure a personalized itinerary based on user needs.

### Step 2: Building the Prompt System
- Develop prompts for gathering detailed preferences (e.g., dietary needs, accommodation types, etc.).
- Utilize web-search tools for real-time activity suggestions.
- Generate a well-structured and personalized itinerary.

### Step 3: Deliverables
- Submit final prompts used (System Prompt, User Prompt, and Model Response).
- Provide sample inputs and outputs, including curated suggestions and a structured itinerary.
- Document the approach taken for prompt engineering and logic building.
- Host the final application on **Streamlit/Gradio** and provide a testable link.

---

## 🎯 Bonus Challenge (Optional)
- Improve itinerary generation by allowing **flexible input formats** (e.g., “I want a mix of famous and offbeat places”).
- Handle vague or incomplete inputs effectively, prompting the user for clarity.

---

## 🏆 Evaluation Criteria
✔ **Prompt Design** – Are the prompts clear, specific, and structured?
✔ **Prompt Chaining** – Are multiple prompts strategically used to refine responses?
✔ **Personalization** – How well does the output align with the user’s preferences?
✔ **Documentation** – Is the reasoning and thought process explained effectively?

---

## 📌 How to Run the Project
### Clone the Repository
```sh
https://github.com/7693geetu/AI-Travel-Itinerary-Planner.git
cd AI-Travel-Itinerary-Planner
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Run the Application
```sh
python app.py
```

### Access the Deployed App (once hosted)
[Live Demo]("https://ai-travel-itinerary-planner-gvnnh5vakrzry9phs2b9kz.streamlit.app") *(Replace with hosted link)*

---

## ✨ Future Enhancements
🔹 Add support for **multi-user session handling**.
🔹 Integrate **Google Maps API** for location-based suggestions.
🔹 Allow users to **save and modify itineraries**.
🔹 Enable **multi-language support** for diverse users.

---

## 📢 Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📩 Contact
📧 **Geetanjali Dake** – [GitHub Profile](https://github.com/7693geetu)

---

🌍 **Plan your dream trip effortlessly with AI!** ✈️🎒🏝️

