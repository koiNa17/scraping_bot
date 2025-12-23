import requests
from bs4 import BeautifulSoup

# 1. ターゲットURL (Python公式サイト)
url = "https://www.python.org/"
print(f"🌍 {url} にアクセスしてニュースを探します...")

# 2. Webサイトのデータを取得
# headersは「私はロボットじゃなくてブラウザですよ」と伝えるための名刺のようなものです
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124"
}
response = requests.get(url, headers=headers)

# 3. 解析の準備
soup = BeautifulSoup(response.text, "html.parser")

# 4. 狙った場所を特定する (ここが今日のハイライト！)
# Python公式サイトでは、ニュース部分は 'div' タグの 'medium-widget event-widget last' というクラスの中にあります。
# 構造が変わることもあるので、少し広めに「Latest News」という文字を探すアプローチもありますが、
# 今回は「ニュース記事のリンク(aタグ)」を具体的に探してみましょう。

# "blog-widget" というクラスを持つ div（箱）を探します（検証ツールで見つけた名前）
news_widget = soup.find("div", class_="blog-widget")

# もし箱が見つかったら、その中の記事を取り出す
if news_widget:
    print("\n✅ ニュースセクションを発見！記事一覧を表示します:\n")
    
    # 箱の中にある <li> タグ（リストの項目）を全部探す = find_all
    news_items = news_widget.find_all("li")
    
    # for文で、見つかったリストを一つずつ処理する
    for item in news_items:
        # liタグの中にある aタグ（リンク）のテキストを取り出す
        title = item.find("a").text
        # リンクのURLも取り出してみる (href属性)
        link = item.find("a")["href"]
        
        print(f"📰 {title}")
        print(f"   🔗 https://www.python.org{link}")
        print("-" * 30)

else:
    print("❌ ニュースセクションが見つかりませんでした。クラス名が変わった可能性があります。")