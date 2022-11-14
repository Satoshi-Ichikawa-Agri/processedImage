"""要件
Pillowを用いて、以下のように画像を加工するプログラムを作成してください
※ 画像はリサイズすること（大きさは自由)
※ フォントは日本語が表示できれば自由に設定してよい
※「平泉 最高」の文字は画像の真ん中に表示すること
"""
import cv2
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


""" Pillowによる画像への描画 """
# pathを格納する
use_image_file_pillow = "images/konjikido_01.jpg"
# ファイルを開く
img_pillow = Image.open(use_image_file_pillow)
# resize
img_resize_lanczos = img_pillow.resize((1400, 730), Image.LANCZOS)
img_resize_lanczos.save("images/resize_pillow_konjikido_01.jpg")
# img_resize = img_pillow.resize((1400, 730))
# img_resize.save("images/resize_pillow_konjikido_01.jpg")

# Drawオブジェクトを生成
draw_pillow = ImageDraw.Draw(img_resize_lanczos)

# フォントオブジェクト生成
font = ImageFont.truetype("C:/Windows/Fonts/HGRPRE.TTC", 100)

# draw_pillow.text((500, 500), "平泉 最高", "red")
draw_pillow.multiline_text(
    (500, 300),
    "平泉 最高",
    fill=(0, 255, 255),
    font=font,
    align="center",
)
img_resize_lanczos.save("images/result_pillow_konjikido_01.jpg")


""" ここから下はOpenCVによる画像への描画 """
# # 使用する画像を格納する
# use_image_file = "images/konjikido_01.jpg"

# # 画像ファイルの読込
# img = cv2.imread(use_image_file)
# # print(img.shape)

# # Resize
# resize_img = cv2.resize(img, dsize=(2800 // 2, 1460 // 2))
# cv2.imwrite("images/resize_konjikido_01.jpg", resize_img)

# # 画像ファイルの再読込
# use_image_file_recreate = "images/resize_konjikido_01.jpg"
# img_recreate = cv2.imread(use_image_file_recreate)
# # print(img2.shape)

# # 画像に文字を描画する
# drawing_img = cv2.putText(
#     img_recreate,
#     text="Hiraizumi Great",
#     org=(100, 200),
#     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#     fontScale=5,
#     color=(255, 255, 0),
#     thickness=3,
# )
# """cv2.putText()の引数メモ
# 第1引数img: 対象の画像データ。Ndarray 型で指定。
# 第2引数text: 描画する文字。String型で指定。
# 第3引数pt2: 描画する長方形の右下頂点の座標。(int型, int型)のtupleで指定。
# 第4引数fontFace: 描画するフォントの種類。OpenCVの独自コードで指定。
# 第5引数fontScale: 描画する文字の縮尺。float型で指定。
# 第6引数color: 描画する文字の色。(int型, int型, int型)のtupleで指定。
# 第7引数thickness: 印字する文字の太さ。int型で指定。
# (第8引数lineType): 文字を描画するアルゴリズムの種類。OpenCVの独自コードで指定。
# """

# # 描画済みの画像を保存
# cv2.imwrite("images/design_konjikido_01.jpg", drawing_img)
# print("処理完了")

# # 画面に表示する
# cv2.imshow("Image", drawing_img)
# cv2.waitKey(0)
# # 現在までに作られた全てのウィンドウを閉じる関数
# cv2.destroyAllWindows()
