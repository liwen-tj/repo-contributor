from projects import getCNCFProjects
from contributors import getStatsContributors, getInfoFromLogin
import pickle


#
# projects =
# [
#     {
#         'project': 'hypertrons',
#         'address': 'hypertrons/hypertrons',
#         'contributors': [
#             {
#                 "login": "liwen-tj",
#                 "name": None,
#                 "email": None,
#                 "commits": 9
#             }
#         ]
#     }
# ]
#
def getData():
    graduated, incubating = getCNCFProjects()
    projects = graduated + incubating
    for proj in projects:
        proj['contributors'] = getStatsContributors(proj['address'])
        print(proj['project'], len(proj['contributors']))

    with open("tmp/projects.pkl", "wb") as f:
        pickle.dump(projects, f)
    return projects


def commonContributors(p1, p2):
    c1, c2 = [u['login'] for u in p1['contributors']], [u['login'] for u in p2['contributors']]
    inter = set(c1).intersection(set(c2))
    return {
        "p1": p1['project'],
        "p2": p2['project'],
        "contributors": inter
    } if len(inter) > 0 else None


def fillNameAndEmail():
    with open("tmp/projects.pkl", "rb") as fp:
        projects = pickle.load(fp)
    with open("users.pkl", "rb") as fu:
        users = pickle.load(fu)
    names = []
    for p in projects:
        contributors = p['contributors']
        print("\n---> executing", p['address'])
        counter = 0
        for c in contributors:
            if c['name'] is None:   # ----> normal
                if c['login'] in users:
                    (c['name'], c['email']) = users[c['login']]
                else:
                    c['name'], c['email'] = getInfoFromLogin(c['login'])
                    users[c['login']] = (c['name'], c['email'])
            else:                   # ----> anonymous
                names.append((c['name'], c['email']))
                counter += 1

        print("---> total--anonymous-->", len(contributors), counter)

    with open("names.pkl", "wb") as fn:
        pickle.dump(names, fn)

    with open("data.pkl", "wb") as fd:
        pickle.dump(projects, fd)


def getEmailLogin():
    email_login = {}
    with open("users.pkl", "rb") as f_users:
        users_info = pickle.load(f_users)
        for login in users_info:
            name_email = users_info[login]
            if name_email[1] is not None:
                email_login[name_email[1]] = login
    return email_login


def fixProjects():
    el = getEmailLogin()
    with open("data.pkl", "rb") as fp:
        projects = pickle.load(fp)
    for proj in projects:
        for c in proj['contributors']:
            if c['login'] is None:
                if c['email'] in el:
                    c['login'] = el[c['email']]
                else:
                    c['login'] = c['name'] if c['name'] is not None else c['email']

    with open("final.pkl", "wb") as new:
        pickle.dump(projects, new)


if __name__ == '__main__':
    getData()
    fillNameAndEmail()
    fixProjects()
