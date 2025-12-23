import requests
from bs4 import BeautifulSoup
import pandas as pd

print("🚀 スクレイピングを開始します...")

# 1. サイト情報（Day 20と同じ Python公式サイト）
url = "https://www.python.org/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 2. データを入れる「空のリスト」を準備
data_list = []

# 3. データを抽出（Day 20のロジックを使用）
news_widget = soup.find("div", class_="blog-widget")

if news_widget:
    news_items = news_widget.find_all("li")
    
    for item in news_items:
        # タイトルとURLを取得
        title = item.find("a").text
        link = item.find("a")["href"]
        
        # URLが "/downloads/..." のように省略されている場合があるので補完する
        full_url = f"https://www.python.org{link}" 
        
        # 辞書（Dictionary）にまとめる
        data = {
            "Title": title,
            "URL": full_url
        }
        
        # リストに追加（append）
        data_list.append(data)

# 4. 表（DataFrame）に変換
df = pd.DataFrame(data_list)

# 結果を表示
print("\n📊 取得したデータ:")
print(df)

# 5. CSVファイルに保存
# index=False: 行番号(0,1,2...)を保存しない設定
# encoding="utf-8_sig": Excelで開いたときの文字化けを防ぐおまじない
df.to_csv("python_news.csv", index=False, encoding="utf-8_sig")

print("\n💾 'python_news.csv' に保存しました！")