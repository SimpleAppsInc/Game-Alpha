import sys,time,os

def about():
    generous = 7
    generous_level = ""

    good_person = 7
    personality = ""

    anger = ""
    anger_level = 0

    charisma = ""
    charisma_level = 7

    if good_person <= 5:
        personality = "Bad"
    elif good_person > 5 and good_person <=10:
        personality = "neutural"
    elif good_person > 11 and good_person < 22:
        personality = "Good"
    elif good_person > 23:
        personality = "Very good"
    
    elif anger_level <= 5:
        anger = "Peace"
    elif anger_level > 5 and good_person <=10:
        anger = "Calm"
    elif anger_level > 11 and good_person < 22:
        anger = "Angry"
    elif anger_level > 23:
        anger = "Very angry"
    
    elif charisma_level <= 5:
        charisma = "Non Charisma"
    elif charisma_level > 5 and good_person <=10:
        charisma = "Neutural"
    elif charisma_level > 11 and good_person < 22:
        charisma = "Charismatic"
    elif charisma_level > 23:
        charisma = "Very Charismatic"
    
    elif generous <= 5:
        generous_level = "Not Generous"
    elif generous > 5 and good_person <=10:
        generous_level = "Generous"
    elif generous > 11 and good_person < 22:
        generous_level = "Very Generous"
    elif generous > 23:
        generous_level = "Impressive"

    print("Generous: " + str(generous_level))
    print("Personality: " + str(personality))
    print("Anger: " + str(anger))
    print("Charisma: " + str(charisma))

def writer(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.17)
        else:
            time.sleep(1)
            
def Giris():
    ilk = "You were born in poor family (in 1990). Your father is lumberjack and your mom is house wife. \nSince your family is so poor they have decided to send you to your grandfamily's house to stay with them. \nYou are sad because you missed them a lot. You are crying on your bed and your grandmother heard you while you are crying and sat next to you and wants to talk to you. \n(talk / not talk / yell at her / reject her kindly) \n"
    about()
    writer(ilk)
    choice_one = str(input(">>>> ")).lower()
    if choice_one == "talk":
        print("hello")
        about().anger_level += 7
        about()







health = 1
while health > 0:
    Giris()
    health -= 1
    