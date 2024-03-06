from recording import recording
from audio_to_text import audio_to_text

from conversation import chat
import json

from text_to_audio import text_to_audio
from broadcasting import play_mp3


while True:
    input_filename = recording()

    user_input_text = audio_to_text(input_filename)
    print(f"Human: {user_input_text}")
    # Convert the JSON string to a Python dictionary
    #user_input_text = json.loads(user_input_text)
    
    #user_input_text_final = user_input_text['results']['channels'][0]['alternatives'][0]['transcript']

    chat_output = chat(user_input_text)

    filename = text_to_audio(chat_output)
    play_mp3(file_path=filename)