import pyttsx3 as tts
import speech_recognition as sr

endings = ("or", "er", "ur")

r = sr.Recognizer()

while True:
    engine = tts.init()
    with sr.Microphone() as source:
        print("Say something > ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
        except:
            print("There was an error with transcribing that audio")

    words = text.split()
    print(words)

    for word in words:
        if word.endswith(endings) and  len(word) >= 5:
            response = word[:-2] + " her, I barely even knew her!"
            engine.say(response)
            engine.runAndWait()
