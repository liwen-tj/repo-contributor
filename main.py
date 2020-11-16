from projects import getCNCFProjects
from contributors import getStatsContributors
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

    with open("projects.pkl", "wb") as f:
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


if __name__ == '__main__':
    data = getData()
    # N = len(data)
    #
    # intersects = []
    # for i in range(N - 1):
    #     for j in range(i + 1, N):
    #         cc = commonContributors(data[i], data[j])
    #         if cc is not None:
    #             intersects.append(cc)
    # print(intersects)
