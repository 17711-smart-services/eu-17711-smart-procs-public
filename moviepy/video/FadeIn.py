# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.FadeIn.FadeIn',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, duration=1, initial_color=(0, 0, 0)):
    """
    Makes the provided input clip progressively appear from a specified color at the beginning.

    Args:
        input_source: The video clip to which the effect will be applied.
        duration (float, optional): The duration in seconds over which the clip will fade in. Defaults to 1 second.
        initial_color (tuple, optional): A 3-tuple (R, G, B) representing the color from which the clip will appear.
                                         Defaults to black (0, 0, 0).
    """
    output = input_source.with_effects([FadeIn(duration=duration, initial_color=initial_color)])
    return output
