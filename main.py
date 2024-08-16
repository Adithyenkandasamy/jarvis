import pyttsx3
import os
import webbrowser as wb
import pyautogui
import respond as rs
import take_command as tc
import pyjokes
import date_time as dt

assis_name = "Jarvis"
boss_name = "gokul"

def tell_jokes():
    joke = pyjokes.get_joke()
    return joke


def respond(text):
    if "hello" in text:
        rs.say(dt.wishing())
        rs.say("How can I help you?")
    elif "what is your name" in text:
        rs.say("My name is " + assis_name)
    elif "tell my name" in text:
        rs.say("Your name is " + boss_name)
    elif "how are you" in text:
        rs.say("I am fine")
    elif "who is gokul" in text:
        rs.say("He is your teacher")
    elif "instagram" in text or "Instagram" in text:
        rs.say("Sir, let's open Instagram")
        wb.open("https://www.instagram.com")   
    elif "github" in text or "Github" in text:
        rs.say("Sir, let's open GitHub")
        wb.open("https://www.github.com")         
    elif "chatgpt" in text or "Chatgpt" in text:
        rs.say("Sir, let's open ChatGPT")
        wb.open("https://chatgpt.com")    
    elif "what is my favorite game" in text:
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
    elif "play the song Asha" in text or "play the song asha" in text or "Asa" in text or "asa" in text:
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
    elif "search" in text:
        rs.say("What do you want to search on YouTube?")
        search_query = tc.takecommand()
        rs.say(f"Searching for {search_query} on YouTube.")
        wb.open(f"https://www.youtube.com/results?search_query={search_query}")
        rs.say("Do you want to control the video? Say a command like play, pause, mute, or stop.")
        
        # Adding YouTube playback control commands
        while True:
            control_command = tc.takecommand().lower()
            if "play the video" in control_command or "pause the video" in control_command:
                rs.say("Toggling play/pause on the video.")
                pyautogui.press('space')
            elif "mute the video" in control_command:
                rs.say("Muting the video.")
                pyautogui.press('m')
            elif "unmute the video" in control_command:
                rs.say("Unmuting the video.")
                pyautogui.press('m')
            elif "full screen" in control_command:
                rs.say("Toggling full screen.")
                pyautogui.press('f')
            elif "volume up" in control_command:
                rs.say("Increasing volume.")
                pyautogui.press('up')
            elif "volume down" in control_command:
                rs.say("Decreasing volume.")
                pyautogui.press('down')
            elif "rewind" in control_command:
                rs.say("Rewinding the video.")
                pyautogui.press('left')
            elif "fast forward" in control_command:
                rs.say("Fast forwarding the video.")
                pyautogui.press('right')
            elif "stop" in control_command or "exit" in control_command:
                rs.say("Exiting YouTube control mode.")
                break
            else:
                rs.say("Sorry, I didn't understand that command.")
    elif "shutdown the computer" in text:
        rs.say("Shutting down the computer.")
        os.system('shutdown now')
    elif "restart the computer" in text:
        rs.say("Restarting the computer.")
        os.system('reboot')
    elif "logout" in text:
        rs.say("Logging out.")
        os.system('gnome-session-quit --logout --no-prompt')
    elif "lock the computer" in text:
        rs.say("Locking the computer.")
        os.system('gnome-screensaver-command -l')
    elif "open firefox" in text:
        rs.say("Opening Firefox.")
        os.system('firefox')
    elif "open terminal" in text:
        rs.say("Opening Terminal.")
        os.system('gnome-terminal')
    elif "open chrome" in text:
        rs.say("Opening Chrome.")
        os.system('google-chrome')  
    elif "Bye" in text or "bhai" in text:
        rs.say("Bye sir, have a good day.")
        exit()
 

while True:
    rs.say("Say something, sir")
    text = tc.takecommand()
    print(text)
    respond(text)
  