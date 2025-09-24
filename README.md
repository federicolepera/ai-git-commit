# AI Git Commit Helper

This project provides a Python script that uses the Groq AI API to automatically generate **commit messages** for staged changes in a Git repository. The script analyzes the `git diff --cached` output and creates clear, concise commit messages following the **Conventional Commits** style.

---

## Features

- Automatically reads staged changes in your Git repository.
- Generates human-readable, conventional commit-style messages.
- Suggests commit messages in English.
- Allows you to confirm before creating the commit.

---

## Requirements

- Python 3.8 or higher
- `pip` installed
- Groq API key
- Git installed and initialized in your project

Install the required Python package:

```bash
pip install groq
```

---

## Setup

1. **Get a Groq API key:**
   - Sign up at [Groq Console](https://console.groq.com/)
   - Generate an API key
   - Export it in your terminal:
     ```bash
     export GROQ_API_KEY="your_api_key_here"
     ```

2. **Initialize Git in your project (if not already):**
   ```bash
   git init
   git add .
   git commit -m "initial commit"
   ```

3. **Save the script** as `ai_commit.py` in your project folder.

---

## Usage

1. Stage the changes you want to commit:

```bash
git add .
```

2. Run the AI commit helper script:

```bash
python ai_commit.py
```

3. The script will:
   - Analyze your staged changes
   - Generate a suggested commit message
   - Display the message and ask for confirmation

4. Confirm by typing `y` to automatically commit with the generated message.

---

## How it Works

1. **`get_staged_diff()`**
   - Uses `git diff --cached` to get the changes that are staged.

2. **`generate_commit_message(diff)`**
   - Sends the diff to the Groq API using `llama-3.3-70b-versatile`.
   - Generates a clear and concise commit message in conventional commits style.

3. **`main()`**
   - Checks if there are staged changes.
   - Prints the suggested commit message.
   - Prompts the user to confirm the commit.

---

## Notes

- Ensure your Groq API key is set in the environment variable `GROQ_API_KEY`.
- The script uses the `llama-3.3-70b-versatile` model for generating commit messages.
- You can adapt the script to use other Groq-supported models if needed.

---

## Example

```bash
$ git add .
$ python ai_commit.py

💡 Commit message suggested:
feat(utils): add error handling to authentication module

Do you want to commit with this message? [y/N] y
```

---

## License

This project is open-source and free to use under the MIT License.

