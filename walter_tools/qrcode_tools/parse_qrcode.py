from PIL import Image
from pyzbar.pyzbar import decode

# 加载二维码图片
image = Image.open('example_qrcode.png')

# 解析二维码图片
decoded_objects = decode(image)

# 打印解析结果
for obj in decoded_objects:
    print('Type:', obj.type)
    print('Data:', obj.data.decode('utf-8'))
