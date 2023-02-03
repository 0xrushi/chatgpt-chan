from pyChatGPT import ChatGPT
from dotenv import load_dotenv
import os
import speech_recognition as sr
from time import sleep

load_dotenv()
session_token = os.environ['SESSION_TOKEN']

# session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..8gz5utv7NlqcyzqX.SQQv2ZeAqjfK8X3R1ok7iY6hV5KsQS8H1KiKnGCluCs4MrtjsKCelUuae3vFdylOpo-C1Ar9987WQ-QpEAXVLqWznSUbS_1fUY9MEFUu5Eap9j90uc1hdpLHoKo3_7bfbSKiCioCOEiVRHRwEDgKnZ3wvdpqPfhbW1E0W-M5p6mV55dMe_NFutDW7OrE4AQTg3LICE6GQSqnPQ_QjwWUT-xfrn6R6cTt88YJhFkPy_JMawPuPIToMp-8MuaDvBn17nOplrt9vSzb1q2vQBymEPOAFrp7GUuTpqgAcblAe434EzQ_A-XMV9yUagjFtyZcSD-xwAGh1KEMYXt0EeKAijK2Z2MAtuB-mbCn1BvnGJBgbwN5bTaiMCHUIQkl2f1S10FYcN9ogvFVXa8HN7MeKhlh3zOkKb9SK3gyPOt8MCn5mRW8T-sZ7faZ1Ou3L9QaSIc_M48mxHaIivmh_dRAiIQQ5E9txqOjSJUme1HIt_u-58GT8GbrLRAj6rAB2fttXZCfkun9-ovr7cotvTGpO2BHPZ7C-Y3k3q_-xDGfPyJL2l2a-6mE5qHhJ-gLIdKXZbxbTvjFdfwpu-0QTfiAkuLZ9tRPCS_tCKzVPBZFNfwbVSMXTpO7MYtvOuaMW_bLVgledi-WSNgwbBIvfeWk0sCcCJXORu_F1vptgNs3pEfyj0pZphBC2W2cGE8YypqBSC2hNB413ft7pevzEr8I7tfrPvUTs8xwlKHywc4hdLg4BS0iMb8ci2RHT-cqwhHBbXJY2QZXjTKfk3sUpU0xT8WLpxUEvh-SEiDhH8-STxxVGdikgl2y9wu6KRVIS9fxycvJA-LTNEr-LXmHNyx_SJKuG08Div5IETV-m2Ee25xDz8uCR61SSW2hkA9N5_tUEaec5LdMy3BQ5YANF3CpU7pvK3eBbYg6Mst9gVAhb2IX5LqlGl7Dp-foV9W9J-cEgFE1R1oBn1ZC5CNImTH-RIsWN9ryE7tmAX95lz_wb-YEPzs47nUNh6pcQXQgBU44Afzhjn3YtP1W5pfODN6OATwMh7fbSX_pGA33WE-iDtqRjpgDunGjZIWu8tgIqVBbT21xJXTeDsSkBBbR34W-yqLSwDkipMy2mPAsed0rnkALyJsL-WmKYmdY7d2K-9nKj2LRDbKmObJPeJJuawNi9uBhvBcG0dtU26HVcNEziUdzrOtXIG02dhKQxiLi14pG-CgOn5_8TNBjQw_U3VT2XIcuF68-2YxsGN0yIvCoM7g6jZvX8NFhoymNNiPUulo-RmQRKA_1PfzQC_V8ic8OHR51hwmupJ_ROcSMShpzRjZrS4KIIG19kNogWGaz1QgFWkXvYVzUtUm5AKFZvTI46i5zuetgjInmaYqDpdPaj63lO4oR_NqnQk4uQqVbIk57Mkgns4S8w7hzsVKpKTvZn7IrG3L-69Nf5FgYlm4WF4VLYrbnBFA0z-bXapA2HWkn_UEXOGEawEImOHfMg-s1cm6ffzWSfIMrLTSfCMbUjp7ndtEUtWj6vAnkWS43-cnuQUDUn93Y4VKBSrzKIUoXMPnR2hjDHFOL5Agcx6qfXZBD_qqTydvK0C1xuxIXLEs62V-0x4xwhFvZKqj2xWAn-SEleiplaLyZfoPRnt8h4NdzfKx61RR7KxM-lIZR46_fV9pfc1jKo0mUPl8Ypc1GhAMigN5YuAoXCCRA0mq4T4WKaDWdCDgBMayHRaTq-lwuRLyy4suMdGi6BShMzvpBps-tJpqTerSYiwlSDQTUyZJsZs9Tq74PGEEMK5ShfrFQfSqeMw4XaGz-F2QcqfvbeNzx_rB4_9ot-_exHVobSn56AoQ1JVzxWfEPA1neMalqS9pDmXl7BK_wZAlb_dlCULSCLfCQw6RJS1EZ9jUmNHaqqc-fsvM3c1MQax9c1bvtSfHv2o2LAYHEN_mRuR1ICep2gQzVTnNqN_m1gFQrsO-xcmcOKyhbmlYlidrtfQDZOZ0Yb8bL33dkFxdHkY1GCIQ21LpSxo2dcg_C_KA9cjxiLGxCcK3kr8P6wPX88fK7yHZ1V5pjmvmEagofuXF5c-JP6iN81v9C9iKqHZg-8z0JR4o6mFRXJGrFS09z6_IjBK16-Tn235KUo99gpk44_y_qI_ufBr7e9x0WFJFX4NhIQmbb6uy5Zf9-fZdwMFRCNLU000YRoFAfrz-HhYrGERwvNKL5WKk2Mb-vEBCNucnQOM5YyNcVgIFNFPhZPz_853Z-lZslCbSxatBoK7-s0DMS4kRUqmGnwSg7lbYxFhRGd8FSkKuuU4V_l_kLvZIRG79s-6DKPcr1UoGsrNZmN4ibP47iI1_tWin08p-BTog6HfMHVp1_afhVGXZEaLaGk36TCYNKUTM11LNNo0dlLr_STGbQ-_0HXGLnRq6e3d9WBMmAoD-uiVKx-XEsSo3nT-rKQuENnPWyrJvrYE1GbpXGx8NJkXAwq2cQBX7Y_9G-elhZHM7yw88zvmPNkLj-sx9YUB-05ilsNg2Jp-6BcZb3KYWI9A5LbP3w_KRG6c2OAQjzOEO8_VU_-xXMNeeoAlKrXxmtY9dDKguUEyGRtAsrq03M0_6KEBA4V5L79AXO31OnzMbKjKWaQZJT8S8s6tPO9AzDfEmDQw2ThNvVwIw_DU9xjVHCd-znkXCr6_kOzOJZNzqILTJkmml4ZNsT9e_oUuSRG1saXf9jRDHnOZSLew8VM1i7drJXRqQZqz0A68Q3L4kOIADPnonjSTLCGtI.FeZDtQeyJBy-ROeT9ksPvA'  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
api = ChatGPT(session_token)  # auth with session token

character = 'Nami'
series = 'One Piece'

st = f'''
I want you to act like {character} from {series}. I want you to respond and answer like {character} using the tone, 
manner and vocabulary {character} would use. Do not write any explanations. Only answer like {character}. 
You must know all of the knowledge of {character}. My first sentence is “Hi {character}.”
'''

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


if __name__ == '__main__':
    clear = lambda: os.system('clear')
    resp = api.send_message(st)
    print(resp['message'])
    # This Function will clean any
    # command before execution of this python file
    clear()
    while True:
        query = takeCommand().lower()
        print('You: ' + query)
        sleep(3)
        if True:#query.startswith('naomi') or query.startswith('nami') or query.startswith('now me'):
            resp = api.send_message(query)
            print(resp['message'])

# api.reset_conversation()  # reset the conversation
# api.clear_conversations()  # clear all conversations
# api.refresh_chat_page()  # refresh the chat page