import speech_recognition
import pyttsx3
import pyaudio


class SpeechAudio:
    text = ""

    def __int__(self):
        print('speech object created')

    def activate_voice_control(self):
        required = -1
        for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
#            print(str(index)+':'+str(name))

            if "WI-XB400" in name:
                required = index

        print('required index : '+ str(required))
        recognizer = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone(device_index = required) as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                audio = recognizer.listen(mic)
                self.text = recognizer.recognize_google(audio)
                self.text = self.text.lower()
                return self.text

        except :
            recognizer = speech_recognition.Recognizer()


# speech = SpeechAudio()
# print('from function::'+speech.activate_voice_control())