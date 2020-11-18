import pickle

# data =
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


def howManyContributors(projects):
    for p in projects:
        print(p['address'], len(p['contributors']))
    print(len(projects))


# 我们遍历projects对象
# 1. 对于不是匿名的贡献者，我们直接使用login
# 2. 对于匿名的贡献者，我们根据email来查找login，如果找到login，那很好。否则，我们就把name/email作为id
if __name__ == '__main__':
    with open("final.pkl", "rb") as ff:
        data = pickle.load(ff)
    howManyContributors(data)




