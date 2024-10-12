import os
import sys
from dotenv import load_dotenv
from github import Github
import github
from pathlib import Path

def load_env_files():
    # スクリプトのディレクトリの.envを読み込む
    load_dotenv()
    
    # 作業ディレクトリの.envを読み込む
    work_env = Path.cwd() / '.env'
    if work_env.exists():
        load_dotenv(work_env)

def add_collaborator_to_repo(repo_full_name, collaborator):
    # GitHubのPersonal Access Tokenを環境変数から取得
    token = os.getenv('GITHUB_ACCESS_TOKEN')
    if not token:
        print("Error: GITHUB_ACCESS_TOKEN environment variable not set.")
        sys.exit(1)

    # GitHubクライアントを初期化
    g = Github(token)

    try:
        # リポジトリを取得
        repo = g.get_repo(repo_full_name)

        # コラボレーターを追加
        repo.add_to_collaborators(collaborator)
        print(f"Added {collaborator} as a collaborator to {repo_full_name}.")

    except github.GithubException as e:
        print(f"An error occurred: {e.status} {e.data}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <full_repo_name> <collaborator>")
        sys.exit(1)

    repo_full_name = sys.argv[1]
    collaborator = sys.argv[2]
    add_collaborator_to_repo(repo_full_name, collaborator)

# python github_add_collaborator.py HarmonAI-III iris-s-coon
# python github_add_collaborator.py HarmonAI-III iris-s-coon
# python .\.github\github_add_collaborator.py Sunwood-ai-labs/HarmonAI_III yukihiko-fuyuki
# python .\.github\github_add_collaborator.py Sunwood-ai-labs/HarmonAI_III yukihiko-fuyuki
