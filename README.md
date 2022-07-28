# 画像の前処理

使用するモデルに合わせて画像に前処理を加える。

## 一覧(順次追加)
|  file name  |  discription  |
| ---- | ---- |
| bgw.py | 背景透過を用いて背景を白色にする |
| crop.py | 正方形状にcenter cropする。|


## 環境
`bgw.py`は`rembg`ライブラリを使用するため**Python3.9**のみでしか動作確認をしていない。
<br>
CPU support:
```
pip install rembg
```

GPU support:
```
pip install rembg[gpu]
```

`Pillow`がなければインストール
```
pip install Pillow
```

## 実行方法
下記のコードを参照。オプションについては次項参照のこと
```
python bgw.py --inupt_image=sample.png
python crop.py --input_image=sample.py --is_resize=True --crop_size=512
```

## オプション
`--input_image`と`--input_dir`は片方のみ使用可能。1枚だけに処理を施す場合は`--input_image`でもよい。

### `bgw.py`

|  option  |  discription  |
| ---- | ---- |
|  --input_image  |  単一画像へのパス  |
|  --input_dir  |  画像が複数入ったフォルダへのパス。フォルダの中の画像は1枚でも可。  |
|  --out_dir    |  出力場所。デフォルトは`result`  |
|

### `crop.py`
`--is_resize`は(w, h)の短い辺を`--crop_size`にする。補間はBICUBICを用いている。Pillow 10での変更(2023/7/1)に対応。
|  option  |  discription  |
| ---- | ---- |
|  --input_image  |  単一画像へのパス  |
|  --input_dir  |  画像が複数入ったフォルダへのパス。フォルダの中の画像は1枚でも可。  |
|  --out_dir    |  出力場所。デフォルトは`result`  |
|  --is_resize  |  crop前にresizeするかどうか。`bool`でデフォルトは`False`|
|  --crop_size  |  cropする画像のサイズ。デフォルトは256。偶数のみ指定可能。 |
|

## Acknowledge 
The Liblary `rembg` is implemented at [@danielgatis](https://github.com/danielgatis/rembg). 
