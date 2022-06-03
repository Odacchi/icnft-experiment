# はじめに

ICP NFT関連の遊び場。
自分のマシン環境を汚さずに遊ぶため、仮想環境構築にPyenvとPoetryを使います。

## 実行に必要なツール

Pyenv + Poetry

先にインストールしておくこと。細かいやり方はググって下さい。

## 準備

pyenvでpython3.10.4をインストールする。
```
pyenv install 3.10.4
```

Poetryでpythonの仮想環境構築
```
poetry install
```

## 実行

### 設定ファイル

設定ファイルをコピーして作成
```
cp .env.dist .env
```

コピー後、コピー先の設定ファイル（.env, config.yml）を記述する。

### 起動

```
poetry shell
cd src
python main.py
```

もしくは

```
cd src
poetry run python main.py 
```