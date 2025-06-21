# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.MultiplySpeed.MultiplySpeed',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, factor=1.0):
    """
    Returns a clip playing the provided input clip at a speed multiplied by a given factor.

    Args:
        input_source: The video clip to which the effect will be applied.
        factor (float, optional): The factor by which to multiply the clip's speed. A factor > 1.0 speeds up the clip,
                                  a factor < 1.0 slows it down. Defaults to 1.0 (original speed).
    """
    output = input_source.with_effects([MultiplySpeed(factor=factor)])
    return output

