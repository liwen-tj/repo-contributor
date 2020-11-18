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
    total = 0
    coders = {}
    for p in projects:
        pc = p['contributors']
        total += len(pc)
        for obj in pc:
            c = obj['login']
            if c in coders.keys():
                coders[c].append(p['address'])
            else:
                coders[c] = [p['address']]

    people = {}
    for coder in coders:
        index = len(coders[coder])
        if index in people.keys():
            people[index].append(coder)
        else:
            people[index] = [coder]

    print(len(coders))
    for i in range(1, 24):
        if i in people.keys():
            print(i, ":", len(people[i]))
            if i > 7:
                print(people[i])


# 我们遍历projects对象
# 1. 对于不是匿名的贡献者，我们直接使用login
# 2. 对于匿名的贡献者，我们根据email来查找login，如果找到login，那很好。否则，我们就把name/email作为id
if __name__ == '__main__':
    with open("final.pkl", "rb") as ff:
        data = pickle.load(ff)
    howManyContributors(data)

