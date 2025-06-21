# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.MultiplyColor.MultiplyColor',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, factor=1.0):
    """
    Multiplies the provided input clip's colors by a given factor, affecting brightness.

    Args:
        input_source: The video clip to which the effect will be applied.
        factor (float, optional): The factor by which to multiply the clip's colors. A factor > 1.0 increases brightness,
                                  a factor < 1.0 decreases it. Defaults to 1.0 (no change).
    """
    output = input_source.with_effects([MultiplyColor(factor=factor)])
    return output

