# Question 4: Steps of Push Commands in Git

**Name**: S Deeksha  
**Course**: BTech in CSE AIML  

## Aim
To demonstrate the complete workflow of git push commands from local to remote repository.

## Procedure
1. Initialized new repository `push-commands`
2. Created `push_steps.py` using `vi` editor with push workflow code
3. Staged and committed file locally
4. Modified file and made second commit
5. Created remote repo `push-commands` on GitHub
6. Linked local repo to remote using `git remote add origin`
7. Pushed commits to GitHub using `git push -u origin main`

## Key Commands for Push
1. `git remote add origin <url>` - Connect local repo to GitHub
2. `git branch -M main` - Rename branch to main
3. `git push -u origin main` - First push, sets upstream tracking
4. `git push` - Subsequent pushes to remote

## Observation
- `git push` transfers local commits to remote GitHub repository
- `-u` flag sets upstream so future `git push` works without args
- All local commits appear on GitHub after successful push

## Result
Successfully demonstrated push command workflow. Local repo is now synced with GitHub remote.

## Conclusion
The `git push` command uploads committed changes from local to remote repository. It requires remote setup via `git remote add` and branch naming. This completes the Git workflow: working directory → staging → local repo → remote repo.
