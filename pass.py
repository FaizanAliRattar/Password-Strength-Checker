import streamlit as st
import re

# Set up the page
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

# Title and description
st.title("🔐 Password Strength Checker")
st.markdown(""" 
### Welcome to the ultimate password strength checker!
Make your passwords stronger! Our tool quickly evaluates how secure your password is.
""")

# Toggle to show/hide password
show_password = st.checkbox("Show Password")
password = st.text_input("Enter your password", type="default" if show_password else "password", help="Ensure your password is strong")

# Initialize
feedback = []
score = 0

# Password strength logic
if password:
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Case sensitivity check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper and lower case characters.")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Special character check
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%^&*).")

    # Progress bar and message
    st.progress(score / 4)

    if score == 4:
        st.success("✅ Your password is strong! 🎉")
    elif score == 3:
        st.warning("🟡 Your password is medium strength. It could be stronger!")
    else:
        st.error("🔴 Your password is weak. Please make it stronger!")

    # Show feedback
    if feedback:
        st.markdown("### Suggestions to improve:")
        for item in feedback:
            st.write(item)
else:
    st.info("Please enter your password to get started.")

