#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from PIL import Image, ImageFont, ImageDraw
import re

usersDir = 'C:\\Users\\'
savedGamesDir = "\\Saved Games\\DCS\\Config\\Input\\"

def getUsers(): 
    try:
        usersDirList = os.listdir(usersDir)
        users = []
        for i in usersDirList:
            userDir = usersDir + i
            if os.path.isdir(userDir):
                users.append(i)
        return users
    except Exception as e:
        print(f"Error accessing directories. {e}")
        return []

def getUserSelection(users):
    print("Select your user profile below.")
    for index, user in enumerate(users, start=1):
        print(f"{index}. {user}")
    choice = int(input("Enter the number associated with your profile: "))
    while True: 
        if 1 <= choice <= len(users):
                return users[choice - 1]
        else:
            choice = int(input("Invalid choice. Please try again: "))

def getModules(user):
    try:
        moduleDirList = os.listdir(usersDir + user + savedGamesDir)
        modules = []
        for i in moduleDirList:
            moduleDir = usersDir + user + savedGamesDir + i
            if os.path.isdir(moduleDir):
                modules.append(i)
        return modules
    except Exception as e:
        print(f"Error accessing directories. {e}")
        return []

def getModuleSelection(modules):
    print("Select your desired module below.")
    for index, module in enumerate(modules, start=1):
        print(f"{index}. {module}")
    choice = input("Enter the number associated with your module (Leave blank for all): ")
    
    while True:
        if choice.strip() == "":
            return modules
        try:
            choice = int(choice)
            if 1 <= choice <= len(modules):
                module = [modules[choice - 1]]
                return module
            else:
                choice = input("Invalid choice. Please try again: ")
        except ValueError:
            choice = input("Invalid input. Please enter a number: ")

def getAllDevices(user):
    devices = []
    for module in os.listdir(usersDir + user + savedGamesDir):
        print(usersDir + user + savedGamesDir + module)
        if os.path.isdir(usersDir + user + savedGamesDir + module):
            for device in os.listdir(usersDir + user + savedGamesDir + module + "\joystick\\"):
                devices.append(device)
    noduplicatedevices = set(devices)
    return noduplicatedevices

def getSavedDevices(user, module):
    savedDevices = []
    if type(module) == list:
        if len(module) > 1:
            try:
                savedDevices = getAllDevices(user)
                devices = []
                for i in savedDevices:
                    if i.endswith(".lua"):
                        devices.append(i)
                return devices
            except Exception as e:
                print(f"Error accessing directories. {e}")
                return []
        else: 
            try:
                module = module[0]
                savedDevices = os.listdir(usersDir + user + savedGamesDir + module + "\joystick\\")
                devices = []
                for i in savedDevices:
                    if i.endswith(".lua"):
                        devices.append(i)
                return devices
            except Exception as e:
                print(f"Error accessing directories. {e}")
                return []
    

def getDeviceSelection(user, devices):
    print("Select your desired devices below. If you wish to select multiple devices, deliminate them with a comma and a space. e.g. 1, 3, 5...")
    for index, device in enumerate(devices, start=1):
        print(f"{index}. {device}")
    try:
        choice = input("Enter the number(s) associated with your device(s): ")
        choices = [int(i.strip()) for i in choice.split(",")]
    except ValueError as e:
        print(f"Invalid input. Please enter only numbers separated by commas. Error: {e}")
    selectedDevices = []
    for i in choices: 
        i = i-1
        selectedDevices.append(devices[i])
    return selectedDevices

def createDevicesFrameworks(selectedDevices):
    frameworks = {}
    #POR stands for point of reference. Add or remove 53 or 144 from the point of reference to get the adjacent points. 
    for device in selectedDevices:
        frameworks[device] = {}
        if device.startswith("VPC MongoosT-50CM3"):
            print(f"Generating Device Framework from {device}")
            text_boxes = {
                "JOY_BTN1": (76, 172, 100, 34), #POR
                "JOY_BTN2": (76, 119, 100, 34),
                "JOY_BTN3": (76, 225, 100, 34),
                "JOY_BTN4": (76, 323, 100, 34), 
                "JOY_BTN5": (220, 429, 100, 34),
                "JOY_BTN6": (220, 376, 100, 34), #POR
                "JOY_BTN7": (220, 323, 100, 34),
                "JOY_BTN8": (836, 174, 100, 34), #POR
                "JOY_BTN9": (836, 121, 100, 34),
                "JOY_BTN10": (940, 174, 100, 34),
                "JOY_BTN11": (836, 227, 100, 34), 
                "JOY_BTN12": (692, 174, 100, 34),
                "JOY_BTN13": (1191, 132, 100, 34),
                "JOY_BTN14": (766, 376, 100, 34), #POR
                "JOY_BTN15": (766, 429, 100, 34),
                "JOY_BTN16": (1047, 302, 100, 34), #POR
                "JOY_BTN17": (1191, 302, 100, 34),
                "JOY_BTN18": (1047, 355, 100, 34),
                "JOY_BTN19": (903, 302, 100, 34),
                "JOY_BTN20": (1047, 249, 100, 34),
                "JOY_BTN21": (1191, 597, 100, 34),
                "JOY_BTN22": (576, 302, 100, 34), #POR
                "JOY_BTN23": (576, 355, 100, 34),
                "JOY_BTN24": (432, 302, 100, 34),
                "JOY_BTN25": (576, 249, 100, 34),
                "JOY_BTN26": (720, 302, 100, 34),
                "JOY_BTN27": (1047, 483, 100, 34), #POR
                "JOY_BTN28": (1047, 536, 100, 34),
                "JOY_BTN29": (903, 483, 100, 34),
                "JOY_BTN30": (1047, 430, 100, 34),
                "JOY_BTN31": (1187, 483, 100, 34),
                "JOY_BTN32": (576, 429, 100, 34),
                "JOY_BTN33": (1047, 619, 100, 34),
                "JOY_BTN34": (576, 495, 100, 34),
                "JOY_BTN35": (576, 570, 100, 34), 
                "JOY_BTN36": (364, 495, 100, 34), #POR
                "JOY_BTN37": (364, 548, 100, 34),
                "JOY_BTN38": (901, 727, 100, 34), #POR
                "JOY_BTN39": (1045, 727, 100, 34),
                "JOY_BTN40": (1189, 727, 100, 34),
                "JOY_BTN41": (901, 780, 100, 34), #POR
                "JOY_BTN42": (1045, 780, 100, 34),
                "JOY_BTN43": (1189, 780, 100, 34),
                "JOY_BTN44": (76, 613, 100, 34), #POR
                "JOY_BTN45": (220, 613, 100, 34),
                "JOY_BTN46": (364, 613, 100, 34),
                "JOY_BTN47": (76, 666, 100, 34), #POR
                "JOY_BTN48": (220, 666, 100, 34),
                "JOY_BTN49": (364, 666, 100, 34),
                "JOY_BTN50": (145, 816, 100, 34), #POR
                "JOY_BTN51": (145, 869, 100, 34),
                "JOY_BTN52": (145, 763, 100, 34),
                "JOY_BTN53": (289, 816, 100, 34), #POR
                "JOY_BTN54": (289, 869, 100, 34),
                "JOY_BTN55": (289, 763, 100, 34),
            }
            frameworks[device] = text_boxes
        elif device.startswith("VPC Stick MT-50CM3"):
            print(f"Generating Device Framework from {device}")
            text_boxes = {
                "JOY_BTN1": (948, 336, 100, 34),
                "JOY_BTN2": (948, 389, 100, 34), #POR
                "JOY_BTN3": (948, 442, 100, 34),
                "JOY_BTN4": (948, 528, 100, 34), #POR
                "JOY_BTN5": (948, 581, 100, 34),
                "JOY_BTN6": (276, 100, 100, 34),
                "JOY_BTN7": (523, 100, 100, 34),
                "JOY_BTN8": (949, 100, 100, 34), 
                "JOY_BTN9": (949, 47, 100, 34),
                "JOY_BTN10": (805, 100, 100, 34), #POR
                "JOY_BTN11": (949, 153, 100, 34),
                "JOY_BTN12": (1092, 100, 100, 34),
                "JOY_BTN13": (949, 231, 100, 34),
                "JOY_BTN14": (276, 310, 100, 34), #POR
                "JOY_BTN15": (276, 257, 100, 34),
                "JOY_BTN16": (132, 310, 100, 34),
                "JOY_BTN17": (276, 363, 100, 34),
                "JOY_BTN18": (420, 310, 100, 34),
                "JOY_BTN19": (276, 524, 100, 34), #POR
                "JOY_BTN20": (276, 577, 100, 34),
                "JOY_BTN21": (276, 471, 100, 34),
                "JOY_BTN22": (276, 630, 100, 34),
                "JOY_BTN23": (742, 740, 100, 34), #POR
                "JOY_BTN24": (742, 687, 100, 34),
                "JOY_BTN25": (597, 740, 100, 34),
                "JOY_BTN26": (742, 793, 100, 34),
                "JOY_BTN27": (885, 740, 100, 34),
                "JOY_BTN28": (1160, 283, 100, 34), #POR
                "JOY_BTN29": (1160, 230, 100, 34),
                "JOY_BTN30": (1160, 336, 100, 34),
                "JOY_BTN31": (742, 878, 100, 34),
                "JOY_BTN32": (742, 529, 100, 34),
            }
            frameworks[device] = text_boxes
        else:
            print(f"Device {device} is not supported yet")
            return None
    return(frameworks)

def getKeybindsFromGame(user, module, selectedDevices):
    deviceBindings = {
    }
    for mod in module:
        deviceBindings[mod] = {}
        try: 
            for device in selectedDevices:
                luaDir = usersDir + user + savedGamesDir + mod + "\\joystick\\" + device
                with open(luaDir, "r") as file:
                    luaContent = file.read()
                    keybinding_pattern = re.compile(
                        r'\[\"(d\d+pnil.+?)\"\]\s*=\s*\{\s*'
                        r'\[\"added\"\]\s*=\s*\{\s*'
                        r'\[1\]\s*=\s*\{\s*'
                        r'\[\"key\"\]\s*=\s*\"(JOY_BTN\d+)\",\s*\},\s*\},\s*'
                        r'\[\"name\"\]\s*=\s*\"(.*?)\",\s*\},',
                        re.DOTALL
                    )
                    matches = keybinding_pattern.findall(luaContent)
                    keybindings = []
                    for match in matches:
                        name = match[2].split("\"")[0]
                        keybinding = {
                            "id": match[0],       
                            "key": match[1],       
                            "name": name       
                        }
                        keybindings.append(keybinding)
                    deviceBindings[mod][device] = keybindings
        except Exception as e:
            print(f"Could not get device for this module. See error {e}.")
            del deviceBindings[mod]
            pass
    return deviceBindings

def generateImage(keybindsList, frameworks):
    font = ImageFont.truetype("arial.ttf", 10)
    for module, devices in keybindsList.items():
        if devices is not None:
            for device, binds in devices.items():
                if device.startswith("VPC MongoosT-50CM3"):
                    image = Image.open("./templatefiles/mongoosethrottle.png")
                    draw = ImageDraw.Draw(image)
                elif device.startswith("VPC Stick MT-50CM3"): 
                    image = Image.open("./templatefiles/constellationalphaprime.png")
                    draw = ImageDraw.Draw(image)
                for i in binds:
                    x = frameworks[device][i["key"]][0]
                    y = frameworks[device][i["key"]][1]
                    width = frameworks[device][i["key"]][2]
                    height = frameworks[device][i["key"]][3]
                    draw.rectangle([x, y, x+width, y+height], outline="red", width=2)
                    text = i["name"]
                    text_x = x + 5
                    text_y = y + 5
                    draw.text((text_x, text_y), text, fill="black", font=font, align="center")
                outputdevice = device.split(" {")[0]
                outputmodule = str(module).strip()
                if 'imagefiles' not in os.listdir("./"):
                    os.mkdir(f"./imagefiles/")
                if outputmodule not in os.listdir("./imagefiles"):
                    os.mkdir(f"./imagefiles/{outputmodule}")
                output_path = f"./imagefiles/{outputmodule}/{outputdevice}.pdf"
                image.save(output_path)

            



def main():
    print("Starting HOTAS PDF Generator.")
    users = getUsers()
    user = getUserSelection(users)
    modules = getModules(user)
    module = getModuleSelection(modules)
    devices = getSavedDevices(user, module)
    selectedDevices = getDeviceSelection(user, devices)
    frameworks = createDevicesFrameworks(selectedDevices)
    keybindsList = getKeybindsFromGame(user, module, selectedDevices)
    generateImage(keybindsList, frameworks)




if __name__ == "__main__":
    main()
