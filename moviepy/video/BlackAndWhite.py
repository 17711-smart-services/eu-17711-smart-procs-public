# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.BlackAndWhite.BlackAndWhite',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, rgb=None):
    """
    Applies a black and white effect to the provided input by desaturating the picture.

    Args:
        input_source: The video clip to which the effect will be applied.
        rgb (tuple, optional): A 3-tuple (R, G, B) representing the target color to desaturate towards.
                               If None, it defaults to a standard black and white conversion.
    """
    output = input_source.with_effects([BlackAndWhite(rgb=rgb)])
    return output
