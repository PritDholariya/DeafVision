import warnings
from transformers import pipeline
import pyttsx3

# Suppressing unnecessary warnings
warnings.simplefilter('ignore')

# Initialize image captioning pipeline
caption = pipeline('image-to-text')

# Get the image file path from user input
image_path = "C:/Users/pritd/OneDrive/Pictures/WhatsApp Image 2023-01-22 at 21.55.40.jpg"
# image_path = input("Enter the path to the image file: ")

try:
    print("before caption")
    # Get caption for the uploaded image
    caption_text = caption(image_path)[0]['generated_text']  # Extracting the generated text from the result
    print("after")
    # Display the caption
    print("Image Description:", caption_text)

    engine = pyttsx3.init()
    engine.say(caption_text)
    engine.runAndWait()

except Exception as e:
    print("An error occurred:", str(e))


# import warnings
# from transformers import pipeline
# from PIL import Image
# import matplotlib.pyplot as plt

# # Suppressing unnecessary warnings
# warnings.simplefilter('ignore')

# # Initialize image captioning pipeline
# caption = pipeline('image-to-text')

# # Get the image file path from user input
# image_path = input("C:/Users/pritd/OneDrive/Pictures/WhatsApp Image 2023-01-22 at 21.55.40.jpg")

# try:
#     # Open and display the image
#     # img = Image.open(image_path)
#     # plt.imshow(img)
#     # plt.axis('off')
#     # plt.show()

#     # Get caption for the uploaded image
#     caption_text = caption(image_path)

#     # Display the caption
#     print("Image Caption:", caption_text)

# except Exception as e:
#     print("An error occurred:", str(e))
