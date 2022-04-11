import cv2
import numpy as np

from PIL import Image
from PIL import ImageChops
# import os
class PictureCom:

    def pict1(self):
        for s in range(1,3):
            # with open(f'/picture/one/pic{s}.jpg') as file1:
            #     image1 = cv2.imread(file1)
            # with open(f'/picture/two/pic{s}.jpg') as file2:
            #     image2 = cv2.imread(file2)
            file1 = f"/picture/one/pic{s}.jpg"
            file2 = f"/picture/one/pic{s}.jpg"
            image1 = cv2.imread(file1)
            image2 = cv2.imread(file2)
            difference = cv2.subtract(image1, image2)
            print(difference,"1213")
            result = not np.any(difference)  # if difference is all zeros it will return False

            if result is True:
                print(s,"两张图片一样")
            else:
                cv2.imwrite("result.jpg", difference)
                print(s,"两张图片不一样")


    def compare_images(diff_save_location):
        """
        比较图片，如果有不同则生成展示不同的图片
        @参数一: path_one: 第一张图片的路径
        @参数二: path_two: 第二张图片的路径
        @参数三: diff_save_location: 不同图的保存路径
        """
        for s in range(1,476):
            image_one = Image.open(rf"E:\pywork\Picture_comparison\picture\one\{s}.png")
            image_two = Image.open(rf"E:\pywork\Picture_comparison\picture\three\{s}.png")
            try:
                diff = ImageChops.difference(image_one, image_two)
                if diff.getbbox() is None:
                    # 图片间没有任何不同则直接退出
                    print(f"{s}We are the same!")
                else:
                    diff.save(diff_save_location)
            except ValueError as e:
                text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                        "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
                        "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
                        "image must match the size of the region.使用2纬的box避免上述问题")
                print("【{0}--{1}】{2}".format(s,e, text))



if __name__ == '__main__':
    picture = PictureCom()
    # picture.pict()
    picture.compare_images()