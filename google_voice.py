import os
from gtts import gTTS
from pydub import AudioSegment

##########
# Settings
##########

include_ogg = False # Include "ogg" in TTS
include_full_path = False # Include the full folder path in TTS
include_last_folder = True # Include the last folder in the path in TTS for extra context (Ignored if include_full_path is True)
language = "en" # TTS language. For a full list of supported languages, see https://github.com/pndurette/gTTS/blob/master/gtts/lang.py

def list_subdir_file(path):
    directories = [path]
    files = []
    index = 0
    while index < len(directories):
        directory = directories[index]
        for item in os.listdir(directory):
            if os.path.isdir(directory + "/" + item):
                directories.append(directory + "/" + item)
            else:
                files.append(directory + "/" + item)

        index += 1

    return files

print("Replacing sounds\nThis will take a while")

for file in list_subdir_file("./Google_TTS/assets/minecraft/sounds"):
    if file.endswith(".ogg"):
        lan = language
        tts_input = file.replace("./Google_TTS/assets/minecraft/sounds", "").replace("_", " ").replace("\\", " ")
        if not include_ogg: # Exclude ogg
            tts_input = tts_input.replace(".ogg", "")
        else: # Include ogg but remove "."
            tts_input = tts_input.replace(".", " ")
        if not include_full_path: # Exclude full path
            if not include_last_folder: # Exclude last folder
                tts_input = tts_input[tts_input.rfind("/")+1:]
            else: # Include last folder
                tts_input = tts_input[tts_input.rfind("/", 0, tts_input.rfind("/"))+1:]
        # Include full path doesn't remove anything else
        tts_input = tts_input.replace("/", " ")

        print(tts_input)
        o = gTTS(text=tts_input,lang=lan, slow=False)
        o.save("tmp.mp3")
        sound = AudioSegment.from_mp3("tmp.mp3")
        sound.export(file, format="ogg")

os.remove("tmp.mp3")
