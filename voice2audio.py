import speech_recognition as sr
from gtts import gTTS
import os

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")

# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
try:
    # using google speech recognition
    print("Text: "+r.recognize_google(audio_text))
    response_text = r.recognize_google(audio_text)
except:
     print("Sorry, I did not get that")
     response_text = "Sorry, I did not get that"

# Generate speech from the response text
tts = gTTS(response_text)

# Save the speech to a file
tts.save("response.mp3")

# Play the speech
os.system("mpg321 response.mp3")
