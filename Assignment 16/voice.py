import gTTS

def speach(text,name):
    a = gTTS(text)
    a.save(f"assignment 16/{name}.mp3")

t_1 = input("Please 1: ")
t_2 = input("Please 2: ")
t_3 = input("Please 3: ")
name = input("fvoice: ")

if len(t_1) > len(t_2) and len(t_1) > len(t_3):
    speach(text_1,name)

elif len(t_2) > len(t_1) and len(t_2) > len(t_3):
    speach(text_2,name)

elif len(t_3) > len(t_1) and len(t_3) > len(t_2):
    speach(t_3,name)