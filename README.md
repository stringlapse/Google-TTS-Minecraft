# Google TTS Minecraft

Originally created by TheblueMan003 https://www.youtube.com/watch?v=ZCZP7JjQ6Aw

## Settings
Edit settings at the top of `google_voice.py` before running
- `include_ogg` - Include "ogg" in TTS
- `include_full_path` - Include the full folder path in TTS
- `include_last_folder` - Include the last folder in the path in TTS for extra context (Ignored if include_full_path is True)

## Usage
1. Install `requirements.txt`
2. Make sure `ffprobe` is in path
3. Run `extract_sounds.py` then run `google_voice.py`
4. Copy the `Google_TTS` folder to `.minecraft/resourcepacks`
5. Enable the resource pack in Minecraft and ...enjoy?
