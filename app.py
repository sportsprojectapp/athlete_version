import streamlit as st
import pandas as pd
from datetime import datetime
import random

# -------------------------------
# App Config
# -------------------------------
st.set_page_config(page_title="Athlete Dashboard", layout="wide", page_icon="🏃‍♂️")

# -------------------------------
# Multi-language dictionary
# -------------------------------
lang_dict = {
    "English": {
        "dashboard_title": "🏅 Athlete Dashboard",
        "profile_name": "Name",
        "profile_age": "Age",
        "profile_gender": "Gender",
        "profile_state": "State",
        "select_sport": "Select Your Sport",
        "latest_score": "Latest Score",
        "highest_score": "Highest Score",
        "attempts": "Attempts",
        "record_upload_video": "Record or Upload Video",
        "motivation_test": "Motivation Test",
        "question1": "Do you feel motivated today?",
        "question2": "Are you confident in your sport?",
        "question3": "Do you enjoy training?",
        "show_score": "Show Motivation Score",
        "motivated": "💪 You are motivated!",
        "keep_pushing": "Keep pushing! You can do it 💪",
        "answer_first": "Answer the questions first!"
    },
    "Malayalam": {
        "dashboard_title": "🏅 ആഥ്ലറ്റ് ഡാഷ്ബോർഡ്",
        "profile_name": "പേര്",
        "profile_age": "വയസ്",
        "profile_gender": "ലിംഗം",
        "profile_state": "സംസ്ഥാനം",
        "select_sport": "നിങ്ങളുടെ സ്പോർട്ട് തിരഞ്ഞെടുക്കുക",
        "latest_score": "അടുത്ത സ്‌കോർ",
        "highest_score": "മുകളിൽ സ്‌കോർ",
        "attempts": "പരീക്ഷണങ്ങൾ",
        "record_upload_video": "വീഡിയോ റെക്കോർഡ് ചെയ്യുക അല്ലെങ്കിൽ അപ്ലോഡ് ചെയ്യുക",
        "motivation_test": "പ്രചോദന പരീക്ഷ",
        "question1": "ഇന്ന് നിങ്ങൾ പ്രചോദനത്തോടെ അനുഭവപ്പെടുന്നുവോ?",
        "question2": "നിങ്ങളുടെ സ്പോർട്ടിൽ നിങ്ങൾ ആത്മവിശ്വാസമുള്ളവനാണോ?",
        "question3": "പരിശീലനം നിങ്ങൾക്ക് ഇഷ്ടമാണോ?",
        "show_score": "പ്രചോദന സ്കോർ കാണിക്കുക",
        "motivated": "💪 നിങ്ങൾ പ്രചോദിതനാണ്!",
        "keep_pushing": "തള്ളിപോവാതെ മുന്നോട്ട് പോവൂ! നിങ്ങൾക്ക് കഴിയും 💪",
        "answer_first": "ദയവായി ആദ്യം എല്ലാ ചോദ്യങ്ങൾക്കും ഉത്തരം നല്‍കുക!"
    },
    "Tamil": {
        "dashboard_title": "🏅 அணிமுறை விளையாட்டு டாஷ்போர்டு",
        "profile_name": "பெயர்",
        "profile_age": "வயது",
        "profile_gender": "பாலினம்",
        "profile_state": "மாநிலம்",
        "select_sport": "உங்கள் விளையாட்டை தேர்வு செய்யவும்",
        "latest_score": "சமீபத்திய மதிப்பெண்",
        "highest_score": "அதிகபட்ச மதிப்பெண்",
        "attempts": "முயற்சிகள்",
        "record_upload_video": "வீடியோ பதிவேற்றவும் அல்லது பதிவு செய்யவும்",
        "motivation_test": "மனப்பிம்முதல் சோதனை",
        "question1": "இன்று நீங்கள் உற்சாகமாக உள்ளீர்களா?",
        "question2": "உங்கள் விளையாட்டில் நீங்கள் நம்பிக்கை வைக்கிறீர்களா?",
        "question3": "பயிற்சி செய்ய விரும்புகிறீர்களா?",
        "show_score": "உற்சாக மதிப்பெண் காண்பி",
        "motivated": "💪 நீங்கள் உற்சாகமாக இருக்கிறீர்கள்!",
        "keep_pushing": "தள்ளாமே! நீங்கள் இதைச் செய்ய முடியும் 💪",
        "answer_first": "முதலில் கேள்விகளுக்கு பதிலளிக்கவும்!"
    },
    "Telugu": {
        "dashboard_title": "🏅 క్రీడాకారుడి డ్యాష్‌బోర్డ్",
        "profile_name": "పేరు",
        "profile_age": "వయసు",
        "profile_gender": "లింగం",
        "profile_state": "రాజ్యం",
        "select_sport": "మీ క్రీడను ఎంచుకోండి",
        "latest_score": "తాజా స్కోరు",
        "highest_score": "అధిక స్కోరు",
        "attempts": "ప్రయత్నాలు",
        "record_upload_video": "వీడియో రికార్డ్ చేయండి లేదా అప్‌లోడ్ చేయండి",
        "motivation_test": "మోటివేషన్ టెస్ట్",
        "question1": "మీరు ఈ రోజు ప్రేరణ పొందారా?",
        "question2": "మీ క్రీడలో మీరు ధైర్యంగా ఉన్నారా?",
        "question3": "ప్రశిక్షణ చేయడం మీకు ఇష్టం?",
        "show_score": "మోటివేషన్ స్కోరు చూపించు",
        "motivated": "💪 మీరు ప్రేరణ పొందారు!",
        "keep_pushing": "తగ్గకుండా కొనసాగించండి! మీరు చేయగలరు 💪",
        "answer_first": "ముందుగా ప్రశ్నలకు సమాధానం ఇవ్వండి!"
    }
}

# -------------------------------
# Sidebar: Language & Theme
# -------------------------------
selected_lang = st.sidebar.selectbox("Select Language", list(lang_dict.keys()))
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
    .stButton>button {{
        color: {text_color};
    }}
    .banner {{
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0px;
        background-color: #FFD580;
    }}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sample Athlete Data
# -------------------------------
sports_data = [
    {"sport": "Sprinting", "score": 88, "highest": 95, "attempts": 5, "video_url": ""},
    {"sport": "Long Jump", "score": 82, "highest": 90, "attempts": 4, "video_url": ""},
    {"sport": "High Jump", "score": 90, "highest": 95, "attempts": 6, "video_url": ""},
    {"sport": "Swimming", "score": 75, "highest": 80, "attempts": 3, "video_url": ""},
    {"sport": "Cycling", "score": 65, "highest": 70, "attempts": 2, "video_url": ""},
]

# -------------------------------
# Athlete Profile
# -------------------------------
st.markdown(f"<h1 style='color:{text_color}'>{t['dashboard_title']}</h1>", unsafe_allow_html=True)

profile_col1, profile_col2 = st.columns([1, 3])
with profile_col1:
    st.image("https://randomuser.me/api/portraits/men/1.jpg", width=120)
with profile_col2:
    st.markdown(f"**{t['profile_name']}:** Athlete 1")
    st.markdown(f"**{t['profile_age']}:** 20")
    st.markdown(f"**{t['profile_gender']}:** Male")
    st.markdown(f"**{t['profile_state']}:** Kerala")

st.markdown("---")

# -------------------------------
# Sport Banners
# -------------------------------
st.subheader(t['select_sport'])

for sport in sports_data:
    with st.expander(f"{sport['sport']} 🏆"):
        st.image("https://via.placeholder.com/150", width=150)
        st.markdown(f"**{t['latest_score']}:** {sport['score']}")
        st.markdown(f"**{t['highest_score']}:** {sport['highest']}")
        st.markdown(f"**{t['attempts']}:** {sport['attempts']}")
        uploaded_video = st.file_uploader(t['record_upload_video'], type=["mp4"], key=sport['sport'])
        if uploaded_video:
            st.video(uploaded_video)

st.markdown("---")

# -------------------------------
# Motivation Test
# -------------------------------
st.subheader(t['motivation_test'])

questions = [t['question1'], t['question2'], t['question3']]
responses = []

for idx, q in enumerate(questions):
    st.markdown(f"**{q}**")
    col1, col2, col3 = st.columns(3)
    if col1.button("😃 Yes", key=f"{idx}-yes"):
        responses.append(1)
    if col2.button("😐 Maybe", key=f"{idx}-maybe"):
        responses.append(0)
    if col3.button("😞 No", key=f"{idx}-no"):
        responses.append(-1)

if st.button(t['show_score']):
    if responses:
        score = sum(responses)
        if score > 0:
            st.success(t['motivated'])
        else:
            st.info(t['keep_pushing'])
    else:
        st.warning(t['answer_first'])

