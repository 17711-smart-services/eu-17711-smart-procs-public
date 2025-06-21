# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.SlideOut.SlideOut',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, duration=1, side='left'):
    """
    Makes the provided input clip slide out to one side of the screen.

    Args:
        input_source: The video clip to which the effect will be applied.
        duration (float, optional): The duration in seconds over which the clip will slide out. Defaults to 1 second.
        side (str, optional): The side to which the clip will slide out. Can be 'left', 'right', 'top', or 'bottom'. Defaults to 'left'.
    """
    output = input_source.with_effects([SlideOut(duration=duration, side=side)])
    return output

