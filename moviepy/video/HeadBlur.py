# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.HeadBlur.HeadBlur',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, fx=0.5, fy=0.5, radius=0.1):
    """
    Blurs a moving part of the frames in the provided input clip, simulating a head blur effect.

    Args:
        input_source: The video clip to which the effect will be applied.
        fx (float, optional): The x-coordinate (relative to clip width, 0 to 1) of the center of the blur. Defaults to 0.5.
        fy (float, optional): The y-coordinate (relative to clip height, 0 to 1) of the center of the blur. Defaults to 0.5.
        radius (float, optional): The radius of the blur. Larger values result in more blur. Defaults to 0.1.
    """
    output = input_source.with_effects([HeadBlur(fx=fx, fy=fy, radius=radius)])
    return output
