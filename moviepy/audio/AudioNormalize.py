# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.audio.fx.AudioNormalize.AudioNormalize',
   }
]

__version__ = '0.0.1'
__input_types__ = ['audio', 'video']
__output_types__ = ['audio', 'video']

def apply(input_source):
    """
    Normalizes the volume of the provided audio clip to 0dB, ensuring consistent loudness.

    Args:
        input_source: The audio (or video) clip to which the effect will be applied.
    """
    output = input_source.with_effects([AudioNormalize()])
    return output

