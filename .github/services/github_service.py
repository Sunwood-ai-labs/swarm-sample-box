from github import Github
from loguru import logger
from config import get_settings

class GitHubService:
    def __init__(self):
        self.settings = get_settings()
        self.g = Github(self.settings.YOUR_PERSONAL_ACCESS_TOKEN_IRIS)
        try:
            self.repo = self.g.get_repo(self.settings.GITHUB_REPOSITORY)
            logger.info(f"リポジトリ情報: {self.repo.full_name}, Owner: {self.repo.owner.login}")
        except Exception as e:
            logger.error(f"リポジトリの取得中にエラーが発生しました: {str(e)}")
            raise
        logger.debug(f"Using token: {self.settings.YOUR_PERSONAL_ACCESS_TOKEN_IRIS[:5]}...")


    def get_issue(self, issue_number: int = None):
        issue_number = issue_number or self.settings.ISSUE_NUMBER
        logger.debug(f"issue_number : {issue_number}")
        return self.repo.get_issue(number=issue_number)

    def get_comments(self, issue):
        return list(issue.get_comments())

    def add_comment(self, issue, comment):
        issue.create_comment(comment)
        logger.info(f"コメントを追加しました: \n{comment[:200]}...")

    def add_labels(self, issue, labels):
        issue.add_to_labels(*labels)
        logger.info(f"ラベルを追加しました: {', '.join(labels)}")

    def create_pull_request(self, title, body, head, base="main"):
        pr = self.repo.create_pull(title=title, body=body, head=head, base=base)
        logger.info(f"Pull Requestを作成しました: {pr.html_url}")
        return pr

    def create_release(self, tag_name: str, release_notes: str, header_image_url: str = None):
        try:
            # リポジトリの最新コミットを取得
            commits = list(self.repo.get_commits())
            if not commits:
                logger.error("リポジトリにコミットが存在しません。")
                return

            latest_commit = commits[0]
            logger.info(f"最新のコミット: {latest_commit.sha}")

            # タグの存在確認
            if header_image_url:
                release_notes = f"![Release Header]({header_image_url})\n\n{release_notes}"
            
            release = self.repo.create_git_release(
                tag=tag_name,
                name=f"Release {tag_name}",
                message=release_notes,
                draft=False,
                prerelease=False
            )
            logger.info(f"GitHubリリース {tag_name} を作成しました。URL: {release.html_url}")
        except Exception as e:
            logger.error(f"GitHubリリースの作成中にエラーが発生しました: {str(e)}")
            logger.error(f"リポジトリ: {self.repo.full_name}, タグ: {tag_name}")
            logger.error(f"エラーの詳細: {e.__class__.__name__}: {str(e)}")
            raise
