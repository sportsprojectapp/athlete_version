import streamlit as st

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
        "answer_first": "Answer the questions first!"
    },
    # Add Malayalam/Tamil/Telugu similarly with translated keys...
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
    .sport-banner {{
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: white;
        font-size: 18px;
    }}
    .sport-image {{
        height: 120px;
        width: 120px;
        object-fit: cover;
        border-radius: 10px;
        margin-right: 15px;
    }}
    .rules-box {{
        background-color: rgba(0,0,0,0.2);
        padding: 10px;
        border-radius: 10px;
        margin-top: 10px;
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
     "image":"https://via.placeholder.com/120?text=Sprint",
     "rules":["Keep camera stable","Record full body","Wear proper shoes"]},
     
    {"sport": "Long Jump", "score": 82, "highest": 90, "attempts": 4,
     "last_feedback":"Landing posture incorrect",
     "color": "#33C1FF",
     "image":"https://via.placeholder.com/120?text=Jump",
     "rules":["Ensure clear background","Record side view","Warm-up properly"]},
     
    {"sport": "High Jump", "score": 90, "highest": 95, "attempts": 6,
     "last_feedback":"Arms not straight during jump",
     "color": "#33FF57",
     "image":"https://via.placeholder.com/120?text=HighJump",
     "rules":["Full jump visible","Good lighting","Use tripod if possible"]},
]

# -------------------------------
# Profile Section
# -------------------------------
st.markdown(f"<h1 style='color:{text_color}'>{t['dashboard_title']}</h1>", unsafe_allow_html=True)
profile_col1, profile_col2 = st.columns([1,3])
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
for sport in s


