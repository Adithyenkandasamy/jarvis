import pyttsx3
import os
import webbrowser as wb
import respond as rs
import take_command as tc
import pyjokes

assis_name = "Jarvis"
boss_name = "gokul"

def tell_jokes():
    joke = pyjokes.get_joke()
    return joke

def respond(text):
    if "hello" in text:
        rs.say("Hi sir")
        rs.say("How can I help you?")
    elif "what is your name" in text:
        rs.say("My name is " + assis_name)
    elif "tell my name" in text:
        rs.say("Your name is " + boss_name)
    elif "how are you" in text:
        rs.say("I am fine")
    elif "who is gokul" in text:
        rs.say("He is your teacher")
    elif "What is my favorite game" in text:
        rs.say("BGMI is your favorite game")
    elif "tell me a joke" in text:
        engine2 = pyttsx3.init()
        voice = engine2.getProperty('voices')
        engine2.setProperty('voice', voice[1].id)
        rate = engine2.getProperty('rate')
        engine2.setProperty('rate', 110)
        engine2.say(tell_jokes())
        engine2.runAndWait()
    elif "play the song Kangal" in text or "play the song kangal" in text:
        rs.say("Sir, let's listen to the song")
        song_path = "/home/kirubha11/Music/Kangal-Edho-MassTamilan.dev.mpga"
        os.system(f"rhythmbox '{song_path}'")
    elif "play the song Asha" in text or "play the song asha" in text:
        rs.say("Sir, let's listen to the song")
        song_path = "/home/kirubha11/Music/Aasa Kooda Sai Abhyankkar 320 Kbps.mpga"
        os.system(f"rhythmbox '{song_path}'")  
    elif "play the song Piravi" in text or "play the song piravi" in text:
        rs.say("Sir, let's listen to the song")
        song_path = "/home/kirubha11/Music/Piravi.mpga"
        os.system(f"rhythmbox '{song_path}'") 
    elif "play the song pirai" in text or "play the song Pirai" in text:
        rs.say("Sir, let's listen to the song")
        song_path = "/home/kirubha11/Music/Pirai-Thedum.mpga"
        os.system(f"rhythmbox '{song_path}'")           
    elif "open calculator" in text:
         rs.say("Opening the calculator")
         os.system('gnome-calculator')
    # elif "close" in text:
    #     text = text.replace("close", "")
    #     if 'Calculator' in text:
    #         os.system("pkill gnome-calculator")
    elif "search" in text:
        rs.say("What do you want to search on YouTube?")
        search_query = tc.takecommand()
        wb.open(f"https://www.youtube.com/results?search_query={search_query}")
        rs.say(f"Searching for {search_query} on YouTube.")

while True:
    rs.say("Say sometging sir")
    text = tc.takecommand()
    print(text)
    respond(text)
