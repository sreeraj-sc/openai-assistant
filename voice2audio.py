import speech_recognition as sr
from gtts import gTTS
import os
import openai

# Set up OpenAI API client
openai.api_key = "YOUR_API_KEY"

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
    print("You said: "+r.recognize_google(audio_text))
    input_text = r.recognize_google(audio_text)
except:
     print("Sorry, I did not get that")
     input_text = "Sorry, I did not get that"

# Use OpenAI API to generate a response to the input text
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=input_text,
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0.5,
)

# Get the generated response text
response_text = response["choices"][0]["text"].strip()

# Generate speech from the response text
tts = gTTS(response_text)

# Save the speech to a file
tts.save("response.mp3")

# Play the speech
os.system("mpg321 response.mp3")
