import pixellib
from pixellib.tune_bg import alter_bg
import cv2

change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
output = change_bg.change_bg_img(f_image_path = "sample.jpg",b_image_path = "colored_bg.jpg")
cv2.imwrite("img.jpg", output)