# push_steps.py - Demo for git push workflow
print("Git Push Commands Step by Step")

commands = [
    "git init - Initialize repo",
    "git add <file> - Stage files", 
    "git commit -m 'msg' - Save to local repo",
    "git remote add origin <url> - Link to GitHub",
    "git branch -M main - Set main branch",
    "git push -u origin main - Upload to remote"
]

for step, cmd in enumerate(commands, 1):
    print(f"Step {step}: {cmd}")

print("Push complete - Local commits now on GitHub")
