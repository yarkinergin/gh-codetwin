import requests
import os
import sys

def fetch_pull_request_files(repo, pull_number, token):
    """Fetch files from a GitHub pull request."""
    token = token.strip()  # Trim whitespace and newline characters from the token
    url = f"https://api.github.com/repos/{repo}/pulls/{pull_number}/files"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        files = response.json()
        if not files:
            print("No files or data available for this pull request.")
        return files
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None

def main():
    if len(sys.argv) != 3:
        print("Usage: python codetwin.py <repository> <pull_number>", file=sys.stderr)
        sys.exit(1)

    repo = sys.argv[1]
    pull_number = sys.argv[2]
    token = os.getenv('GITHUB_TOKEN')
    
    if not token:
        print("GitHub token not set in environment variables.", file=sys.stderr)
        sys.exit(1)
    
    print("Fetching pull request data...")
    files = fetch_pull_request_files(repo, pull_number, token)
    if files:
        for file in files:
            print(f"File: {file['filename']} - Changes: +{file['additions']} -{file['deletions']}")

if __name__ == "__main__":
    main()
