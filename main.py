from gtts import gTTS
import os
import webbrowser as wb
import pyautogui
import take_command as tc
import date_time as dt

assis_name = "Jarvis"
boss_name = "gokul"

# Function to use Google Text-to-Speech (gTTS) for speech output
def say(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("mpg123 response.mp3")
    os.remove("response.mp3")  # Clean up the audio file after playing

def respond(text):
    if "hello" in text:
        say(dt.wishing())
        say("How can I help you?")
    elif "what is your name" in text:
        say("My name is " + assis_name)
    elif "tell my name" in text:
        say("Your name is " + boss_name)
    elif "how are you" in text:
        say("I am fine")
    elif "who is gokul" in text:
        say("He is your teacher")
    elif "instagram" in text or "Instagram" in text:
        say("Sir, let's open Instagram")
        wb.open("https://www.instagram.com")   
    elif "github" in text or "Github" in text:
        say("Sir, let's open GitHub")
        wb.open("https://www.github.com")         
    elif "chatgpt" in text or "Chatgpt" in text:
        say("Sir, let's open ChatGPT")
        wb.open("https://chatgpt.com")    
    elif "what is my favorite game" in text:
        say("BGMI is your favorite game")
    elif "tell me a joke" in text:
        say(tell_jokes())
    
    elif "open calculator" in text:
        say("Opening the calculator")
        os.system('gnome-calculator')
    elif "search" in text:
        say("Where do you want to search?")
        What_search = tc.takecommand().lower()
        if "youtube" in What_search:
            say("What do you want to search on YouTube?")
            search_query = tc.takecommand()
            say(f"Searching for {search_query} on YouTube.")
            wb.open(f"https://www.youtube.com/results?search_query={search_query}")
            say("Do you want to control the video? Say a command like play, pause, mute, or stop.")
            while True:
                control_command = tc.takecommand().lower()
                if "play the video" in control_command or "pause the video" in control_command:
                    say("Toggling play/pause on the video.")
                    pyautogui.press('space')
                elif "mute the video" in control_command:
                    say("Muting the video.")
                    pyautogui.press('m')
                elif "unmute the video" in control_command:
                    say("Unmuting the video.")
                    pyautogui.press('m')
                elif "full screen" in control_command:
                    say("Toggling full screen.")
                    pyautogui.press('f')
                elif "volume up" in control_command:
                    say("Increasing volume.")
                    pyautogui.press('up')
                elif "volume down" in control_command:
                    say("Decreasing volume.")
                    pyautogui.press('down')
                elif "rewind" in control_command:
                    say("Rewinding the video.")
                    pyautogui.press('left')
                elif "fast forward" in control_command:
                    say("Fast forwarding the video.")
                    pyautogui.press('right')
                elif "stop" in control_command or "exit" in control_command:
                    say("Exiting YouTube control mode.")
                    break
                else:
                    say("Sorry, I didn't understand that command.")
        elif "google" in What_search:
            say("What do you want to search on google?")
            search_query = tc.takecommand()
            say(f"Searching for {search_query} on google.")
            wb.open(f"https://www.google.com/search?q={search_query}")
        
    elif "shutdown the computer" in text:
        say("Shutting down the computer.")
        os.system('shutdown now')
    elif "restart the computer" in text:
        say("Restarting the computer.")
        os.system('reboot')
    elif "logout" in text:
        say("Logging out.")
        os.system('gnome-session-quit --logout --no-prompt')
    elif "lock the computer" in text:
        say("Locking the computer.")
        os.system('gnome-screensaver-command -l')
    elif "open firefox" in text:
        say("Opening Firefox.")
        os.system('firefox')
    elif "open terminal" in text:
        say("Opening Terminal.")
        os.system('gnome-terminal')
    elif "open chrome" in text:
        say("Opening Chrome.")
        os.system('google-chrome')  
    elif "Bye" in text or "bhai" in text:
        say("Bye sir, have a good day.")
        exit()

while True:
    say("Say something, sir")
    text = tc.takecommand()
    print(text)
    respond(text)
