import requests, time
BASE = "https://static.showroom-live.com/image/avatar/{}.png"
found = []
for i in range(1146786, 1147003):   # 1146886〜1146902 の前後100
    r = requests.head(BASE.format(i), timeout=10)
    if r.status_code == 200:
        found.append(i)
    time.sleep(0.2)                 # 負荷を避けるため間隔を空ける
print(len(found), found)