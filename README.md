# 白背景の画像生成

背景透過ライブラリを用いて入力画像の背景を白色にする。仕組みは透過されたピクセル部分を白く塗っているだけ。

## 環境
`rembg`ライブラリを使用するため**Python3.9**のみしか動作確認をしていません。
<br>
CPU support:
```
pip install rembg
```
<br>

GPU support:
```
pip install rembg[gpu]
```

## 実行方法
下記のコードを参照。オプションについては次項参照のこと
```
python bgw.py --inupt_image=sample.png
```

### オプション
3種類ある。そのうち`input_image`と`input_dir`は片方のみ使用可能。1枚だけに処理を施す場合は`input_image`でもよい。

|  option  |  discription  |
| ---- | ---- |
|  --input_image  |  単一画像へのパス  |
|  --input_dir  |  画像が複数入ったフォルダへのパス。フォルダの中の画像は1枚でも可。  |
|  --out_dir    |  出力場所。デフォルトは`result`  |

## Acknowledge 
The Liblary `rembg` is implemented at [@danielgatis](https://github.com/danielgatis/rembg). 