import os
from PIL import Image

# 设置文件夹路径
source_folder = "B:\\projects\\my-blog\\source\\art\\zyh\\xl\\media"  # 替换为你的图片文件夹
target_folder = "B:\\projects\\my-blog\\source\\images\\art" # 替换为输出文件夹

# 创建目标文件夹
os.makedirs(target_folder, exist_ok=True)

# 遍历并处理图片
for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg','webp')):
        try:
            # 提取图片序号
            num = ''.join([c for c in filename if c.isdigit()])
            
            # 构建新文件名
            new_name = f"art_{num}.jpg"
            
            # 打开图片并保存为新格式
            img = Image.open(os.path.join(source_folder, filename))
            img.convert('RGB').save(os.path.join(target_folder, new_name), 'JPEG')
            
            print(f"{filename} -> {new_name}")
        except:
            print(f"跳过 {filename} (无法处理)")

print("转换完成！")