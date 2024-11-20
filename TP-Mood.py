import streamlit as st
import random

# Create a title for the app
st.title("🌞 How is Your Day! 🌟")

# Create mood options
mood = st.radio(
    "Choose your mood:",
    ("Happy", "Sad", "Terrible", "Neutral")
)

# List of quotes for each mood
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

# Display a quote based on the selected mood
if st.button("Show me a quote"):
    selected_quote = random.choice(quotes[mood])
    st.write(f"**Quote for you:** {selected_quote}")
    
    # Create a smiley face animation
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
