import pandas as pd  # pandasを "pd" というあだ名で読み込む（業界標準）

def analyze_data():
    print("🐼 データ分析を開始します...")

    # 1. CSVファイルの読み込み
    # 前回作成したファイル名に合わせてください（python_news_multi.csv）
    csv_file = "python_news_multi.csv"
    
    try:
        # read_csv: CSVを読み込んで「DataFrame(データフレーム)」という表形式にする魔法のコマンド
        df = pd.read_csv(csv_file)
        print(f"\n📂 '{csv_file}' を読み込みました。")
        
        # 2. データの基本情報を確認
        print(f"📊 データサイズ: {df.shape} (行数, 列数)")
        print("-" * 30)
        
        print("\n👀 最初の5行だけ表示:")
        print(df.head()) # head(): アタマの5行だけ表示する
        
        print("-" * 30)

        # 3. データの抽出（フィルタリング）
        # 例: タイトルに「Python」が含まれる記事だけを抜き出す
        keyword = "Python"
        
        # 【重要】ここがPandasのパワー！
        # 「df['Title']（タイトル列）の文字(str)に keyword が含まれる(contains)」行だけ選ぶ
        filtered_df = df[df['Title'].str.contains(keyword, case=False)] # case=Falseは大文字小文字を区別しない
        
        print(f"\n🔍 '{keyword}' をタイトルに含む記事: {len(filtered_df)} 件見つかりました")
        
        # 抽出結果を表示（見やすくするため、タイトルとURLだけ表示）
        if not filtered_df.empty:
            print(filtered_df[['Title', 'URL']])
        else:
            print("該当する記事はありませんでした。")

    except FileNotFoundError:
        print(f"❌ エラー: '{csv_file}' が見つかりません。前回の課題は完了していますか？")
    except Exception as e:
        print(f"❌ 予期せぬエラー: {e}")

if __name__ == "__main__":
    analyze_data()