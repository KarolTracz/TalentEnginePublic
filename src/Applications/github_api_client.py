import requests
from src.config.config import Config


class GitHubAPIClient:
	def get_search_repo_body(
			self,
			q: str = 'a',
			order:  str = "desc",
			sort: str = "best-match",
			per_page: int = 30,
			page: int = 1
	):
		"""
		:param q: Required. The query contains one or more search keywords and qualifiers. Qualifiers allow you
		to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as the web interface
		for GitHub. To learn more about the format of the query, see Constructing a search query.
		See "Searching for repositories" for a detailed list of qualifiers.

		:param sort: Sorts the results of your query by number of stars, forks, or help-wanted-issues or how recently
		the items were updated. Default: best match Can be one of: stars, forks, help-wanted-issues, updated

		:param order: Determines whether the first search result returned is the highest number of matches (desc) or
		lowest number of matches (asc). This parameter is ignored unless you provide sort.
		Default: desc
		Can be one of: desc, asc

		:param per_page: Optional. The number of results per page (max 100).

		:param page: Optional. Page number of the results to fetch.

		:return: Full body of topic search
		"""
		r = requests.get(
			url=f"{Config.get_property('API_BASE_URL')}/search/topics",
			params={
				'q': q,
				'order': order,
				'sort': sort,
				'per_page': per_page,
				'page': page
			},
			headers={
				"Accept": "application/vnd.github+json",
				"X-GitHub-Api-Version": "2022-11-28",
			}
		)
		data = r.json()
		return data
