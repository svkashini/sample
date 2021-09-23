import streamlit as st
import pandas as pd
import datetime

st.title('アップされたcsvファイルを３倍にするアプリ')

#この１行でユーザーがドラッグ・ドロップしたファイルが変数upload_fileに格納される
upload_file = st.file_uploader('csvファイルをアップロードしてください。')

#集計開始日の選択BOXを生成。datetime変数はデフォルトで何月何日にするかの設定。ここでは「今日」の60日前をで設定
start_date = st.date_input(
    '集計開始日を選択（処理に関係ないけどw）',#ボタン部分に記載する内容部分
    datetime.datetime.today() - datetime.timedelta(days=60)#デフォルト値の部分
)

#集計終了日の選択BOXを生成。アプリ実行日（今日）をデフォルトの選択値としている
end_date = st.date_input(
    '集計終了日を選択（処理に関係ないけどw）',
    datetime.date.today()
)

if upload_file is not None:#ファイルのアップロードがあった時だけ、以下の処理が実行される
    df = pd.read_csv(upload_file)
    temp = pd.DataFrame()
    i = 0 
    while i < 3:
        temp = pd.concat([temp, df], axis=0)#アップロードしたcsvの内容を空のDataFrameへ３回concatして、ファイル長を３倍にしてるだけ
        i += 1

    #ダウンロードボタン。if文中にあるので、ファイルをアップロードしないとボタンは出てこない
    st.download_button(
        label='３倍になったファイルをダウンロード',
        data=temp.to_csv(),
        file_name='download.csv',
        mime='text/csv',
    )




