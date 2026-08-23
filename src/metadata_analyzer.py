from PIL import Image
from PIL.ExifTags import TAGS


def analyze_metadata(image_path):
    """
    Analyze an image for available EXIF metadata.
    """

    try:
        image = Image.open(image_path)
        exif_data = image.getexif()

        if not exif_data:
            return {
                "metadata_found": False,
                "metadata": {}
            }

        metadata = {}

        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, str(tag_id))

            # Keep values that can be safely represented as text
            try:
                metadata[tag_name] = str(value)
            except Exception:
                metadata[tag_name] = "Unavailable"

        return {
            "metadata_found": True,
            "metadata": metadata
        }

    except Exception as error:
        return {
            "metadata_found": False,
            "metadata": {},
            "error": str(error)
        }


if __name__ == "__main__":

    image_path = input("Enter image path: ")

    result = analyze_metadata(image_path)

    print("\n===== GUARDX METADATA ANALYSIS =====")

    if "error" in result:
        print("Error:", result["error"])

    elif not result["metadata_found"]:
        print("No EXIF metadata found.")

    else:
        print("EXIF metadata detected:\n")

        for key, value in result["metadata"].items():
            print(f"{key}: {value}")

    print("====================================")