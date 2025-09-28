import streamlit as st

# -------------------------------
# App Config
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
    },
    # Add other languages similarly (Marathi, Telugu, Tamil, Kannada, Malayalam, Tulu)
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
        justify-content: space-between;
        color: white;
        font-size: 18px;
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
     "rules":["Full jump visible","Good lighting","Use tripod if possible"]},
    {"sport": "Shot Put", "score": 70, "highest": 85, "attempts": 3,
     "last_feedback":"Incorrect release angle",
     "color": "#FF33A8",
     "image":"https://i.ibb.co/1L1gFz3/shotput.jpg",
     "rules":["Full motion visible","Good lighting","Use proper stance"]},
    {"sport": "Discus Throw", "score": 75, "highest": 88, "attempts": 4,
     "last_feedback":"Foot placement needs adjustment",
     "color": "#FFA833",
     "image":"https://i.ibb.co/gPCXWP0/discus.jpg",
     "rules":["Record full rotation","Stable camera","Wear shoes"]},
    {"sport": "Javelin Throw", "score": 80, "highest": 92, "attempts": 5,
     "last_feedback":"Over-rotation detected",
     "color": "#33FFA5",
     "image":"https://i.ibb.co/2FqY3j3/javelin.jpg",
     "rules":["Clear background","Record full throw","Good lighting"]},
    {"sport": "Hurdles", "score": 85, "highest": 95, "attempts": 6,
     "last_feedback":"Incorrect hurdle clearance",
     "color": "#8D33FF",
     "image":"https://i.ibb.co/7KfLvZQ/hurdles.jpg",
     "rules":["Full hurdle visible","Good camera angle","Use markers"]},
    {"sport": "Relay Race", "score": 78, "highest": 88, "attempts": 4,
     "last_feedback":"Baton exchange slow",
     "color": "#FF3333",
     "image":"https://i.ibb.co/2qv6ZL3/relay.jpg",
     "rules":["Full team visible","Clear start/end","Stable camera"]},
    {"sport": "Pole Vault", "score": 82, "highest": 90, "attempts": 3,
     "last_feedback":"Pole placement wrong",
     "color": "#33FFC5",
     "image":"https://i.ibb.co/0sF0TnG/polevault.jpg",
     "rules":["Full vault visible","Good lighting","Clear background"]},
    {"sport": "Marathon", "score": 95, "highest": 98, "attempts": 2,
     "last_feedback":"Pacing inconsistent",
     "color": "#FFBD33",
     "image":"https://i.ibb.co/HXkHV4r/marathon.jpg",
     "rules":["Full run visible","Wear bib number","Stable camera"]},
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
# Display Sport Banners (expandable)
# -------------------------------
st.subheader(t['select_sport'])
for sport in sports_data:
    sport_name_lang = t.get(sport["sport"], sport["sport"])  # Translate sport name
    with st.expander(f"{sport_name_lang} 🏆"):
        # Banner
        banner_html = f"""
        <div class="sport-banner" style="background-color:{sport['color']};">
            <img src="{sport['image']}" class="sport-image">
            <div>
                <b>{sport_name_lang}</b><br>
                {t['latest_score']}: {sport['score']} | {t['highest_score']}: {sport['highest']} | {t['attempts']}: {sport['attempts']}<br>
                {t['last_feedback']}: {sport['last_feedback']}
            </div>
        </div>
        """
        st.markdown(banner_html, unsafe_allow_html=True)
        # Recording rules
        st.markdown(f"**{t['record_rules']}:**")
        for rule in sport['rules']:
            st.markdown(f"- {rule}")
        # Camera-only recording
        recorded_video = st.camera_input(t['record_upload_video'], key=sport['sport'])
        if recorded_video:
            st.video(recorded_video)

# -------------------------------
# Motivation Test
# -------------------------------
st.markdown("---")
st.subheader(t['motivation_test'])
questions = [t['question1'], t['question2'], t['question3']]
responses = []

for idx, q in enumerate(questions):
    st.markdown(f"**{q}**")
    col1, col2, col3 = st.columns(3)





