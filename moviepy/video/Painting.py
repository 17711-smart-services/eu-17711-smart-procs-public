# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.Painting.Painting',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, saturation=1.0, black=0.0):
    """
    Transforms the provided input clip into a painting-like visual.

    Args:
        input_source: The video clip to which the effect will be applied.
        saturation (float, optional): The saturation level of the "painting" effect. Higher values result in more vibrant colors. Defaults to 1.0.
        black (float, optional): The black level of the "painting" effect. Higher values increase the intensity of dark areas. Defaults to 0.0.
    """
    output = input_source.with_effects([Painting(saturation=saturation, black=black)])
    return outputo
