# -*- coding: utf-8 -*-
import os
import urllib.parse

project_path = r'c:\Users\Victu\OneDrive\Desktop\Ai関連\hp_development\projects\hp\Usen関連\USEN-Hikari-Plus-tosup'
images_path = os.path.join(project_path, 'images')

# Get all jpg files
jpg_files = [f for f in os.listdir(images_path) if f.lower().endswith('.jpg')]

# Separate main images and tosup images
main_images = [f for f in jpg_files if not f.startswith('tosup')]
tosup_images = [f for f in jpg_files if f.startswith('tosup')]

# Sort each group
main_images.sort()
tosup_images.sort()

# Combine: main images first, then tosup at the end
all_images = main_images + tosup_images

print(f"Found {len(main_images)} main images + {len(tosup_images)} tosup images = {len(all_images)} total")

# Generate HTML
html_content = '''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>USEN光+</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .image-wrapper {
            width: 100%;
            line-height: 0;
        }
        .image-wrapper img {
            width: 100%;
            height: auto;
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
'''

for jpg_file in all_images:
    encoded_name = urllib.parse.quote(jpg_file)
    html_content += f'        <div class="image-wrapper"><img src="images/{encoded_name}" alt="" loading="lazy"></div>\n'

html_content += '''    </div>
</body>
</html>
'''

# Write HTML file
output_path = os.path.join(project_path, 'index.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Created: {output_path}")
