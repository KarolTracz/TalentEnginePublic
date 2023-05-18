from src.config.config import Config
import requests


class GitHubAPIClient:

    # def __call__(self, *args: Any, **kwds: Any) -> Any:
    #     pass

    # def __new__(cls) -> Self:
    #     pass

    def __init__(self) -> None:
        pass

    def login(self, username, password):
        print(f"DO LOGIN for {username} and {password}")

    def logout(self):
        print("DO LOGOUT")

    def get_emojis(self):
        """
            Get list of available emojis in github sustem
        """

        r = requests.get(
            url=f"{Config.get_property('API_BASE_URL')}/emojis",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        )
        print("Get Emojis Response Status Code:", r.status_code)
        
        r.raise_for_status()
        body = r.json()
        list_of_emojis = body.keys()

        return list_of_emojis