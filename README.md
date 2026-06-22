# Image to PDF Tools

This project was created to make it easy to turn scanned pages or screenshot images into printable PDF files.
It is especially useful when you have multiple ordered images and need a single combined PDF or when a single image contains two pages that must be split.

## Why this exists

- Convert an ordered set of images into one PDF quickly.
- Split double-page scans into separate PDF pages automatically.
- Keep the output file in the project root for easy access.

## How others can use it

1. Put your input images inside the `images/` folder.
2. Install the Pillow library.
3. Run `main.py` to create one combined PDF.
4. Run `split.py` to split each image into two PDF pages.

## Files

- `main.py` — Converts all supported images in `images/` into a single PDF in the project root.
- `split.py` — Splits each image in `images/` into two pages, then saves the result as a PDF in the project root.
- `images/` — Place your input images here.
- `venv/` — Python virtual environment (ignored by `.gitignore`).

## Requirements

- Python 3.x
- Pillow

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

2. Install dependencies:

```powershell
python -m pip install pillow
```

## Usage

### Convert images to a single PDF

Run:

```powershell
python .\main.py
```

Output: `genkitb.pdf`

### Split each image into two pages and save as PDF

Run:

```powershell
python .\split.py
```

Output: `split_tb.pdf`

## Supported image formats

- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`
- `.webp`

## Notes

- Files are sorted naturally by name, so `1.png`, `2.png`, `10.png` keep the expected order.
- The generated PDF files are saved in the project root, not inside the `images/` folder.
- If you want better ordering, use numbered filenames like `01.png`, `02.png`, etc.
