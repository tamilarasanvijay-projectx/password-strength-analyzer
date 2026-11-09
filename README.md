# Password Strength Analyzer

A beginner-friendly Python cybersecurity project that checks a password against a set of basic strength rules and provides suggestions for improvement.

## Features

- Checks password length.
- Checks uppercase and lowercase letters.
- Checks numbers and special characters.
- Gives a score out of 6.
- Classifies the result as **Weak**, **Medium**, **Strong**, or **Very Strong**.
- Provides suggestions to improve a password.
- Uses Python's built-in modules only; no API key or third-party package is required.
- Does not save or transmit the password.

## Requirements

- Python 3.9 or newer recommended.
- A terminal, command prompt, VS Code terminal, or a Python IDE such as Pydroid 3.

## Project files

```text
password-strength-analyzer/
├── password_checker.py
├── test_password_checker.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Run the project

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Run:

   ```bash
   python password_checker.py
   ```

   On some systems, use `python3 password_checker.py`.

4. Enter a test password when prompted. In a supported terminal, the input is hidden while typing.

### Android

You can run the project in Pydroid 3 or another Python environment that supports Python 3. Open `password_checker.py` and press Run. If the IDE does not support hidden password input, the program falls back to ordinary input; use only a made-up test password in that situation.

## Run the tests

```bash
python -m unittest -v
```

## Scoring rules

| Check | Point |
|---|---:|
| At least 8 characters | 1 |
| At least 12 characters | 1 |
| Contains uppercase letter | 1 |
| Contains lowercase letter | 1 |
| Contains a number | 1 |
| Contains a special character | 1 |
| **Maximum** | **6** |

The score is a simple classroom demonstration. It is not a formal security measurement. A long, unique passphrase is generally preferable to a short password that merely combines character types.

## Example

```text
==============================================
          PASSWORD STRENGTH ANALYZER
==============================================
Your password is analyzed locally and is not stored.
Enter a password to analyze: [hidden]

------------- ANALYSIS RESULT -------------
Password length : 17 characters
Security score  : 6/6
Strength        : VERY STRONG

Your password meets all of this project's checks.
```

## Security and limitations

- Do not enter your real password into an unfamiliar or shared device.
- This project does not store, log, or send passwords.
- It does not check password breach databases, common-password lists, or password reuse.
- Passing the checks does not guarantee that a password is secure.

## GitHub submission instructions

1. Sign in to [GitHub](https://github.com/).
2. Select **New repository**.
3. Enter the repository name `password-strength-analyzer`.
4. Add a short description: `A Python tool that checks password strength and gives improvement suggestions.`
5. Choose **Public** or **Private**, according to your assignment instructions.
6. Create the repository.
7. Upload the files in this folder, or use Git:

   ```bash
   git init
   git add .
   git commit -m "Add password strength analyzer"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/password-strength-analyzer.git
   git push -u origin main
   ```

8. Replace `YOUR-USERNAME` with your GitHub username.
9. Copy the repository URL and submit that URL.

## Conclusion

The Password Strength Analyzer demonstrates basic password-security checks using Python. It helps users understand why password length and character variety matter and gives practical suggestions for improvement.

## License

This project is provided for educational use. You may adapt it for your coursework.
