# importing speech recognition package from google api
import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import wolframalpha  # to calculate strings into formula
from selenium import webdriver  # to control browser operations
import re
import requests

num = 1


def assistant_speaks(output):
    global num

    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    print("PerSon : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    # saving the audio file given by google text to speech
    file = str(num)+".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)


def process_text(input):
    try:
        if 'search' in input or 'play' in input:
            # a basic web crawler using selenium
            search_web(input)
            return

        if "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am Khushi. Your personal Assistant. 
			I am here to make your life easier. You can command me to perform 
			various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak)
            return

        if "tell me a joke" in input:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept": "application/json"}
            )
            if res.status_code == requests.codes.ok:
                assistant_speaks(str(res.json()['joke']))
            else:
                assistant_speaks('oops!I ran out of jokes')

        if "calculate" in input.lower():

            # write your wolframalpha app_id here
            app_id = "WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return

        if 'open' in input:

            # another function to open
            # different application availaible
            open_application(input.lower())
            return

        if "khushi" in input:
            assistant_speaks("hello, how can i help?")

        if "hey" in input:
            assistant_speaks("hi dear, how can i help?")

        if "how are you" in input:
            assistant_speaks("I am fine")

        if "what is your boss name" in input:
            assistant_speaks("oh wow!,he is great,i'am proud to say his name as a god for me?")

        if "what is your age" in input:
            assistant_speaks("I'm new here in this world about half of age")

        if "tell me about your country" in input:
            assistant_speaks("nepal,country where the mount Everest lies, where lord buddha was born")

        if "where are you now" in input:
	assistant_speaks(" now i am in capital of our country, kathmandu")

	if "

        # if "note" in input:
        #     write = 1
        #         data = recordAudio("Writing...")
        #         write = writeNote(data, 'note')

        if "ok quit" in input:
            assistant_speaks("Bye "+user_name+".")
            return 0

        if "what time is it" in input:
            assistant_speaks(ctime())

        if "where is" in input:
            data = data.split(" ")
            location = data[2]
            assistant_speaks("Hold on "+user_name +
                            ", I will show you where " + location + " is.")
            os.system("google-chrome https://www.google.nl/maps/place/" +
                    location + "/&amp;")

        if 'open reddit' in input:
        #     while write:
            reg_ex = re.search('open reddit (.*)', data)
            url = 'https://www.reddit.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            os.system("google-chrome " + url + "/")
            print('Done!')

        if 'open website' in input:
            reg_ex = re.search('open website (.+)', data)
            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.' + domain
                os.system("google-chrome " + url + "/")
                print('Done!')
            else:
                pass

        if 'what\'s up' in input:
            assistant_speaks('Just doing my thing')

        if 'tell me a joke' in input:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept": "application/json"}
            )
            if res.status_code == requests.codes.ok:
                assistant_speaks(str(res.json()['joke']) + "HAHA")
            else:
                assistant_speaks('oops!I ran out of jokes')

        if 'tell me another joke' in input:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept": "application/json"}
            )
            if res.status_code == requests.codes.ok:
                assistant_speaks(str(res.json()['joke']) + "HAHA")
            else:
                assistant_speaks('oops!I ran out of jokes')

        else:
            assistant_speaks(
                "I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except:

        assistant_speaks(
            "I don't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)


def search_web(input):

    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in input.lower():

        assistant_speaks("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get(
            "http://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():

        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:

        if 'google' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        else:

            driver.get("https://www.google.com/search?q =" +
                       '+'.join(input.split()))

        return


# function used to open application
# present inside the system.
def open_application(input):

    # if "chrome" in input:
    # 	assistant_speaks("Google Chrome")
    # 	os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    # 	return

    # elif "firefox" in input or "mozilla" in input:
    # 	assistant_speaks("Opening Mozilla Firefox")
    # 	os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
    # 	return

    # elif "word" in input:
    # 	assistant_speaks("Opening Microsoft Word")
    # 	os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
    # 	return

    # elif "excel" in input:
    # 	assistant_speaks("Opening Microsoft Excel")
    # 	os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
    # 	return

    # else:

    assistant_speaks("Application not available")
    return


def get_audio():

    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=4)
    print("Stop.")  # limit 5 secs

    try:

        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text

    except:

        assistant_speaks("PLease try again !")
        return 0


#    def writeNote(data, _type):

#     if 'stop writing' in data:
#         print("Writing stoped")
#         return 0

#     if 'note' in _type:
#         print("Opening Note...")
#         f = open("note.txt", "a+")
#         f.write(""+data+"\r\n")

#     return 1


# Driver Code
if __name__ == "__main__":
    # assistant_speaks("What's your name, Human?")
    name = 'Human'
    # name = get_audio()
    # assistant_speaks("Hello, " + name + '.')

    while(1):

        assistant_speaks("What can i do for you?")
        text = get_audio()

        if text == 0:
            continue

        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye, " + name+'.')
            break

        # calling process text to process the query
        process_text(text)
