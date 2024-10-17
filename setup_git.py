#!/usr/bin/env python3

import os
import subprocess
import shutil

def remove_old_git_history():
    # Remove the .git directory if it exists
    git_dir = os.path.join(os.getcwd(), '.git')
    if os.path.exists(git_dir):
        shutil.rmtree(git_dir)
        print(".git history removed.")
    else:
        print("No existing .git history found.")

def initialize_new_git_repo():
    # Initialize a new Git repository
    subprocess.run(['git', 'init'])
    print("Initialized a new Git repository.")

def add_remote_repository(repo_url):
    # Add a new remote origin
    subprocess.run(['git', 'remote', 'add', 'origin', repo_url])
    print(f"Added new remote repository: {repo_url}")

def initial_commit():
    # Add all files, commit them, and push to the new remote
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Initial commit'])
    print("Initial commit created.")

def push_to_remote():
    # Push to the remote repository
    subprocess.run(['git', 'push', '-u', 'origin', 'main'])
    print("Pushed to the remote repository.")

def ask_user_for_github_link():
    # Ask the user if they want to link to a GitHub repository
    choice = input("Do you want to link this project to a GitHub repository? (y/n): ").strip().lower()
    if choice == 'y':
        repo_url = input("Enter the GitHub repository URL (e.g., https://github.com/user/project.git): ").strip()
        return repo_url
    return None

if __name__ == "__main__":
    # Step 1: Remove old .git history
    remove_old_git_history()

    # Step 2: Initialize a new Git repository
    initialize_new_git_repo()

    # Step 3: Ask if the user wants to link to a GitHub repository
    repo_url = ask_user_for_github_link()

    if repo_url:
        # Step 4: Add the new remote repository if the user provided a URL
        add_remote_repository(repo_url)

        # Step 5: Create an initial commit
        initial_commit()

        # Step 6: Push the project to the new remote repository
        push_to_remote()
    else:
        print("Skipping GitHub repository linking. Initial commit will be created locally.")

        # Step 5: Create an initial commit without pushing
        initial_commit()

    print("Git setup complete!")
