import streamlit as st
def check_password(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("🔴Use at least 8 charactors.")
    if any(c.isupper() for c in password):
        score +=1
    else:
        tips.append("🟠Include upper letter.")
    if any(c.islower() for c in password):
        score +=1
    else:
        tips.append("🟡Include lower letter.")
    if any(c.isdigit() for c in password):
        score +=1
    else:
        tips.append("🟢Add a number (0-9).")
    if any(c in "!@#$%^&*" for c in password):
        score +=1
    else:
        tips.append("🔵Use a special charactor (!@#$%^&*).")
    return score, tips

def main ():
    
    st.subheader(" Created By Zeeshan Ahmed")
    st.title("🔐 Password Strength Meter")
    password = st.text_input("Enter password 🔑", type="password")
    if password:
        score, tips = check_password(password)

        if score == 5:
            st.success(" ✅strong Password! Secure & Safe.")
        elif score == 3 or score == 4:
            st.warning(" ⚠️Moderate password! Improve it.")
        else:
            st.error("❌weak password! Follow these steps:")
        for tip in tips:
            st.write(tip)
main()
