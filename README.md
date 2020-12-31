# Google TTS Minecraft

### A Minecraft resource pack that changes all sounds to Google TTS saying the names of the sounds

Originally created by TheblueMan003 https://www.youtube.com/watch?v=ZCZP7JjQ6Aw

## Installing this resource pack
There are pregenerated resource packs in [releases](https://github.com/stringlapse/Google-TTS-Minecraft/releases). To install one, download the zip file and extract the contained `Google_TTS` folder into `.minecraft/resourcepacks` then enable it in game.

## Generating a new resource pack
1. Install `requirements.txt`
2. Make sure `ffprobe` is in path
3. Run `extract_sounds.py`
4. Make changes to settings in `google_voice.py` then run it
5. Copy the `Google_TTS` folder to `.minecraft/resourcepacks`
6. Enable the resource pack in Minecraft and ...enjoy?

## Settings
Settings can be changed by editing `google_voice.py`
- `include_ogg` - Include "ogg" in TTS
- `include_full_path` - Include the full folder path in TTS
- `include_last_folder` - Include the last folder in the path in TTS for better context (Ignored if `include_full_path` is enabled)
- `language` - TTS language. For a full list of supported languages, see https://github.com/pndurette/gTTS/blob/master/gtts/lang.py
