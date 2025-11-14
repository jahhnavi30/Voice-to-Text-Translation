import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Speak something...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand.")
    except sr.RequestError:
        print("Could not connect to recognition service.")
