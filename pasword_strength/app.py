import re
import streamlit as st
import random
import string

# Common password blacklist (cuz who still uses "password123"? 🥱)
COMMON_PASSWORDS = ["password", "123456", "qwerty", "admin", "letmein", "welcome", "monkey", "sunshine", "password1", "123456789"]

def generate_strong_password(length=12):
    """Generate a fire password with a mix of uppercase, lowercase, digits, and special characters. 🔥"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Bro, your password is shorter than my attention span. Make it at least 8 characters. 🫠")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Mix it up, fam! Add some uppercase AND lowercase letters. 🌀")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Yo, throw in a number or two. Numbers = instant drip. 🔢")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Spice it up with a special character (!@#$%^&*). You’re basic rn. 🌶️")
    
    # Strength Rating
    if score == 4:
        return "✅ SHEESH! That password is GOATED. No cap. ", feedback
    elif score == 3:
        return "⚠️ Not bad, but you’re mid. Level up your password game. 📈", feedback
    else:
        return "❌ L + Ratio. Your password is weak sauce. Fix it ASAP. 📉", feedback
 
# Function to get strength color and label
def get_strength_color(score):
    if score == 4:
        return "green", "GOATED "
    elif score == 3:
        return "orange", "Mid 😐"
    else:
        return "red", "L + Ratio 📉"
    
def main():
    st.set_page_config(page_title=" WhisperKey 🔐", page_icon="🔥", layout="centered")
    
    # Custom CSS for styling and animations
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    
    body {
        font-family: 'Roboto', sans-serif;
        background-color: white;
    }
    
    .stApp {
        max-width: 800px;
        margin: auto;
        padding: 20px;
        border: 2px solid  #D90429 ;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #0D0D0D ;
        animation: fadeIn 1s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    .stButton>button {
        background-color: #D90429 ;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color:  #D90429 ;
    }
    
    .stTextInput>div>div>input {
        border-radius: 5px;
        border: 1px solid  #D90429 ;
        padding: 10px;
        font-size: 16px;
    }
    
    .stMarkdown h1 {
        color:  #D90429 ;
        text-align: center;
        animation: slideIn 1s ease-in-out;
    }
    
    @keyframes slideIn {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("  VelvetLock 🖤")
    st.write("Your password’s glow-up starts here. No cap.")
    st.write("Drop your password below, and let’s see if it’s fire or mid. 🔥")
    
    # Password input
    password = st.text_input("Enter your password:", type="password")
    
    # Password generator button
    if st.button("Generate a  LockDown Mode 🛑"):
        generated_password = generate_strong_password()
        st.text_input("Generated Password:", value=generated_password, type="password")
    
    if password:
        # Check if password is in the common passwords list
        if password.lower() in COMMON_PASSWORDS:
            st.error("❌   Your password just got ratioed. Try harder. 🤡")
        else:
            strength, feedback = check_password_strength(password)
            st.subheader(strength)
            for suggestion in feedback:
                st.write(suggestion)

if __name__ == "__main__":
    main()
