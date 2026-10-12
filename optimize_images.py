
from pathlib import Path
from PIL import Image

# Folder containing this Python script
PROJECT_DIR = Path(__file__).resolve().parent
SOURCE_DIR = PROJECT_DIR / "images"
OUTPUT_DIR = PROJECT_DIR / "images_optimized"

# Optimization settings
MAX_WIDTH = 1200
WEBP_QUALITY = 82

# Images to optimize
IMAGE_FILES = [
    "project-01.jpg",
    "project-02.jpg",
    "project-03.jpg",
    "project-04.jpg",
]


def format_size(size_bytes):
    """Return a readable file size in KB or MB."""
    if size_bytes >= 1_000_000:
        return f"{size_bytes / 1_000_000:.2f} MB"
    return f"{size_bytes / 1_000:.1f} KB"


def optimize_image(filename):
    source_path = SOURCE_DIR / filename
    output_path = OUTPUT_DIR / f"{Path(filename).stem}.webp"

    if not source_path.exists():
        print(f"SKIPPED: {source_path.name} was not found.")
        return

    with Image.open(source_path) as image:
        # Convert to RGB for consistent WebP output.
        image = image.convert("RGB")

        original_width, original_height = image.size

        # Resize only if the image exceeds the maximum width.
        if original_width > MAX_WIDTH:
            new_height = round(
                original_height * MAX_WIDTH / original_width
            )
            image = image.resize(
                (MAX_WIDTH, new_height),
                Image.Resampling.LANCZOS,
            )

        image.save(
            output_path,
            "WEBP",
            quality=WEBP_QUALITY,
            method=6,
        )

    original_size = source_path.stat().st_size
    optimized_size = output_path.stat().st_size

    reduction = (1 - optimized_size / original_size) * 100

    print(f"\n{filename}")
    print(f"  Original:   {format_size(original_size)}")
    print(f"  Optimized:  {format_size(optimized_size)}")
    print(f"  Reduction:  {reduction:.1f}%")
    print(f"  Dimensions: {Image.open(output_path).size}")


def main():
    if not SOURCE_DIR.exists():
        print("ERROR: The images folder was not found.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Pune Elite Interiors - Image Optimization")
    print("-" * 42)

    for filename in IMAGE_FILES:
        optimize_image(filename)

    print("\nDone! Original JPEG files have not been changed.")
    print(f"Optimized images saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
