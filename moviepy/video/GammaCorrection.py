# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.GammaCorrection.GammaCorrection',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, gamma=1.0):
    """
    Applies gamma correction to the provided input video clip.

    Args:
        input_source: The video clip to which the effect will be applied.
        gamma (float, optional): The gamma value for correction. Values greater than 1.0 will lighten the image,
                                 and values less than 1.0 will darken it. Defaults to 1.0 (no correction).
    """
    output = input_source.with_effects([GammaCorrection(gamma=gamma)])
    return output
