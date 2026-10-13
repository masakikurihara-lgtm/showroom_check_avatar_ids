import time
import requests
import pandas as pd
import streamlit as st

BASE = "https://static.showroom-live.com/image/avatar/{}.png"

st.title("アバター画像の公開時刻チェック")
start = st.number_input("開始ID", value=1146877, step=1)
end = st.number_input("終了ID", value=1146913, step=1)

if st.button("チェックを実行"):
    rows = []
    for i in range(int(start), int(end) + 1):
        try:
            r = requests.head(BASE.format(i), timeout=10)
            rows.append({
                "avatar_id": i,
                "status": r.status_code,
                "Last-Modified": r.headers.get("Last-Modified", ""),
            })
        except requests.RequestException:
            rows.append({"avatar_id": i, "status": "error", "Last-Modified": ""})
        time.sleep(0.2)  # 負荷を避けるため間隔を空ける
    st.dataframe(pd.DataFrame(rows))