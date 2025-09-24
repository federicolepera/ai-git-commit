import os
import subprocess
from groq import Groq

def get_staged_diff():
    """Prende il diff dei file in staging"""
    result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
    return result.stdout

def generate_commit_message(diff):
    """Usa Groq API per generare un commit message"""
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""Analyze the following git diff and write a clear and concise commit message, indicating the changes made to the files in staging.
Use the conventional commits style if possible, and respond with the commit message in English.

Diff:
{diff}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # modello gratuito e veloce
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )

    return response.choices[0].message.content.strip()

def main():
    diff = get_staged_diff()
    if not diff.strip():
        print("⚠️ Nessun file in staging. Usa prima 'git add'.")
        return

    commit_msg = generate_commit_message(diff)
    print("\n💡 Commit message suggerito:\n")
    print(commit_msg)

    confirm = input("\nVuoi usarlo per fare commit? [y/N] ").lower()
    if confirm == "y":
        subprocess.run(["git", "commit", "-m", commit_msg])

if __name__ == "__main__":
    main()
