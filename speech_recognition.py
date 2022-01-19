import speech_recognition
import pyttsx3
import simpleaudio as sa


recognizer = speech_recognition.Recognizer()


while True:

    try:

        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio,language="de")
            #text = recognizer.recognize_sphinx(audio,language="de")
            text = text.lower()

            word = "hallo eve"

            guess_is_correct = text == word.lower()

            if guess_is_correct:
                print("Moin")
                wave_obj = sa.WaveObject.from_wave_file("") #Put your .wav path here
                play_obj = wave_obj.play()
                play_obj.wait_done()
                

            print(f"Recognized {text}")
    
    except speech_recognition.UnknownValueError():

        print("Fail")

        recognizer = speech_recognition.Recognizer()

        print("Geht aber weiter")
        continue
        
