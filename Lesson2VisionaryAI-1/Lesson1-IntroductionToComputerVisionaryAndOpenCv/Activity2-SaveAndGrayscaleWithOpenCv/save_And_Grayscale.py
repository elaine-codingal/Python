import cv2
import os

# Define image path
image_path = 'house1.jpg'  # Change this if the image is in another directory

# Check if the file exists
if not os.path.exists(image_path):
    print(f"Error: The file '{image_path}' was not found. Check the path and try again.")
else:
    # Load the image
    image = cv2.imread(image_path)

    # Ensure the image was loaded successfully
    if image is None:
        print(f"Error: Unable to load '{image_path}'. It might be corrupted or in an unsupported format.")
    else:
        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Show the grayscale image
        cv2.imshow("Grayscale Image", gray_image)

        # Save the grayscale image
        gray_image_path = "dog_grayscale.jpg"
        cv2.imwrite(gray_image_path, gray_image)
        print(f"Grayscale image saved as '{gray_image_path}'.")

        # Wait for a key press and close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
