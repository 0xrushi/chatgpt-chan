# ChatGPT-chan

An implementation of [https://www.insider.com/tiktok-programmer-ai-girlfriend-waifu-euthanized-stopped-working-chatgpt-2023-1](https://www.insider.com/tiktok-programmer-ai-girlfriend-waifu-euthanized-stopped-working-chatgpt-2023-1)

🤖 ChatGPT chan is an open-source collection of tools to have your own personal assistant in your projects. With this, you can leverage the power of OpenAI's ChatGPT language model to build conversational interfaces, automate tasks, and more. The library provides a simple API for integrating voice assistant into your projects, making it easy for developers to add AI capabilities to their applications. 

## Demo 
[https://odysee.com/@rushi:2/chatgptchandemo2:4](https://odysee.com/@rushi:2/chatgptchandemo2:4)

### Requirements:
- Python39
- Docker

## Setup:

### 1) Emotion Classifier (can be hosted on a different server)

```
git clone https://github.com/mmabrouk/chatgpt-wrapper.git

cd chatgpt-wrapper/emotion_detection

docker build -t emotion_detector .

docker run --rm -it --host net --gpus all emotion_detector
```


### 2) Stable Diffusion model (Optional, can be hosted on a different server)

```
git clone https://github.com/mmabrouk/chatgpt-wrapper.git

cd chatgpt-wrapper/diffusion_model

pip install transformers

# generate a huggingface token
huggingface-cli login

# move that token to `diffusion_model/`

sh build.sh

sh run.sh
```
My usecase is to host on raspberry pi's, the `run.sh` will start a webserver on port 8088, and A GET request with a text prompt like 

```
http://127.0.0.1:8088/?prompt=panda eating ice cream
```

To reduce the time lag, the images have been cached to `chatgptpy/anime_expressions` categorized by emotions

### 3) ChatGPT wrapper

This includes image slideshow, cached stable diffusion expressions, text to speech, speech to text, chatgpt unofficial api

```
git clone https://github.com/mmabrouk/chatgpt-wrapper.git

cd chatgpt-wrapper/chatgptpy

```

Register for azure neural tts api [here](https://azure.microsoft.com/en-us/products/cognitive-services/text-to-speech/#features)

put the keys and region in `~/.bashrc`

```
SPEECH_KEY=<aws_speech_key>
SPEECH_REGION=<azure_region>
```

`source ~/.bashrc`


Fire up the emotion_detection server and the optional stable diffusion server from steps 1 and 2

map the IPs in `chatgptpy/main.py`

```
EMOTION_DETECTION_IP='http://127.0.0.1:5004'
STABLE_DIFFUSION_IP='http://127.0.0.1:8088'
```

```
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

pip install git+https://github.com/mmabrouk/chatgpt-wrapper

python main.py
```

### Current issues 

- Chatgpt wrapper fails sometimes, and we need to switch to some other implementation of chatgpt API and this process goes on
  
- The `chatgpt-wrapper`  uses `playwright`, Docker implementation of which seems challenging
## Credits
- [chatgpt-wrapper](https://github.com/mmabrouk/chatgpt-wrapper), [pyChatGPT](https://github.com/terry3041/pyChatGPT), [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) for unofficial ChatGPT API

- [stable-diffusion](https://github.com/CompVis/stable-diffusion)  

- [Azure Cognitive services](https://azure.microsoft.com/en-us/products/cognitive-services/text-to-speech/#overview)

- [michellejieli](https://huggingface.co/michellejieli/emotion_text_classifier) for emotion_text_classifier

- [OpenAI](https://openai.com/) for creating [ChatGPT](https://openai.com/blog/chatgpt/) 🔥