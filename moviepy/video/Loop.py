# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.Loop.Loop',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, n=None, duration=None):
    """
    Returns a clip that plays the provided input clip in a loop.

    Args:
        input_source: The video clip to which the effect will be applied.
        n (int, optional): The number of times the clip should loop. If None, it loops indefinitely.
        duration (float, optional): The total duration of the looped clip. If specified, 'n' will be ignored.
    """
    output = input_source.with_effects([Loop(n=n, duration=duration)])
    return output
