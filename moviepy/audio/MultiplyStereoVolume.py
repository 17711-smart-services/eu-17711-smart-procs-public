# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.audio.fx.MultiplyStereoVolume.MultiplyStereoVolume',
   }
]

__version__ = '0.0.1'
__input_types__ = ['audio', 'video'] # Specifically for stereo audio
__output_types__ = ['audio', 'video']

def apply(input_source, left=1.0, right=1.0):
    """
    Adjusts the volume of the left and right channels of a stereo audio clip separately.

    Args:
        input_source: The stereo audio (or video) clip to which the effect will be applied.
        left (float, optional): The volume multiplier for the left audio channel. Defaults to 1.0 (no change).
        right (float, optional): The volume multiplier for the right audio channel. Defaults to 1.0 (no change).
    """
    output = input_source.with_effects([MultiplyStereoVolume(left=left, right=right)])
    return output

