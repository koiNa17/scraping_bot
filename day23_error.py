import requests
from bs4 import BeautifulSoup
import pandas as pd
import time # 連続アクセスでサーバーに負荷をかけないための「待機」用

# --- 部品（関数）エリア ---

def get_soup(target_url):
    """
    HTMLを取得し、BeautifulSoupオブジェクトを返す（エラーガード付き）
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124"
    }
    
    # 【重要】 try-except構文
    # 「try」の中を実行してみて、もしエラーが起きたら「except」に逃げる
    try:
        response = requests.get(target_url, headers=headers, timeout=10) # 10秒待ってもダメなら諦める
        response.raise_for_status() # 404エラーなどがあればここで検知
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    
    except Exception as e:
        # エラーが起きたら、止まらずにメッセージだけ出して None (空っぽ) を返す
        print(f"⚠️ エラーが発生しました: {target_url}")
        print(f"   理由: {e}")
        return None

def extract_python_news(soup):
    """
    ニュースを抽出する関数
    """
    # soupが空っぽ（エラーだった）場合は、空のリストを返して終わる
    if soup is None:
        return []

    data_list = []
    # ※ページによって構造が違う場合があるため、汎用的に動くか確認が必要ですが
    # 今回はPython公式サイト内の同じ構造のページを想定します
    news_widget = soup.find("div", class_="blog-widget")

    if news_widget:
        news_items = news_widget.find_all("li")
        for item in news_items:
            title = item.find("a").text
            link = item.find("a")["href"]
            
            # URLが http から始まっていない場合は補完する
            if not link.startswith("http"):
                link = f"https://www.python.org{link}"
            
            data = {
                "Title": title,
                "URL": link
            }
            data_list.append(data)
            
    return data_list

def save_to_csv(data_list, filename):
    if not data_list:
        print("⚠️ 保存するデータがありません。")
        return

    df = pd.DataFrame(data_list)
    df.to_csv(filename, index=False, encoding="utf-8_sig")
    print(f"💾 '{filename}' にデータを保存しました！(件数: {len(df)}件)")

# --- メイン実行エリア ---

def main():
    print("🚀 タフなスクレイピングボット起動")
    
    # 1. 巡回したいURLのリスト
    url_list = [
        "https://www.python.org/",          # 存在するページ
        "https://www.python.org/invalid",   # 存在しないページ（わざとエラーにする実験用）
        "https://www.python.org/psf/"       # 存在するページ（PSF情報）
    ]
    
    all_data = [] # 全ページのデータをここに集める

    # 2. リストの中身を順番に処理
    for url in url_list:
        print(f"\n📡 {url} にアクセス中...")
        
        # 取得
        soup = get_soup(url)
        
        # 抽出
        news = extract_python_news(soup)
        
        # 見つかったデータを全体の箱に追加（extendはリスト同士を結合する命令）
        if news:
            all_data.extend(news)
            print(f"   ✅ {len(news)} 件のニュースを取得")
        else:
            print("   💨 ニュースは見つかりませんでした")

        # サーバーへの礼儀として1秒休む
        time.sleep(1)

    # 3. 最後にまとめて保存
    save_to_csv(all_data, "python_news_multi.csv")
    print("\n✅ 全処理が完了しました。")

if __name__ == "__main__":
    main()