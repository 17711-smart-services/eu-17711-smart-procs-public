# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.FadeOut.FadeOut',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, duration=1, final_color=(0, 0, 0)):
    """
    Makes the provided input clip progressively fade to a specified color at the end.

    Args:
        input_source: The video clip to which the effect will be applied.
        duration (float, optional): The duration in seconds over which the clip will fade out. Defaults to 1 second.
        final_color (tuple, optional): A 3-tuple (R, G, B) representing the color to which the clip will fade.
                                       Defaults to black (0, 0, 0).
    """
    output = input_source.with_effects([FadeOut(duration=duration, final_color=final_color)])
    return output
