import argparse
import pickledb
from getpass import getpass
from github import Github


parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', help="username")
parser.add_argument('-r', '--repo', help="repository")
args = parser.parse_args()
user, repo = args.user, args.repo

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

def initialize_db(user, repo):
    # specify the database
    db_name = user + '_' + repo + '.db'

    # load the database
    db = pickledb.load(db_name, False)
    db.set('User', user)
    db.set('Repository', repo)
    db.dump()
    return db_name

def get_all_clones(db_name, repo):
    contents = repo.get_clones_traffic()
    print(len(contents['clones']))
    clones = {}
    # create the count
    clones['count'] = contents['count']
    # create the unique
    # create the clones
    

def get_last_clone(db_name, repo):
    pass

def get_all_visitors(db_name, repo):
    contents = repo.get_views_traffic()
    print(len(contents['views']))
    # create the count
    # create the unique 
    # create the visitors

def get_last_visitor(db_name, repo):
    pass

def start_watching(user, repo):
    # get the password
    password = '8981921955diku' #getpass()

    # login with username and password
    g = Github(user, password)
    print('[INFO]Watch has successfully logged in...')

    
    # fetch the repo
    db_name = initialize_db(user, repo)
    repo = g.get_repo(user + '/' + repo)
    get_all_clones(db_name, repo)
    get_all_visitors(db_name, repo)


    # get top 10 referrers over the last 14 days
    # content = repo.get_top_referrers()
    # print(content)

    # get top 10 paths over the last 14 days
    # content = repo.get_top_paths()
    # print(content)

    # get the number of clones and breakdown over the last 14 days
  

start_watching(user, repo)


# fetch and check
print('[INFO]Now fetching the details from the database...')
db = pickledb.load('Diprotiv_Ethmail.db', False)
print(db.get('User'))
print(db.get('Repository'))
