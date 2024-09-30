import speech_recognition
import pyttsx3

nc=''
def speech_to_text():
    global nc
    Recognizer = speech_recognition.Recognizer()
    try:
        engine = pyttsx3.init()
        with speech_recognition.Microphone() as mic:
            engine.say('Speak'),print('Speak'),engine.runAndWait(),print('-->',end="")
            Recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = Recognizer.listen(mic)
            text = Recognizer.recognize_google(audio)
            text = text.lower()
            print(text)
    except speech_recognition.UnknownValueError:
        print("Voice is not clear")
        nc="not clear"

    if nc!="not clear":
        try:
            engine = pyttsx3.init()
            t=text.split()
            if t[0] in ["turn","tone","tod","don"]:
                a=[t[1],t[3]]
                c=" ".join(a)
                print('-->',c)

                full=["11","15","19","23","27","31","43","47","51","55","9","13","17","21","25","29","41","45","49","53"]

                full1={"11":["on one","onn one","oon one","on 1","onn 1","oon 1"],"15":["on to","onn to","oon to","on two","onn two","oon two","on 2","onn 2","oon 2","on tu","onn tu","oon tu"]
                       ,"19":["on three","onn three","oon three","on 3","onn 3","oon 3"],"23":["on four","onn four","oon four","on 4","onn 4","oon 4"]
                       ,"27":["on five","onn five","oon five","on 5","onn 5","oon 5"],"31":["on six","onn six","oon six","on sex","onn sex","oon sex","on 6","onn 6","oon 6"]
                       ,"43":["on seven","onn seven","oon seven","on 7","onn 7","oon 7"],"47":["on eight","onn eight","oon eight","on 8","onn 8","oon 8"]
                       ,"51":["on nine","onn nine","oon nine","on 9","onn 9","oon 9"],"55":["on ten","onn ten","oon ten","on 10","onn 10","oon 10"]
                       ,"9":["of one","off one","oof one","of 1","off 1","oof 1"],"13":["of to","off to","oof to","of two","off two","oof two","of 2","off 2","oof 2","of tu","off tu","oof tu"]
                       ,"17":["of three","off three","oof three","of 3","off 3","oof 3"],"21":["of four","off four","oof four","of 4","off 4","oof 4"]
                       ,"25":["of five","off five","oof five","of 5","off 5","oof 5"],"29":["of six","off six","oof six","of sex","off sex","oof sex","of 6","off 6","oof 6"]
                       ,"41":["of seven","off seven","oof seven","of 7","off 7","oof 7"],"45":["of eight","off eight","oof eight","of 8","off 8","oof 8"]
                       ,"49":["of nine","off nine","oof nine","of 9","off 9","oof 9"],"53":["of ten","off ten","oof ten","of 10","off 10","oof 10"]}
                if a[0] in ["on","onn","oon","On","Onn","Oon","ON","ONn","OOn","ONN","OON"]:
                    engine.say('turning on {}'.format(a[1]))
                    engine.runAndWait()
                elif a[0] in ["of","off","oof","Of","Off","Oof","OF","OFf","OOf","OFF","OOF"]:
                    engine.say('turning off {}'.format(a[1]))
                    engine.runAndWait()
                for i in full:
                    if c in full1[i]:
                        return i
                    else:
                        return "0"
                else:
                    return "0"
            else:
                return "0"
        except (IndexError,AttributeError):
            print("")
    else:
        return "0"
