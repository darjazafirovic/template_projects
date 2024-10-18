#!/usr/bin/env python3

import os
import subprocess
import shutil

def run_command(command):
    """Runs a shell command and prints the output."""
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    return True

def remove_old_git_history():
    """Removes the .git directory if it exists."""
    git_dir = os.path.join(os.getcwd(), '.git')
    if os.path.exists(git_dir):
        shutil.rmtree(git_dir)
        print(".git history removed.")
    else:
        print("No existing .git history found.")

def initialize_new_git_repo():
    """Initializes a new Git repository."""
    run_command(['git', 'init'])
    print("Initialized a new Git repository.")

def rename_branch():
    """Renames the default branch from 'master' to 'main'."""
    run_command(["git", "branch", "-M", "main"])
    print("Branch renamed to 'main'.")

def add_remote_repository(repo_url):
    """Adds a new remote origin."""
    run_command(['git', 'remote', 'add', 'origin', repo_url])
    print(f"Added new remote repository: {repo_url}")

def initial_commit():
    """Creates an initial commit."""
    run_command(['git', 'add', '.'])
    run_command(['git', 'commit', '-m', 'Initial commit'])
    print("Initial commit created.")

def push_to_remote():
    """Pushes to the remote repository."""
    run_command(['git', 'push', '-u', 'origin', 'main'])
    print("Pushed to the remote repository.")

def ask_user_for_github_link():
    """Asks the user if they want to link to a GitHub repository."""
    choice = input("Do you want to link this project to a GitHub repository? (y/n): ").strip().lower()
    if choice == 'y':
        repo_url = input("Enter the GitHub repository URL (either HTTPS or SSH): ").strip()

        # Determine if it's HTTPS or SSH
        if repo_url.startswith("https://"):
            print("Detected HTTPS URL.")
        elif repo_url.startswith("git@"):
            print("Detected SSH URL.")
        else:
            print("Invalid URL format. Please provide either an HTTPS or SSH URL.")
            return None

        return repo_url
    return None

if __name__ == "__main__":
    # Step 1: Remove old .git history
    remove_old_git_history()

    # Step 2: Initialize a new Git repository
    initialize_new_git_repo()

    # Step 3: Rename the branch to 'main'
    rename_branch()

    # Step 4: Ask if the user wants to link to a GitHub repository
    repo_url = ask_user_for_github_link()

    if repo_url:
        # Step 5: Add the new remote repository if the user provided a URL
        add_remote_repository(repo_url)

        # Step 6: Create an initial commit
        initial_commit()

        # Step 7: Push the project to the new remote repository
        push_to_remote()
    else:
        # Step 6: Create an initial commit without pushing
        initial_commit()

        print("Skipping GitHub repository linking. Initial commit will be created locally.")
