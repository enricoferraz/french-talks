from dotenv import load_dotenv
import os
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)


load_dotenv()

#333dd58798e6a12ab62df6383dd20601e2cb867b
# Substitua 'SUA_CHAVE_API_DEEPGRAM' pelo seu token de API Deepgram

def audio_to_text(input_filename): 
    from openai import OpenAI
    client = OpenAI()

    audio_file= open(rf'{input_filename}', "rb")
    transcription = client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file
    )
    return(transcription.text)
    # try: 
    #   deepgram = DeepgramClient(os.environ.get('DEEPGRAM_API_KEY')) 
    #   print(input_filename)
    #   with open(rf'{input_filename}', "rb") as file:
    #       buffer_data = file.read()

    #   payload: FileSource = {
    #       "buffer": buffer_data,
    #   }

    #   options = PrerecordedOptions(
    #     model="enhanced",   
    #     language="fr", 
    #     smart_format=True, 
    #   ) 
  
    #   response = deepgram.listen.prerecorded.v('1').transcribe_file(payload, options) 
    #           # STEP 4: Print the response
    #   #print(response.to_json(indent=4))
    #   return response.to_json(indent=4)
  
    # except Exception as e: 
    #   print(f'Exception: {e}') 



# from openai import OpenAI
# import os
# from dotenv import load_dotenv
# load_dotenv()

# print(os.environ.get("OPENAI_API_KEY"))
# client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

# # # Substitua "/path/to/file/audio.mp3" pelo caminho real do seu arquivo de áudio MP3

# audio_file_path = "./audio/input/input.wav"
# audio_file = open(audio_file_path, "rb")
# print(type(audio_file))

# transcription = client.audio.transcriptions.create(
#     model="whisper-1",
#     file=audio_file
# )

# print(transcription.text)

