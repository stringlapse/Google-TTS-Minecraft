import os
from gtts import gTTS
from pydub import AudioSegment


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


for file in list_subdir_file("."):
    if file.endswith(".ogg"):
        lan = "en"
        o = gTTS(text=file.replace(".", " ").replace("_", " ").replace(".ogg", " ").replace("/", " ").replace("\\", " "),lang=lan, slow=False)
        o.save("tmp.mp3")
        sound = AudioSegment.from_mp3("tmp.mp3")
        sound.export(file, format="ogg")

