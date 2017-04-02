import speech_recognition as sr


def active_listen():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        audio = r.listen(src)
    msg = ''
    try:
        msg = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google STT; {0}".format(e))
    except:
        print("Unknown exception occurred!")
    finally:
        return msg.lower()
