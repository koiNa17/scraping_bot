import requests
from bs4 import BeautifulSoup

# 1. ターゲットのURL（本物のWebサイト）
url = "https://example.com/"

print(f"🌍 {url} にアクセス中...")

# 2. Webサイトのデータを取得（リクエストを送る）
response = requests.get(url)

# 通信が成功したかチェック（200なら成功）
if response.status_code == 200:
    print("✅ アクセス成功！")
    
    # 3. 取得したHTMLをスープ（解析できる状態）にする
    soup = BeautifulSoup(response.text, "html.parser")

    # 4. 情報を抜き出す
    print("--------------------------------")
    
    # タイトルを取得
    print("▼ タイトル:")
    print(soup.title.text)
    
    # H1（大見出し）を取得
    print("\n▼ 大見出し:")
    print(soup.h1.text)
    
    # P（本文）を取得
    print("\n▼ 本文の最初の部分:")
    print(soup.p.text)
    
    print("--------------------------------")

else:
    print("❌ アクセス失敗...", response.status_code)