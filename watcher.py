from multiprocessing import AuthenticationError
from time import time
from github import Github
import json
from datetime import datetime, timedelta
# First create a Github instance:

config = None
with open('secrets.json', 'r') as json_file:
	config = json.load(json_file)

# using an access token
g = Github(config["access_token"])
for repo in g.get_user().get_repos():
    try:
        # ok, so there is a lot going on here
        # TODO: Figure out and understand how githubs pagination API works
        # TODO: Get the first git commit (To Get Author)
        # TODO: Make sure the first git commit author is wfletch
        # TODO: Get the most recent git commit (To get last edit date)
        # TODO: Make sure the most recent git author is wfletch
        commits = repo.get_commits().reversed.get_page(0)
        first_commit = commits[0]
        most_recent = commits[-1]
        if str(first_commit.author.login) == "wfletch":
            mr_commit = repo.get_commit(sha=most_recent.sha)
            time_between_insertion = datetime.now() - mr_commit.commit.author.date
            if time_between_insertion.days:
                print("No Commit for over 5 days for repository: ", repo.full_name)
                # TODO: Append to list
                # TODO: Send out Email
    except Exception as E:
        print(E)
