# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.audio.fx.AudioFadeOut.AudioFadeOut',
   }
]

__version__ = '0.0.1'
__input_types__ = ['audio', 'video']
__output_types__ = ['audio', 'video']

def apply(input_source, duration=1):
    """
    Fades out the audio of the provided clip, progressively decreasing volume towards the end.

    Args:
        input_source: The audio (or video) clip to which the effect will be applied.
        duration (float, optional): The duration in seconds over which the audio will fade out. Defaults to 1 second.
    """
    output = input_source.with_effects([AudioFadeOut(duration=duration)])
    return output

