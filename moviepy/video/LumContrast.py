# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.LumContrast.LumContrast',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, lum=0.0, contrast=0.0):
    """
    Applies luminosity and contrast correction to the provided input clip.

    Args:
        input_source: The video clip to which the effect will be applied.
        lum (float, optional): The luminosity adjustment value. Positive values increase brightness, negative values decrease it. Defaults to 0.0 (no change).
        contrast (float, optional): The contrast adjustment value. Positive values increase contrast, negative values decrease it. Defaults to 0.0 (no change).
    """
    output = input_source.with_effects([LumContrast(lum=lum, contrast=contrast)])
    return output
