import pandas as pd
import matplotlib.pyplot as plt

def create_graph():
    print("🎨 グラフ作成を開始します...")

    # 1. データの読み込み（前回作った加工済みデータを使います）
    input_file = "python_news_processed.csv"
    try:
        df = pd.read_csv(input_file)
        
        # 2. キーワード出現数の集計
        # ニュースタイトルに、以下の単語が何回登場するか数えます
        keywords = ['Python', 'Release', 'Bug', 'Security', 'Feature']
        counts = []

        for word in keywords:
            # タイトルの中に word が含まれている行数をカウント
            # case=False は大文字小文字を区別しない（python = Python）
            count = df['Title'].str.contains(word, case=False).sum()
            counts.append(count)

        print("📊 集計結果:")
        for w, c in zip(keywords, counts):
            print(f"  - {w}: {c}")

        # 3. グラフの作成 (Matplotlib)
        plt.figure(figsize=(10, 6)) # 画面サイズの設定 (横10, 縦6)
        
        # 棒グラフ (Bar chart) を描く
        # x軸: キーワード, y軸: 出現数, color: 棒の色('skyblue')
        plt.bar(keywords, counts, color='skyblue')

        # グラフの装飾
        plt.title('Keyword Frequency in News Titles') # タイトル
        plt.xlabel('Keywords') # 横軸ラベル
        plt.ylabel('Count')    # 縦軸ラベル
        plt.grid(axis='y', linestyle='--', alpha=0.7) # グリッド線（横線のみ）

        # 4. グラフを画像として保存
        output_img = "keyword_chart.png"
        plt.savefig(output_img)
        print(f"\n🖼️ グラフを保存しました: {output_img}")
        
        # 最後にplt.close()でメモリを解放するのがマナー
        plt.close()

    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {input_file}")
        print("Day 25の課題（csv作成）が完了しているか確認してください。")
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")

if __name__ == "__main__":
    create_graph()