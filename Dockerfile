# ベースとなるPython環境
FROM python:3.9-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なライブラリのインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# コンテナが起動し続けるようにする設定（これがないとすぐ終了してしまうことがあります）
CMD ["tail", "-f", "/dev/null"]