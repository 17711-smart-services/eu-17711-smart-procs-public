# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.audio.fx.MultiplyVolume.MultiplyVolume',
   }
]

__version__ = '0.0.1'
__input_types__ = ['audio', 'video']
__output_types__ = ['audio', 'video']

def apply(input_source, factor=1.0):
    """
    Multiplies the audio volume of the provided clip by a given factor.

    Args:
        input_source: The audio (or video) clip to which the effect will be applied.
        factor (float, optional): The volume multiplier. A factor > 1.0 increases volume,
                                  a factor < 1.0 decreases it. Defaults to 1.0 (no change).
    """
    output = input_source.with_effects([MultiplyVolume(factor=factor)])
    return output

