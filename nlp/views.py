# renderとは指定されたテンプレートをレンダリングして、HttpResponseを返す（レスポンス）ためのメソッド
from django.shortcuts import render

# 画面遷移のテスト用
# from django.http import HttpResponse

import pandas as pd
import pickle

# カテゴリ辞書の読み込み
category_data = pd.read_csv("idx2category.csv")
category_data.head()
# category_dataから1行ずつ取り出し{key:value}の辞書型に変換
idx2category = {row.k: row.v for idx, row in category_data.iterrows()}

with open("rdmf.pickle", mode="rb") as f:
    model = pickle.load(f)

def index(request):
    if request.method == "GET":
        return render(
            request,
            "nlp/home.html"
        )
    else:
        # 入力データをリストで取得
        title = [request.POST["title"]]
        # 22カテゴリの内どれにあたるかインデックス0を取得
        result = model.predict(title)[0]
        print("title(input):",title)
        print("result(category_num):",result)
        pred = idx2category[result]
        return render(
             request,
            "nlp/home.html",
            {"title": pred}
        )
        

