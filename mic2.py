import speech_recognition as sr


def speechtext():
    speak2 = sr.Recognizer()
    while True:
        try:

            with sr.Microphone() as m:
                speak2.adjust_for_ambient_noise(m,duration=0.1)
                user = speak2.listen(m)

                usersay = speak2.recognize_google(user)
                usersay = usersay.lower()

                print(usersay)
        except Exception as e:
            print('error',e)

speechtext()