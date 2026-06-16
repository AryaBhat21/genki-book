#from images similar to main.py but a pdf which will split the pages rn a picture has 2 pages can u split into 2 pages and save all images in order as pdf
from PIL import Image
import os

# Folder containing the screenshots
folder_path = r"images"   # Change this

output_pdf = os.path.join(folder_path, "split_tb.pdf")

extensions = (".png", ".jpg", ".jpeg")

# Get all images in order
image_files = sorted([
    os.path.join(folder_path, f)
    for f in os.listdir(folder_path)
    if f.lower().endswith(extensions)
])

pdf_pages = []

for file in image_files:
    img = Image.open(file)

    width, height = img.size
    mid = width // 2

    # Split into left and right pages
    left = img.crop((0, 0, mid, height))
    right = img.crop((mid, 0, width, height))

    # Convert to RGB
    pdf_pages.append(left.convert("RGB"))
    pdf_pages.append(right.convert("RGB"))

# Save as PDF
if pdf_pages:
    pdf_pages[0].save(
        output_pdf,
        save_all=True,
        append_images=pdf_pages[1:]
    )
    print(f"PDF created successfully: {output_pdf}")
else:
    print("No images found.")