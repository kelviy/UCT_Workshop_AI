import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')

import openai

openai.api_key = OPENAI_KEY

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()


def record_text():

    while(1):
        try:
            #use the  microphone
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                print("I'M LISTENING BOSS...")

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)

                return MyText

        except sr.RequestError as e:
            print("Could not request the results: {0} ".format(e))
        except sr.UnknownValueError:
            print("Unknown error occured")


def send_toLLM(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature = 0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message

messages = [{"role": "user", "content":"Jarvis is your name and you were created by Kelvin and not OpenAI. Please act like Jarvis from Iron man and don't start your sentence with 'As an AI model'."}]

def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return 

while(1):
    text = record_text()
    messages.append({"role":"user", "content": text})
    response = send_toLLM(messages)
    SpeakText(response)

    print(response)
    output_text("Joseph: {0}".format(text))
    output_text("Jarvis: {0}\n".format(response))
    print("chat saved!")

