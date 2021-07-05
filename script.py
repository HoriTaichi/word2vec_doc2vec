# ----------------------
# このスクリプトはdoc2vecを勉強するためのスクリプトです
# ----------------------

# データの読み込み
with open('./data/doc2vec/sanshiro.txt', encoding='sjis') as file:
    text = file.read()

# ファイル整形
# OUTPUT:
# うとうととして目がさめると女はいつのまにか、隣のじいさんと話を始めている。このじいさんはたしかに前の前の駅から乗ったいなか者である。発車まぎわに頓狂な声を出して駆け込んで来て、いきなり肌をぬいだ
# 171058
import re
text = re.split('\-{5,}',text)[2]
text = re.split('底本：',text)[0]
text = text.replace('｜','')
text = re.sub('《.+?》','', text)
text = re.sub('［＃.+?］','', text)
text = re.sub('\\n\\n','\\n', text)
text = re.sub('\\r','', text)
text = re.sub('　','', text)
text = re.sub(' ','', text)
print(text[:100])
print(len(text))

# 下記のようなリストに変換する
# [
#   [単語1, 単語2, .... ]
#   [単語1, 単語2, .... ]
#   [単語1, 単語2, .... ]
#  ]

# ライブラリの読み込み
def extract_data(text):
    ''' 文章を渡したら、品詞分解した単語のリストを返す
    引数：
    　text：一文
    返り値：
    　data：品詞分解した単語のリスト
    処理概要：
    　１つの文章を受け取り
    　その中に含まれている品詞分解した単語のリストを返す
    '''
    from janome.tokenizer import Tokenizer
    t = Tokenizer()
    data = []
    # 形態素解析
    res = t.tokenize(text)
    for i in res:
        data.append(i.surface)
    return data


# テキストを「。」で区切る
text_list = text.split('。')

# それぞれの文章を単語リストに変換（めっちゃ時間かかる）
word_list = [extract_data(text) for text in text_list]

# 形式の確認
print(len(word_list))
print(word_list[0])

# ライブラリ読み込み
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

# 学習用データに変換
training_docs = []
for i in word_list:
    training_docs.append(
        TaggedDocument(words=i, tags=[str(i)])
    )


# モデルの学習
mode = Doc2Vec(
    documents=training_docs,
    dm=1,         # dmpy
    size=30,      # 分散表現の次元数
    window=8,     # コンテキストの文脈幅
    min_count=1,  # 学習に使う単語の最小出現頻度
    workers=4     # どのくらいのCPUを使うか
)

print(1)