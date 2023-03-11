from gtts import gTTS
ts = gTTS(input('enter the words: '))
ts.save(input('file name: '))
