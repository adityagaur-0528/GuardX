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


def privacy_analysis(metadata):
    """
    Analyze metadata fields for potential privacy exposure.
    """

    sensitive_fields = [
        "GPSInfo",
        "DateTime",
        "DateTimeOriginal",
        "DateTimeDigitized",
        "Make",
        "Model",
        "Software"
    ]

    exposed_fields = []

    for field in metadata:
        if field in sensitive_fields:
            exposed_fields.append(field)

    return exposed_fields


if __name__ == "__main__":

    image_path = input("Enter image path: ").strip()

    result = analyze_metadata(image_path)

    print("\n========== GUARDX METADATA ANALYSIS ==========")

    # Error handling
    if "error" in result:
        print("Error:", result["error"])

    # No metadata
    elif not result["metadata_found"]:
        print("No EXIF metadata found.")
        print("\nPrivacy Status: No metadata exposure detected.")

    # Metadata found
    else:

        print("EXIF metadata detected:\n")

        for key, value in result["metadata"].items():
            print(f"{key}: {value}")

        # Privacy analysis
        exposed_fields = privacy_analysis(result["metadata"])

        print("\n---------- PRIVACY ANALYSIS ----------")

        if exposed_fields:

            print("Potentially exposed metadata fields:")

            for field in exposed_fields:
                print(f"• {field}")

            print(f"\nMetadata fields detected: {len(result['metadata'])}")

            print("\nPrivacy Note:")
            print(
                "Image metadata may contain information that is "
                "not directly visible in the image."
            )

            print("\nPrivacy Status: Metadata exposure detected.")

        else:

            print("No commonly privacy-sensitive metadata fields detected.")

            print(f"\nMetadata fields detected: {len(result['metadata'])}")

            print("\nPrivacy Status: No major metadata exposure detected.")

    print("\n==============================================")