import streamlit as st

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Athlete Dashboard", layout="wide", page_icon="🏃‍♂️")

# -------------------------------
# Language Dictionary
# -------------------------------
lang_dict = {
    "English": {
        "dashboard_title": "🏅 Athlete Dashboard",
        "profile_name": "Name",
        "profile_age": "Age",
        "profile_gender": "Gender",
        "profile_state": "State",
        "select_sport": "Your Sports",
        "latest_score": "Latest Score",
        "highest_score": "Highest Score",
        "attempts": "Attempts",
        "last_feedback": "Last Feedback / Problem",
        "record_rules": "Recording Rules",
        "record_upload_video": "Record Video",
        "motivation_test": "Motivation Test",
        "question1": "Do you feel motivated today?",
        "question2": "Are you confident in your sport?",
        "question3": "Do you enjoy training?",
        "yes": "😃 Yes",
        "maybe": "😐 Maybe",
        "no": "😞 No",
        "show_score": "Show Motivation Score",
        "motivated": "💪 You are motivated!",
        "keep_pushing": "Keep pushing! You can do it 💪",
        "answer_first": "Answer the questions first!",
        # Sport names
        "Sprinting":"Sprinting",
        "Long Jump":"Long Jump",
        "High Jump":"High Jump",
        "Shot Put":"Shot Put",
        "Discus Throw":"Discus Throw",
        "Javelin Throw":"Javelin Throw",
        "Hurdles":"Hurdles",
        "Relay Race":"Relay Race",
        "Pole Vault":"Pole Vault",
        "Marathon":"Marathon"
    },
    "Hindi": {
        "dashboard_title": "🏅 एथलीट डैशबोर्ड",
        "profile_name": "नाम",
        "profile_age": "आयु",
        "profile_gender": "लिंग",
        "profile_state": "राज्य",
        "select_sport": "आपके खेल",
        "latest_score": "नवीनतम स्कोर",
        "highest_score": "उच्चतम स्कोर",
        "attempts": "प्रयास",
        "last_feedback": "पिछली प्रतिक्रिया / समस्या",
        "record_rules": "रिकॉर्डिंग नियम",
        "record_upload_video": "वीडियो रिकॉर्ड करें",
        "motivation_test": "प्रेरणा परीक्षण",
        "question1": "क्या आप आज प्रेरित महसूस कर रहे हैं?",
        "question2": "क्या आप अपने खेल में आत्मविश्वासी हैं?",
        "question3": "क्या आपको प्रशिक्षण का आनंद आता है?",
        "yes": "😃 हाँ",
        "maybe": "😐 शायद",
        "no": "😞 नहीं",
        "show_score": "प्रेरणा स्कोर दिखाएँ",
        "motivated": "💪 आप प्रेरित हैं!",
        "keep_pushing": "लगातार प्रयास करें! आप कर सकते हैं 💪",
        "answer_first": "पहले प्रश्नों का उत्तर दें!",
        "Sprinting":"दौड़",
        "Long Jump":"लंबा कूद",
        "High Jump":"ऊंचा कूद",
        "Shot Put":"शॉट पुट",
        "Discus Throw":"डिस्कस थ्रो",
        "Javelin Throw":"भाला फेंक",
        "Hurdles":"हर्डल्स",
        "Relay Race":"रिले दौड़",
        "Pole Vault":"पोल वॉल्ट",
        "Marathon":"मैराथन"
    },
    # TODO: Add Marathi, Telugu, Tamil, Kannada, Malayalam, Tulu translations here
}

# -------------------------------
# Sidebar
# -------------------------------
selected_lang = st.sidebar.selectbox("Select Language / भाषा", list(lang_dict.keys()))
t = lang_dict[selected_lang]

dark_mode = st.sidebar.checkbox("Dark Mode", value=True)
bg_color = "#111111" if dark_mode else "#FFFFFF"
text_color = "#FFFFFF" if dark_mode else "#000000"

st.markdown(f"""
<style>
.stApp {{
    background-color: {bg_color};
    color: {text_color};
}}
.sport-banner {{
    border-radius: 20px;
    padding: 20px;
    margin: 15px 0;
    display: flex;
    align-items: center;
    color: white;
    font-size: 20px;
    height: 150px;
}}
.sport-image {{
    height: 130px;
    width: 130px;
    object-fit: cover;
    border-radius: 15px;
    margin-right: 15px;
}}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sample Athlete Data
# -------------------------------
sports_data = [
    {"sport": "Sprinting", "score": 88, "highest": 95, "attempts": 5,
     "last_feedback":"Knee posture needs improvement",
     "color": "#FF5733",
     "image":"https://i.ibb.co/2P4Z5yT/sprint.jpg",
     "rules":["Keep camera stable","Record full body","Wear proper shoes"]},
    {"sport": "Long Jump", "score": 82, "highest": 90, "attempts": 4,
     "last_feedback":"Landing posture incorrect",
     "color": "#33C1FF",
     "image":"https://i.ibb.co/Thm7T2T/longjump.jpg",
     "rules":["Ensure clear background","Record side view","Warm-up properly"]},
    {"sport": "High Jump", "score": 90, "highest": 95, "attempts": 6,
     "last_feedback":"Arms not straight during jump",
     "color": "#33FF57",
     "image":"https://i.ibb.co/fQ9R8Lx/highjump.jpg",
     "rules":["Full ju]()






