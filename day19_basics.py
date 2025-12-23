from bs4 import BeautifulSoup

# 1. 練習用の「偽Webページ」を用意します
# 実際のWebサイトからダウンロードしてくると、こういう文字列が手に入ります。
html_data = """
<html>
    <head>
        <title>yoshiの投資レポート</title>
    </head>
    <body>
        <h1>今日の市場動向</h1>
        <p class="content">日経平均は反発しました。</p>
        <p class="date">2025-12-23</p>
    </body>
</html>
"""

# 2. BeautifulSoupで解析の準備（スープを作る）
# html_dataを解析しやすい状態に変換します
soup = BeautifulSoup(html_data, "html.parser")

# 3. 情報を抜き出す（具材をすくう）

# <title>タグの中身を取り出す
print("--------------------------------")
print("▼ ページタイトル:")
print(soup.title.text)

# <h1>タグ（一番大きな見出し）を取り出す
print("\n▼ 大見出し:")
print(soup.h1.text)

# <p>タグのうち、class="content" と書かれたものだけ探す
# find = 「見つける」
news_text = soup.find("p", class_="content").text
print("\n▼ ニュース本文:")
print(news_text)

print("--------------------------------")