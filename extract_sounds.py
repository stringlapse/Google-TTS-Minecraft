# Stolen from https://minecraft.gamepedia.com/Tutorials/Sound_directory#Extracting_Minecraft_Sounds_using_Python

import json, os, platform, shutil, sys

''' 
    Copies audio files from indescript hashed folders to named sorted folders.
    You may need to change output path.
'''

# This section should work on any system as well
print("Your OS is " + platform.system())
if platform.system() == "Windows":
    MC_ASSETS = os.path.expandvars(r"%APPDATA%/.minecraft/assets")
else:
    MC_ASSETS = os.path.expanduser(r"~/.minecraft/assets")

# Find the latest installed version of minecraft (choose the last element in assets/indexes)
MC_VERSION = os.listdir(MC_ASSETS+"/indexes/")[-1]
print("Your latest installed version of minecraft is " + MC_VERSION[:-5] + "\n")

# Change this if you want to put the sound files somewhere else
OUTPUT_PATH = os.path.normpath(os.path.expandvars(os.path.expanduser(f"./Google_TTS/")))

# These are unlikely to change
MC_OBJECT_INDEX = f"{MC_ASSETS}/indexes/{MC_VERSION}"
MC_OBJECTS_PATH = f"{MC_ASSETS}/objects"
MC_SOUNDS = r"minecraft/sounds/"


with open(MC_OBJECT_INDEX, "r") as read_file:
    # Parse the JSON file into a dictionary
    data = json.load(read_file)

    # Find each line with MC_SOUNDS prefix, remove the prefix and keep the rest of the path and the hash
    sounds = {k[len(MC_SOUNDS):] : v["hash"] for (k, v) in data["objects"].items() if k.startswith(MC_SOUNDS)}

    print("File extraction :")

    for fpath, fhash in sounds.items():
        # Ensure the paths are good to go for Windows with properly escaped backslashes in the string
        src_fpath = os.path.normpath(f"{MC_OBJECTS_PATH}/{fhash[:2]}/{fhash}")
        dest_fpath = os.path.normpath(f"{OUTPUT_PATH}/sounds/{fpath}")

        # Print current extracted file
        print(fpath)

        # Make any directories needed to put the output file into as Python expects
        os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)

        # Copy the file
        shutil.copyfile(src_fpath, dest_fpath)