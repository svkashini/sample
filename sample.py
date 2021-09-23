import streamlit as st
import pandas as pd

st.title('アップされたcsvファイルを３倍にするアプリ')

upload_file = st.file_uploader('csvファイルをアップロードしてください。')

if upload_file is not None:
    df = pd.read_csv(upload_file)
    temp = pd.DataFrame([])
    i = 0 
    while i < 3:
        temp = pd.concat([temp, df], axis=0)
        i += 1

    st.download_button(
        label='３倍になったファイルをダウンロード',
        data=temp.to_csv(),
        file_name='download.csv',
        mime='text/csv',
    )




