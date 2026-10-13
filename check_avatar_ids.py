import time
import requests
import streamlit as st

BASE = "https://static.showroom-live.com/image/avatar/{}.png"

st.title("アバターID 存在チェック")
center = st.number_input("中心のアバターID", value=1146886, step=1)
width = st.number_input("前後の範囲", value=100, min_value=10, max_value=300, step=10)

if st.button("チェックを実行"):
    start, end = int(center - width), int(center + width)
    found = []
    bar = st.progress(0.0)
    total = end - start + 1
    for n, i in enumerate(range(start, end + 1), start=1):
        try:
            r = requests.head(BASE.format(i), timeout=10)
            if r.status_code == 200:
                found.append(i)
        except requests.RequestException:
            pass
        bar.progress(n / total)
        time.sleep(0.2)  # 負荷を避けるため間隔を空ける
    st.success(f"{start}〜{end} の中に存在したID: {len(found)}件")
    st.write(found)