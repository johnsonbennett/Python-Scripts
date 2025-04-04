#This script can be used to delete all repositories or can be tweaked to delete specific repositories from your Github account
#This script uses the PyGithub library to connect to the Github API and delete the repositories
#It requires the access token to be generated from your Github account and the token should have the delete permission for the repositories
#This script can be tweaked to perform various operations on the repositories like creating, updating, deleting, etc.
#It also requires the PyGithub library to be installed. You can install it using pip: pip install PyGithub
from github import Github
from github import Auth

auth = Auth.Token("access token") #Replace with your access token
g = Github(auth=auth)

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.delete(repo)