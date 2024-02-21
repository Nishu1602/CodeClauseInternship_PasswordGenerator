from gtts import gTTS
import time
import os
import playsound
import pygame
print(time.ctime())
tts=gTTS("What is the cost of lies?", lang='en')
a='ok.mp3'
tts.save(a)
playsound.playsound(a)
os.remove(a)

# Initialize pygame
pygame.init()

# Load the audio file
pygame.mixer.music.load('ok.mp3')

# Play the audio file
pygame.mixer.music.play()

# Wait for the audio to finish playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Clean up
pygame.quit()
