import os
import re

try:
    from PIL import Image
    import PIL.JpegImagePlugin
    import PIL.PdfImagePlugin
except ImportError:
    raise ImportError("Pillow is required to run this script. Install it with 'pip install pillow'.")

folder_path = "images"  # Folder containing the images
output_pdf = "genkitb.pdf"

supported_formats = (".jpg", ".jpeg", ".png", ".bmp", ".webp")


def natural_key(filename: str):
    """Sort filenames by numeric parts first, then alphabetic parts."""
    parts = re.split(r"(\d+)", filename.lower())
    return [int(part) if part.isdigit() else part for part in parts]


if not os.path.isdir(folder_path):
    raise FileNotFoundError(f"Folder not found: {folder_path}")

image_files = sorted(
    [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(supported_formats)
    ],
    key=lambda path: natural_key(os.path.basename(path))
)

images = []
for file_path in image_files:
    with Image.open(file_path) as img:
        img = img.convert("RGB")
        images.append(img.copy())

if not images:
    print("No images found in the folder.")
else:
    images[0].save(
        output_pdf,
        format="PDF",
        save_all=True,
        append_images=images[1:]
    )
    print(f"PDF created successfully: {output_pdf}")
