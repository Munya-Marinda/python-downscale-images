# Python Image Downscaler

Batch image compression and resizing script using Pillow.

## Features

- Converts images to JPEG
- Resizes images to a max width (default: 1920px)
- Compresses with adjustable quality
- Skips already processed files
- Supports PNG, JPG, JPEG, WEBP

---

## Project Structure

```
.
├── files
│   ├── input      # Place original images here
│   └── output     # Processed images are saved here
├── main.py
└── requirements.txt
```

---

## Setup

### 1. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

1. Add images to:

```
files/input/
```

2. Run:

```bash
python main.py
```

3. Output will be saved in:

```
files/output/
```

---

## Configuration

Edit these values in `main.py`:

```python
MAX_WIDTH = 1920   # Resize width
QUALITY = 70       # JPEG quality (0–100)
```

---

## Notes

- Existing output files are skipped automatically
- Large PNG screenshots are significantly reduced in size
- Output is always JPEG for better compression

---

## Example

| Before      | After         |
| ----------- | ------------- |
| PNG (70MB+) | JPEG (~2–5MB) |

---

## License

MIT
