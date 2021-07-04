# ----------------------
# このスクリプトはword2vecを勉強するためのスクリプトです
# ----------------------

# 読み込み
from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('./sample_models/word2vec/entity_vector/entity_vector.model.bin',binary=True)

# 単語のベルトル化
# OUTPUT:
#[ 0.09032071 -0.05341686  0.28220174  0.29330444  0.05328318  0.14241028
# -0.24687128  0.18441112  0.02650695  0.0828563  -0.426362   -0.02014246
#  0.02603034 -0.03726895  0.19294073 -0.12511627  0.5407648   0.05329642
# -0.114064   -0.08794833  0.48768535  0.16046745  0.0785282  -0.49404824
#  0.11478704 -0.32564625 -0.55675274 -0.30036446 -0.20920439  0.06128695
# -0.05599485 -0.08785352 -0.17117216  0.28584853  0.01225359  0.15091456
# -0.07321789 -0.07828152  0.16382505  0.38058066  0.19476666  0.06204469
# -0.27429718  0.04294476 -0.05257293  0.05322105 -0.15351981 -0.6151462
#  0.16540758  0.36411384  0.03025797 -0.31749636  0.2605783  -0.05329959
#  0.0940825  -0.1286651  -0.19278173 -0.3219691   0.10385962  0.25326288
# -0.00975231 -0.09564543 -0.3629564  -0.20086282 -0.12936008  0.43610513
# -0.36885667  0.295815   -0.12997843  0.4314916  -0.14947411  0.06331145
#  0.01181818  0.6452983  -0.06020614  0.05043695 -0.04708637  0.01179598
# -0.36667073 -0.17686577  0.17143977  0.3592317   0.3453721  -0.11092807
#  0.03805619  0.11667155 -0.21518715 -0.19824842  0.7911886  -0.28698277
#  0.22000696  0.6519969   0.08775561 -0.03462984 -0.06396964  0.10759465
# -0.27445945  0.12017197  0.2182324   0.02001271 -0.2749907   0.1472141
# -0.15745465 -0.36727196  0.03987442 -0.15021245 -0.12411412  0.47442573
# -0.27764642  0.18471095 -0.19148739  0.4019693   0.04580771 -0.01343833
#  0.05986825 -0.0702235  -0.3262036   0.21441376 -0.05585141  0.4068481
# -0.20326735  0.159737    0.22966705 -0.2549111  -0.38730478 -0.2007898
# -0.12139512 -0.13236366 -0.1494875  -0.8284076   0.14567637 -0.14218427
# -0.20600604 -0.02710883 -0.7757116  -0.23637761 -0.28013197  0.03547173
#  0.08473831 -0.24143983  0.5714134  -0.20404778  0.2857376  -0.12174043
# -0.05783201  0.16254428 -0.11809638  0.45789692  0.567776    0.1777195
# -0.4642111   0.12196863 -0.25125453 -0.02837646 -0.11756613 -0.27768514
# -0.06383181 -0.13533409 -0.09328051  0.01945806 -0.04140085 -0.13909361
#  0.08832241 -0.5650386  -0.13418637  0.01655536 -0.27362147 -0.12080104
#  0.20296168  0.02414615  0.02504183 -0.20633349  0.03708602  0.26493123
# -0.03714316  0.23291802  0.1900764   0.5301852   0.3596682   0.06676093
#  0.18211949  0.01261326 -0.01917026  0.00164132 -0.08637996 -0.03631896
#  0.6470705   0.0400873  -0.08204225  0.15705019 -0.06294098 -0.09003455
#  0.09688611  0.2371008  -0.04234828  0.12725645  0.11786682 -0.5076251
#  0.3587788  -0.19403741]
output = model["イチロー"]
print(output)

# 類似単語の抽出(デフォルトは10個返却)
# ('[前田敦子]', 0.8524860739707947)
# ('[松井玲奈]', 0.8497596383094788)
# ('[柏木由紀]', 0.8481603860855103)
# ('[大島優子]', 0.8426693677902222)
# ('[渡辺麻友]', 0.8364785313606262)
# ('[高橋みなみ]', 0.8302541971206665)
# ('[山本彩]', 0.8275360465049744)
# ('[HKT48]', 0.8238900899887085)
# ('[小嶋陽菜]', 0.8218119144439697)
# ('[島崎遥香]', 0.817225992679596)
results = model.most_similar("[指原莉乃]")
for result in results:
    print(result)

