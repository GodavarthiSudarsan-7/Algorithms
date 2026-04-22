import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# TEXT TO SPEECH
def text_to_speech(text):
    print("Text:", text)
    engine.say(text)
    engine.runAndWait()

# SPEECH TO TEXT
def speech_to_text():
    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except:
        print("Could not understand audio")
        return None


# ----------- MAIN PROGRAM -----------

print("Choose input method:")
print("1. Speak")
print("2. Type")

choice = input("Enter choice (1/2): ")

if choice == "1":
    spoken_text = speech_to_text()
elif choice == "2":
    spoken_text = input("Type your message: ")
else:
    print("Invalid choice")
    spoken_text = None

# OUTPUT
if spoken_text:
    text_to_speech("You said " + spoken_text)
else:
    text_to_speech("Sorry, I could not understand you")