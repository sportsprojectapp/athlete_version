import streamlit as st

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Athlete Dashboard", layout="wide", page_icon="🏃‍♂️")

# -------------------------------
# Language Dictionary (English + Hindi for now)
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
        # Sport names
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
    }
}

# -------------------------------
# Sidebar: Language + Dark Mode
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









