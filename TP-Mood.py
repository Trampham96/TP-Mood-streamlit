import streamlit as st
import random

# Tạo tiêu đề cho ứng dụng
st.title("🌞 How is Your Day! 🌟")

# Tạo các tùy chọn cảm xúc
mood = st.radio(
    "Choose your mood:",
    ("Happy", "Sad", "Terrible", "Neutral")
)

# Danh sách các câu quote cho mỗi cảm xúc
quotes = {
    "Happy": [
        "Enjoy your happiness, because joy is a treasure of life!",
        "Smile big and make your day full of joy! 😊",
        "Happiness is not in what you own, but in how you live."
    ],
    "Sad": [
        "Everything will be okay. Stay strong! 🌈",
        "Even if today is sad, remember tomorrow is a new day.",
        "Tears cleanse the soul, cry and then be strong again!"
    ],
    "Terrible": [
        "A terrible day is just a small part of your life's story.",
        "When things get tough, remember you've overcome so much already.",
        "The bad moments may pass, but your strength will remain."
    ],
    "Neutral": [
        "Being neutral is a good state for rest and recovery.",
        "Life is not always extraordinary; sometimes, being normal is great.",
        "Embrace the peace in an uneventful day."
    ]
}

# Hiển thị câu quote phù hợp khi người dùng chọn cảm xúc
if st.button("Show me a quote"):
    selected_quote = random.choice(quotes[mood])
    st.write(f"**Quote for you:** {selected_quote}")
    
    # Tạo hiệu ứng mặt cười chạy lên
    st.markdown(
        """
        <style>
        .emoji {
            font-size: 50px;
            animation: moveUp 4s linear infinite;
            position: fixed;
            bottom: -100px;
            left: 50%;
            transform: translateX(-50%);
        }

        @keyframes moveUp {
            0% {
                bottom: -100px;
                opacity: 0;
            }
            25% {
                opacity: 1;
            }
            75% {
                opacity: 1;
            }
            100% {
                bottom: 100vh;
                opacity: 0;
            }
        }
        </style>
        <div class="emoji">😊</div>
        """,
        unsafe_allow_html=True
    )
