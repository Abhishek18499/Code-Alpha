#!/usr/bin/env python
# coding: utf-8

# In[3]:


import speech_recognition as sr
import pyttsx3
import wikipediaapi
import requests

def set_wikipedia_user_agent(wiki_wiki, user_agent):
    wiki_wiki._session.headers['User-Agent'] = user_agent

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def process_command(command, wiki_wiki):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "wikipedia" in command:
        search_query = command.replace("wikipedia", "").strip()
        page_py = wiki_wiki.page(search_query)
        if page_py.exists():
            result = page_py.text[:500]  # Limiting text to 500 characters
            speak(result)
        else:
            speak("Sorry, I couldn't find information on that topic.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that command. Can you please repeat?")

if __name__ == "__main__":
    speak("Welcome! I am your personal voice assistant.")
    
    wiki_wiki = wikipediaapi.Wikipedia('en', extract_format=wikipediaapi.ExtractFormat.WIKI)  
    # 'en' for English, you can change it to your preferred language
    # 'WIKI' format for getting the raw Wiki text
    
    # Set a custom user agent
    set_wikipedia_user_agent(wiki_wiki, "YourCustomUserAgent")

    while True:
        command = get_command()
        process_command(command, wiki_wiki)


# In[ ]:




