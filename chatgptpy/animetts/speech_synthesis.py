import os
import azure.cognitiveservices.speech as speechsdk

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name='en-US-JaneNeural'
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

def synthesize_ssml(ssml_file):
    ssml_string = open(ssml_file, "r").read()

    # Synthesize the SSML
    print("SSML to synthesize: \r\n{}".format(ssml_string))
    speech_synthesis_result = synthesizer.speak_ssml_async(ssml_string).get()
    stream = speechsdk.AudioDataStream(speech_synthesis_result)
    stream.save_to_wav_file("file.wav")

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("SynthesizingAudioCompleted result")
        return os.path.abspath("file.wav")
    
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        os.remove("file.wav")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
        return None
synthesize_ssml("ssml.xml")