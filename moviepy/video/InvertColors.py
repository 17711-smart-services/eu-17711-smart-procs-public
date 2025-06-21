# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.InvertColors.InvertColors',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source):
    """
    Inverts the colors of the provided input clip.

    Args:
        input_source: The video clip to which the effect will be applied.
    """
    output = input_source.with_effects([InvertColors()])
    return output
