import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="EduLearn | Interactive Learning",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR ---
st.sidebar.title("🎓 EduLearn Menu")
menu = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📘 Lessons", "🧩 Quiz", "📊 Progress"]
)

# --- HEADER ---
st.markdown(
    """
    <style>
    .main-title {
        font-size: 40px;
        color: #2E86C1;
        font-weight: 700;
        text-align: center;
    }
    .subtitle {
        text-align: center;
        color: #555;
        font-size: 18px;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">EduLearn - Interactive Learning App 🎓</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your personal space for learning, testing, and tracking progress!</div>', unsafe_allow_html=True)

# --- HOME PAGE ---
if menu == "🏠 Home":
    st.subheader("👋 Welcome, Learner!")
    st.info("""
    EduLearn helps you:
    - 📖 **Study lessons** with easy explanations  
    - 🧩 **Test yourself** with quick interactive quizzes  
    - 📊 **Track your progress** over time  
    """)

    st.image(
        "https://cdn.pixabay.com/photo/2015/01/09/11/11/office-594132_1280.jpg",
        caption="Learn. Practice. Grow."
    )

# --- LESSONS PAGE ---
elif menu == "📘 Lessons":
    st.subheader("🧠 Lesson 1: Machine Learning Basics")
    st.markdown("""
    **What is Machine Learning (ML)?**  
    ML is a field of Artificial Intelligence that enables computers to **learn patterns from data** and make predictions or decisions without being explicitly programmed.

    **Main Types of Machine Learning:**
    - 🧭 **Supervised Learning:** Model learns using labeled data (e.g., Regression, Classification)
    - 🌌 **Unsupervised Learning:** Model identifies hidden patterns in unlabeled data (e.g., Clustering)
    - 🕹️ **Reinforcement Learning:** Model learns through reward and punishment (e.g., Game AI)
    """)

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/6/67/Artificial_intelligence_tree_structure.svg",
        caption="AI vs ML vs DL Overview"
    )

    st.info("💡 Tip: Machine Learning is about letting data guide decisions — not hardcoding logic!")

# --- QUIZ PAGE ---
elif menu == "🧩 Quiz":
    st.subheader("🧩 Quick Quiz: ML Basics")

    st.write("Answer the following questions and test your understanding:")

    q1 = st.radio("1️⃣ What does ML stand for?", ["Manual Learning", "Machine Learning", "Model Logic"])
    q2 = st.radio("2️⃣ Which of the following is supervised learning?", ["K-Means", "Linear Regression", "Apriori"])
    q3 = st.radio("3️⃣ What is used to train ML models?", ["Data", "Rules", "Code only"])

    if st.button("🚀 Submit Answers"):
        score = 0
        if q1 == "Machine Learning": score += 1
        if q2 == "Linear Regression": score += 1
        if q3 == "Data": score += 1

        st.success(f"✅ You scored **{score}/3**!")
        if score == 3:
            st.balloons()
            st.success("🎉 Excellent work! You're a future ML expert.")
        elif score == 2:
            st.info("👍 Good job! Review a bit more for a perfect score.")
        else:
            st.warning("😅 Keep studying! Review the lessons above.")

# --- PROGRESS PAGE ---
elif menu == "📊 Progress":
    st.subheader("📈 Your Learning Progress")

    # Simulated progress data
    progress_data = pd.DataFrame({
        "Topic": ["Intro to ML", "Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Deep Learning"],
        "Completion (%)": [90, 75, 60, 40, 20]
    })

    st.write("### Progress Overview")
    st.dataframe(progress_data)

    st.write("### Progress Chart")
    st.bar_chart(progress_data.set_index("Topic"))

    avg = np.mean(progress_data["Completion (%)"])
    st.info(f"🏅 **Overall Completion Rate:** {avg:.1f}%")

    if avg >= 80:
        st.success("Excellent progress! You're almost done! 🎯")
    elif avg >= 50:
        st.warning("You're halfway there — keep it up! 💪")
    else:
        st.error("You’ve just started. Stay consistent and you’ll improve fast! 🚀")
