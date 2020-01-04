from github import Github
import argparse
from getpass import getpass

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', help="username")
parser.add_argument('-r', '--repo', help="repository")
args = parser.parse_args()



user, repo = args.user, args.repo
password = getpass()

# login with username and password
g = Github(user, password)

repo = g.get_repo(user + '/' + repo)
print(repo)
print(repo.get_topics())
print(repo.stargazers_count)

# show the contents of the root directory of the repo
# for content in repo.get_contents(''):
#     print(content) 

# show the contents recursively
# contents = repo.get_contents('')
# while contents:
#     file_content = contents.pop(0)
#     if file_content.type == 'dir':
#         contents.extend(repo.get_contents(file_content.path))
#     else:
#         print(file_content)


# get top 10 referrers over the last 14 days
# content = repo.get_top_referrers()
# print(content)

# get top 10 paths over the last 14 days
# content = repo.get_top_paths()
# print(content)

# get the number of clones and breakdown over the last 14 days
contents = repo.get_clones_traffic()
contents = repo.get_clones_traffic(per="week")
print(contents)

contents = repo.get_views_traffic()
contents = repo.get_views_traffic(per="week")
print(contents)