# word2vec_doc2vec

## 前準備
仮想環境で確認する
```
$ brew install python3
$ python3 -m venv venv
$ source venv/bin/activate
(venv)  pip install --upgrade pip
(venv)  pip install --upgrade gensim
(venv)  pip install python-Levenshtein
(venv)  pip install janome
(venv)  deactivate
```

## word2vecを勉強

### word2vecの概要
同義語を検出したり、部分的な文に追加の単語を提案したりできます by wikiより

### 勉強法について
Youtube動画より学習：
https://www.youtube.com/watch?v=9Gih75Ujsq8

今回、著名な学習済みデータセットを使用することが多いらしいので、
サンプルを使って理解します。
```
http://blog.hassaku-labs.com/post/pretrained-word2vec/
※「entity_vector.model.bin」をダウンロードする
```

## doc2vecを勉強

### doc2vecの概要
Doc2Vecは任意の長さの文章を固定長のベクトルに変換する技術 by qiita（https://qiita.com/g-k/items/5ea94c13281f675302ca）

### 勉強法について
青空文庫にある小説を使ってモデルを作り検証します。
https://www.aozora.gr.jp/cards/000148/files/794_ruby_4237.zip







