import pygame

def play_mp3(file_path):
    pygame.init()
    pygame.mixer.init()
    print(file_path)
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        pygame.mixer.quit()

