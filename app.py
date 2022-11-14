"""要件
Pillowを用いて、以下のように画像を加工するプログラムを作成してください
※ 画像はリサイズすること（大きさは自由)
※ フォントは日本語が表示できれば自由に設定してよい
※「平泉 最高」の文字は画像の真ん中に表示すること
"""
import cv2
from PIL import Image


# 使用する画像を格納する
use_image_file = "images/konjikido_01.jpg"

# 画像ファイルの読込
img = cv2.imread(use_image_file)
print(img.shape)
resize_img = cv2.resize(img, dsize=(2800 // 2, 1460 // 2))
cv2.imwrite("images/resize_konjikido_01.jpg", resize_img)

# 画像に文字を描画する
use_image_file2 = "images/resize_konjikido_01.jpg"
img2 = cv2.imread(use_image_file2)
print(img2.shape)
design_img = cv2.putText(
    img2,
    text="平泉 最高",
    org=(100, 200),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=5,
    color=(255, 255, 0),
    thickness=3,
)
# cv2.imshow("Image", img2)  # 読み込んだ画像を表示
# cv2.waitKey(5000)  # 1秒待つ
cv2.imwrite("images/design_konjikido_01.jpg", design_img)
print("処理完了")
