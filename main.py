import speech_recognition as sr  
from os import system
import openai

openai.api_key = ('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')
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
   
 # obtain audio from the microphone  
r = sr.Recognizer()  
source = sr.Microphone()

   
def main():
    with source:
        system("say Please wait, calibrating microphone..")
        r.adjust_for_ambient_noise(source, duration=1.5)
        system("say your personal robot companion is now online")
        while True:
            listening = True
            while listening:
                audio = r.listen(source)
                try:
                    message = r.recognize_google(audio)
                    message = message.lower()

                    if "computer" in message:
                        system("say Yes what do you want")
                        listening = False
                except:
                    continue
            takingInput = True
            while takingInput: #make the led go orange
                audio = r.listen(source)
                try:
                    message = r.recognize_google(audio)
                    message = message.lower()
                    message = ("Talk like a human and give me the simplest answers only, "+ message)
                    #make led go red
                    system("say Please wait while i look through my database")
                    if message:
                        messages.append(
                            {"role": "user", "content": message},
                        )
                        chat = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo", messages=messages
                        )
                    reply = chat.choices[0].message.content
                    print(reply)
                    #make led go green
                    system("say According to my database")
                    system('say "{}"'. format(reply))
                    messages.append({"role": "assistant", "content": reply})
                    takingInput = False
                    print(message)
                except:
                    print("no commands given.")
                    takingInput=False

 # recognize speech using Sphinx  

while True:
    main()

#branch testing
#commit to main from beta branch

