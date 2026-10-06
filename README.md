# Password Strength Analyzer

## Overview

This project is a Python-based password strength analyzer that evaluates a user-entered password based on common password complexity requirements.

The program analyzes multiple password characteristics, calculates a strength score, classifies the password from Weak to Very Strong, and provides personalized recommendations for improving password complexity.

## Features

The analyzer checks whether a password contains:

- At least 8 characters
- An uppercase letter
- A lowercase letter
- A number
- A special character

Each successful requirement contributes one point toward a maximum score of 5.

## Password Strength Ratings

| Score | Rating |
|---|---|
| 0–2 | Weak |
| 3 | Moderate |
| 4 | Strong |
| 5 | Very Strong |

## Example

A password that meets all five requirements will receive:

```text
Score: 5 / 5
Password Strength: Very Strong
```

If requirements are missing, the program provides recommendations explaining how the password can be improved.

## Demo

![Password Strength Analyzer Demo](<img width="1534" height="758" alt="password analysis demo" src="https://github.com/user-attachments/assets/16f10640-2902-4b8b-9223-283a33465cc3" />
)

## Technologies Used

- Python
- Conditional Logic
- Variables
- User Input
- String Methods
- Iteration
- Boolean Logic

## Skills Demonstrated

- Python programming fundamentals
- Input validation and analysis
- Conditional statements
- String manipulation
- Boolean expressions
- Algorithmic problem solving
- Security-focused programming concepts

## Project File

The `password_analyzer.py` file contains the complete Python program.
