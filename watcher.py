from github import Github
import json
# First create a Github instance:

config = None
with open('secrets.json', 'r') as json_file:
	config = json.load(json_file)

# using an access token
g = Github(config["access_token"])
for repo in g.get_user().get_repos():
    print(repo.name)