import qrcode

# 输入数据
data = "https://www.example.com"

# 创建qr对象
qr = qrcode.QRCode(
    version=1,  # 二维码尺寸，1-40的整数
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 纠错等级，分别有L、M、Q和H四种
    box_size=10,  # 二维码每个小格的像素大小
    border=4,  # 二维码的边框宽度
)

# 添加数据
qr.add_data(data)
qr.make(fit=True)

# 生成二维码图片对象
img = qr.make_image(fill='black', back_color='white')

# 保存到文件或显示
# img.save("example_qrcode.png")
img.show()  # 如果要直接在默认图片查看器中查看
