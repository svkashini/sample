import streamlit as st
import pandas as pd
import datetime

st.title('アップされたcsvファイルを３倍にするアプリ')

upload_file = st.file_uploader('csvファイルをアップロードしてください。')

tart_date = st.date_input(
    '集計開始日を選択（処理に関係ないけどw）',
    datetime.datetime.today() - datetime.timedelta(days=60)
)

end_date = st.date_input(
    '集計終了日を選択（処理に関係ないけどw）',
    datetime.date.today()
)

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




