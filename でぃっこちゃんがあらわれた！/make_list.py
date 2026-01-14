import os
import json

# 画像が入っているフォルダ名
TARGET_FOLDER = 'tentacles'
# 出力するリストのファイル名
OUTPUT_FILE = 'image_list.js'

# フォルダ内の画像ファイルを探す（jpg, pngに対応）
jail_images = []
love_images = []

if os.path.exists(TARGET_FOLDER):
    for filename in os.listdir(TARGET_FOLDER):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # ファイル名に 'jail' が含まれていれば牢屋用
            if 'jail' in filename.lower():
                jail_images.append(f"{TARGET_FOLDER}/{filename}")
            # ファイル名に 'love' が含まれていれば愛す用
            elif 'love' in filename.lower():
                love_images.append(f"{TARGET_FOLDER}/{filename}")

    # 名前順にソート（並び替え）
    jail_images.sort()
    love_images.sort()

# JavaScriptで読み込める形式で保存する
data = {
    "jail": jail_images,
    "love": love_images
}

# image_list.js というファイルを作成
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("const slideData = ")
    json.dump(data, f, indent=4, ensure_ascii=False)
    f.write(";")

print(f"完了！ {OUTPUT_FILE} を作成しました。")
print(f"牢屋用: {len(jail_images)}枚, 愛す用: {len(love_images)}枚")
