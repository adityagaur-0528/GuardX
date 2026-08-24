from PIL import Image


def sanitize_image(input_path, output_path):
    """
    Remove EXIF metadata from an image
    and save a clean copy.
    """

    try:
        image = Image.open(input_path)

        # Create a new image without the original EXIF data
        clean_image = Image.new(image.mode, image.size)
        clean_image.putdata(list(image.getdata()))

        # Save the clean image
        clean_image.save(output_path)

        return {
            "success": True,
            "output_path": output_path
        }

    except Exception as error:
        return {
            "success": False,
            "error": str(error)
        }


if __name__ == "__main__":

    print("\n========== GUARDX METADATA SANITIZER ==========")

    input_path = input("Enter input image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    result = sanitize_image(input_path, output_path)

    if result["success"]:

        print("\nSanitization completed successfully.")
        print("Original image :", input_path)
        print("Sanitized image:", output_path)

        print("\nPrivacy Action:")
        print("EXIF metadata has been removed from the sanitized copy.")

    else:

        print("\nSanitization failed.")
        print("Error:", result["error"])

    print("\n==============================================")