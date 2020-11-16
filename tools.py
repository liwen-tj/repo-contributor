import pickle

with open("tmp.pkl", "rb") as f:
    data = pickle.load(f)
    print(data)
