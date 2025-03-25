import re

def check_password_strength(password):
    # Initialize strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Count met criteria
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Assess strength
    if criteria_met == 5:
        strength = "Strong"
    elif criteria_met >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character (!@#$%^&*(), etc.).")

    return strength, feedback

def main():
    print("Password Complexity Checker")
    password = input("Enter a password to check its strength: ")
    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()