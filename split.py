#from images similar to main.py but a pdf which will split the pages rn a picture has 2 pages can u split into 2 pages and save all images in order as pdf
import os
import re

try:
    from PIL import Image
    import PIL.JpegImagePlugin
    import PIL.PdfImagePlugin
except ImportError:
    raise ImportError("Pillow is required to run this script. Install it with 'pip install pillow'.")

# Folder containing the screenshots
folder_path = r"images"   # Change this

output_pdf = "split_tb.pdf"  # Save PDF in the project root instead of the images folder

supported_formats = (".png", ".jpg", ".jpeg", ".bmp", ".webp")


def natural_key(filename: str):
    parts = re.split(r"(\d+)", filename.lower())
    return [int(part) if part.isdigit() else part for part in parts]


if not os.path.isdir(folder_path):
    raise FileNotFoundError(f"Folder not found: {folder_path}")

# Get all images in order
image_files = sorted(
    [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(supported_formats)
    ],
    key=lambda path: natural_key(os.path.basename(path))
)

pdf_pages = []

for file in image_files:
    with Image.open(file) as img:
        width, height = img.size

        if width >= height:
            # Split left/right for wide images
            mid = width // 2
            first = img.crop((0, 0, mid, height))
            second = img.crop((mid, 0, width, height))
        else:
            # Split top/bottom for tall images
            mid = height // 2
            first = img.crop((0, 0, width, mid))
            second = img.crop((0, mid, width, height))

        pdf_pages.append(first.convert("RGB").copy())
        pdf_pages.append(second.convert("RGB").copy())

# Save as PDF
if pdf_pages:
    pdf_pages[0].save(
        output_pdf,
        format="PDF",
        save_all=True,
        append_images=pdf_pages[1:],
        quality=100,
        subsampling=0,
        resolution=300.0
    )
    print(f"PDF created successfully: {output_pdf}")
else:
    print("No images found.")