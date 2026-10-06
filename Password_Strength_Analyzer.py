#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("=" * 50)
print("          PASSWORD STRENGTH ANALYZER")
print("=" * 50)

password = input("\nEnter a password to analyze: ")

# Check password requirements
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)

special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
has_special = any(char in special_characters for char in password)

# Calculate score
score = 0

if len(password) >= 8:
    score += 1
if has_uppercase:
    score += 1
if has_lowercase:
    score += 1
if has_number:
    score += 1
if has_special:
    score += 1

# Determine password strength
if score <= 2:
    strength = "Weak"
elif score == 3:
    strength = "Moderate"
elif score == 4:
    strength = "Strong"
else:
    strength = "Very Strong"

# Display results
print("\n" + "=" * 50)
print("ANALYSIS RESULTS")
print("=" * 50)

print("Length (8+ characters):", "PASS" if len(password) >= 8 else "FAIL")
print("Uppercase letter:      ", "PASS" if has_uppercase else "FAIL")
print("Lowercase letter:      ", "PASS" if has_lowercase else "FAIL")
print("Number:                ", "PASS" if has_number else "FAIL")
print("Special character:     ", "PASS" if has_special else "FAIL")

print("\nScore:", score, "/ 5")
print("Password Strength:", strength)

# Recommendations
print("\nRECOMMENDATIONS")

if len(password) < 8:
    print("- Use at least 8 characters.")
if not has_uppercase:
    print("- Add at least one uppercase letter.")
if not has_lowercase:
    print("- Add at least one lowercase letter.")
if not has_number:
    print("- Add at least one number.")
if not has_special:
    print("- Add at least one special character.")

if score == 5:
    print("- Your password meets all the requirements!")

print("\n" + "=" * 50)


# In[ ]:




