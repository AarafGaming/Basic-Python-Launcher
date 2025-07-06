import subprocess
import webbrowser
print("What do you want to launch?")
userinput = input()
if userinput == "Minecraft":

    subprocess.Popen(['start', 'Minecraft.bat'], shell=True)
if userinput == "Roblox":
    print("PlaceID of the game you want to play?")
    protocol = "roblox://placeId="
    placeid = input()
    webbrowser.open(protocol + placeid)
if userinput == "Website":
input = input()
    webbrowser.open(input)
if userinput == "Rocket League":
 webbrowser.open("com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch&silent=true")
if userinput == "Among Us":
 webbrowser.open("steam://rungameid/945360")
if userinput == "Stumble Guys":
    webbrowser.open("steam://rungameid/1343400")
if userinput == "Fall Guys":
    webbrowser.open("com.epicgames.launcher://apps/50118b7f954e450f8823df1614b24e80%3A38ec4849ea4f4de6aa7b6fb0f2d278e1%3A0a2d9f6403244d12969e11da6713137b?action=launch&silent=true")
