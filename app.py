from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors module
import warnings
from transformers import pipeline
import pyttsx3

app = Flask(__name__)
CORS(app)  # Add CORS middleware to your Flask app

# Suppressing unnecessary warnings
warnings.simplefilter('ignore')

# Initialize image captioning pipeline
caption = pipeline('image-to-text')

@app.route('/process_image', methods=['POST'])
def process_image():
    # Get the image file path from user input
    file = request.files['image']
    print(file)
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

    # Your image processing logic here
    # For now, let's just return a dummy response
    return jsonify({'message': caption_text})

if __name__ == '__main__':
    app.run(debug=True)
