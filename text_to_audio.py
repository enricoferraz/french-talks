import requests
from dotenv import load_dotenv
import os


load_dotenv()


from pathlib import Path
from openai import OpenAI

def text_to_audio(chat_output):
    client = OpenAI()


    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=chat_output
    )
    filename = "./audio/output/output_file.mp3"
    response.stream_to_file(filename)
    return filename

# def text_to_audio(chat_output):
#     # Set your Deepgram API key


#     # Define the API endpoint
#     url = "https://api.deepgram.com/v1/speak?model=aura-asteria-en"

#     # Define the headers
#     headers = {
#         "Authorization": f"Token {os.environ.get('DEEPGRAM_API_KEY')}",
#         "Content-Type": "application/json"
#     }

#     # Define the payload
#     payload = {
#         "text": chat_output
#     }

#     # Make the POST request
#     response = requests.post(url, headers=headers, json=payload)

#     filename = "./audio/output/output_file.mp3"
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Save the response content to a file
#         with open(filename, "wb") as f:
#             f.write(response.content)
#         print("File saved successfully.")
#         return filename
#     else:
#         print(f"Error: {response.status_code} - {response.text}")


