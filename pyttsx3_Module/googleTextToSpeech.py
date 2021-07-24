__copyright__ = "Copyright (C) 2021"
__version__ = "1.0"

"""
Package installation prerequisite
pip install gTTS
pip install playsound

Ref. 24Source : 
https://gtts.readthedocs.io/en/latest/index.html 
https://github.com/TaylorSMarks/playsound
"""
from gtts import gTTS
from playsound import playsound

# User input text you can give
tts = gTTS('Johny, Johny,'
'Yes papa?'\
'Eating sugar?'\
'No papa.'\
'Telling lies?'\
'No papa.'\
'Open your mouth.'\
'Ha ha ha!', lang='en')

# create "voice_english.mp3" file and Save in current directory 
tts.save("voice_english.mp3")

#play stored "voice_english.mp3" file using playsound module
playsound("voice_english.mp3")
