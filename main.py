import os
from PIL import Image

INPUT_DIR = "files/input"
OUTPUT_DIR = "files/output"

MAX_WIDTH = 1920
QUALITY = 70

os.makedirs(OUTPUT_DIR, exist_ok=True)

SUPPORTED_EXT = (".png", ".jpg", ".jpeg", ".webp")


def process_image(input_path, output_path):
    try:
        img = Image.open(input_path)

        # Resize if needed
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.LANCZOS)

        # Convert to RGB for JPEG
        img = img.convert("RGB")

        # Save compressed
        img.save(output_path, "JPEG", quality=QUALITY, optimize=True, progressive=True)

        print(f"Saved: {os.path.basename(output_path)}")

    except Exception as e:
        print(f"Failed: {input_path} -> {e}")


def main():
    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith(SUPPORTED_EXT):
            continue

        input_path = os.path.join(INPUT_DIR, filename)

        # Force .jpg output
        name_without_ext = os.path.splitext(filename)[0]
        output_filename = f"{name_without_ext}.jpg"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        # Skip if already exists
        if os.path.exists(output_path):
            print(f"Skipped (exists): {output_filename}")
            continue

        process_image(input_path, output_path)


if __name__ == "__main__":
    main()