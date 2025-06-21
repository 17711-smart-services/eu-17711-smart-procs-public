# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.CrossFadeIn.CrossFadeIn',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, duration=1):
    """
    Makes the provided input clip appear progressively over a specified duration.

    Args:
        input_source: The video clip to which the effect will be applied.
        duration (float, optional): The duration in seconds over which the clip will progressively appear.
                                    Defaults to 1 second.
    """
    output = input_source.with_effects([CrossFadeIn(duration=duration)])
    return output
