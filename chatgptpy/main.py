# from pyChatGPT import ChatGPT
from dotenv import load_dotenv
import os
import speech_recognition as sr
from time import sleep
import requests
import json
from animetts.speech_synthesis import synthesize_ssml
import sounddevice as sd
import soundfile as sf
from utils.imageplayer import show_slideshow
from utils.stablediffusion import dictionary_of_image_paths, get_random_image

EMOTION_DETECTION_IP='http://127.0.0.1:5004'
STABLE_DIFFUSION_IP='http://127.0.0.1:8088'

load_dotenv()

# session token of chatgpt firefox inspect element
# session_token = os.environ['SESSION_TOKEN']

session_token = ''
# api = ChatGPT(session_token)  # auth with session token

character = 'Nami'
series = 'One Piece'

st = f'''
I want you to act like {character} from {series}. I want you to respond and answer like {character} using the tone, 
manner and vocabulary {character} would use. Do not write any explanations. Only answer like {character}. 
You must know all of the knowledge of {character}. My first sentence is “Hi {character}.”
'''

from chatgpt_wrapper import ChatGPT
bot = ChatGPT()
response = bot.ask(st)
# print(response)  # prints the response from chatGPT

# speech to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
    return query

def send_emotion_detect(text):
    url = EMOTION_DETECTION_IP + "/detect"
    payload = {"text": text}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    map_emotion = {'anger': 'Angry', 'disgust':'Unfriendly', 'fear':'Terrified', 'joy':'Cheerful', 'sadness':'Sad', 'surprise':'Excited', 'neutral':'Chat'}
    # anger disgust fear joy sadness surprise
    if response.status_code == 200:
        # print(response.json())
        return map_emotion[response.json()[0]['label']]

    else:
        # neutral
        return "Chat"
    
    
def generate_xml(message, style):
    xml = f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">\n'
    xml += f'    <voice name="en-US-JaneNeural">\n'
    xml += f'        <mstts:express-as style="{style}">\n'
    xml += f'            {message}\n'
    xml += f'        </mstts:express-as>\n'
    xml += f'    </voice>\n'
    xml += f'</speak>'
    return xml
   
if __name__ == '__main__':
    clear = lambda: os.system('clear')
    #resp = api.send_message(st)
    #print(resp['message'])
    # This Function will clean any
    # command before execution of this python file
    clear()
    while True:
        query = takeCommand().lower()
        print('You: ' + query)
        sleep(3)
        if True:#query.startswith('naomi') or query.startswith('nami') or query.startswith('now me'):
            #resp = api.send_message(query)
            #message = resp['message']
            message = bot.ask(query)
            style = send_emotion_detect(message)

            imagedict = dictionary_of_image_paths()
            random_styled_image_list = imagedict[style]
            random_styled_image = get_random_image(random_styled_image_list)

            show_slideshow(random_styled_image)

            xml_content = generate_xml(message, style)

            with open("ssml.xml", "w") as file:
                file.write(xml_content)
            ssml_file_path = os.path.abspath("ssml.xml")

            # Synthesize the SSML
            wav_file = synthesize_ssml(ssml_file_path)

            data, fs = sf.read(wav_file, dtype='int16')
            sd.play(data, fs)
            status = sd.wait()


# api.reset_conversation()  # reset the conversation
# api.clear_conversations()  # clear all conversations
# api.refresh_chat_page()  # refresh the chat page