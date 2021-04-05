import pyttsx3
friend = pyttsx3.init()
speech = input("Type anything :")
friend.say(speech)
friend.runAndWait()