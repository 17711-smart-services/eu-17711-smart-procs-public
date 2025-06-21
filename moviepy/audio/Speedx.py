# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.audio.fx.Speedx.Speedx',
   }
]

__version__ = '0.0.1'
__input_types__ = ['audio', 'video']
__output_types__ = ['audio', 'video']

def apply(input_source, factor):
    """
    Changes the speed of the audio of the provided clip by a given factor.

    Args:
        input_source: The audio (or video) clip to which the effect will be applied.
        factor (float): The factor by which to multiply the audio speed.
                        A factor > 1.0 speeds up the audio, a factor < 1.0 slows it down.
    """
    output = input_source.with_effects([Speedx(factor=factor)])
    return output
 
