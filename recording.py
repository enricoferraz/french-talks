import pyaudio
import wave

CHUNK = 1024  # Número de frames por bloco
FORMAT = pyaudio.paInt16  # Formato de áudio (16 bits PCM)
CHANNELS = 1  # Número de canais (1 para mono, 2 para estéreo)
RATE = 44100  # Taxa de amostragem (número de frames por segundo)
RECORD_SECONDS = 15  # Duração da gravação em segundos
WAVE_OUTPUT_FILENAME = "./audio/input/input.wav"  # Nome do arquivo de saída WAV

def recording():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Gravando...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Gravação concluída.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Salvar a gravação em um arquivo WAV
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return WAVE_OUTPUT_FILENAME
