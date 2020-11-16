import requests
from time import sleep


def getStatsContributors(address, retryTime=5, retryInterval=1):
    print("\nstarting..." + address)
    url = f"https://api.github.com/repos/{address}/contributors"
    res = []
    for i in range(1, 51):
        params = {
            "anon": 1,
            "page": i,
            "per_page": 100
        }
        data = None
        for _ in range(retryTime):
            try:
                resp = requests.get(url, params)
                data = resp.json()
                resp.close()
                break
            except:
                sleep(retryInterval)
                pass

        if data is None:
            print("----> request error")
            return None

        if len(data) == 0:
            print("----> no data")
            break

        for d in data:
            login, name, email = None, None, None
            if d['type'] == 'Anonymous':
                name, email = d['name'], d['email']
            else:
                login = d['login']
            res.append({
                "login": login,
                "name": name,
                "email": email,
                "commits": d['contributions']
            })

        if len(data) < 100:
            print("----> last page")
            break

    print(f"get {address} contributors done")
    return res


getStatsContributors("kubernetes/kubernetes")
