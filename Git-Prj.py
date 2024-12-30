def git_tutorial():
    print("Welcome to the Titties Basics Tutorial!")
    print("Let's learn some common Git commands.\n")
    
    commands = {
        "git init": "Initialize a new Git repository.",
        "git clone <repo>": "Clone an existing repository.",
        "git status": "Check the status of your repository.",
        "git add <file>": "Stage changes to a file for commit.",
        "git commit -m 'message'": "Commit changes with a message.",
        "git push": "Push your commits to a remote repository.",
        "git pull": "Fetch and merge changes from the remote repository.",
        "git branch": "List, create, or delete branches.",
        "git checkout <branch>": "Switch to a different branch.",
        "git merge <branch>": "Merge a branch into the current branch.",
        "git log": "View the commit history.",
    }
    
    for command, description in commands.items():
        input(f"Press Enter to learn about: {command}")
        print(f"{command}: {description}\n")
    
    print("Congratulations! You've completed the Git Basics Tutorial.")

if __name__ == "__main__":
    git_tutorial()