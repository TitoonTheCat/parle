# Attention, si on a une erreur du style "sh: 1: mpg321: not found"
# il faut installer le programme mpg321 avec la ligne de code dessous
# sudo apt install mpg321

# et il est imperatif d'installer le paquet gTTS (Google Text-to-Speech) avec "pip install gTTS

from gtts import gTTS
import os

# Texte à prononcer
text = 'Bonjour Stéphanie, je suis un exemple de synthèse vocale en français et je peux maintenant faire des dictées de mots si besoin à Marine et Maelle.'

# Création du fichier audio
tts = gTTS(text=text, lang='fr')
tts.save("hello.mp3")

# Lecture du fichier audio
os.system("mpg321 hello.mp3")
