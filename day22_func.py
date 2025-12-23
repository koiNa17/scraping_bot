import requests
from bs4 import BeautifulSoup
import pandas as pd

# --- 部品（関数）の定義エリア ---

def get_soup(target_url):
    """
    指定されたURLからHTMLを取得し、BeautifulSoupオブジェクトを返す関数
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124"
    }
    # データを取得
    response = requests.get(target_url, headers=headers)
    # 解析準備
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def extract_python_news(soup):
    """
    BeautifulSoupオブジェクトからPythonニュースを抽出し、リストで返す関数
    """
    data_list = []
    news_widget = soup.find("div", class_="blog-widget")

    if news_widget:
        news_items = news_widget.find_all("li")
        for item in news_items:
            title = item.find("a").text
            link = item.find("a")["href"]
            full_url = f"https://www.python.org{link}"
            
            # 辞書にまとめる
            data = {
                "Title": title,
                "URL": full_url
            }
            data_list.append(data)
            
    return data_list

def save_to_csv(data_list, filename):
    """
    データのリストをCSVファイルとして保存する関数
    """
    if not data_list:
        print("⚠️ 保存するデータがありませんでした。")
        return

    # DataFrameに変換
    df = pd.DataFrame(data_list)
    # 保存
    df.to_csv(filename, index=False, encoding="utf-8_sig")
    print(f"💾 '{filename}' にデータを保存しました！(件数: {len(df)}件)")

# --- 実行エリア（メイン処理） ---

def main():
    print("🚀 スクレイピングボット起動 (Function版)")
    
    # 1. 設定
    target_url = "https://www.python.org/"
    output_file = "python_news_v2.csv"
    
    # 2. 取得 (担当A)
    print(f"📡 {target_url} にアクセス中...")
    soup_data = get_soup(target_url)
    
    # 3. 抽出 (担当B)
    print("🔍 ニュースを抽出中...")
    news_data = extract_python_news(soup_data)
    
    # 4. 保存 (担当C)
    save_to_csv(news_data, output_file)
    
    print("✅ 全処理が完了しました。")

# このファイルが直接実行されたときだけ main() を動かすおまじない
if __name__ == "__main__":
    main()