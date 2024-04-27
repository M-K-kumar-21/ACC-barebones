from git import Repo

def clone(url):
    # URL of the Git repository you want to clone
    git_url = url

    # Local directory where you want to clone the repository
    repo_dir = 'RepoCopy'

    # Clone the repository
    Repo.clone_from(git_url, repo_dir)

    print("Repository cloned successfully.")
