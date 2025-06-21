# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.AccelDecel.AccelDecel',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, new_duration=None):
    """
    Applies an accelerate and decelerate effect to the provided input.

    Args:
        input_source: The video clip to which the effect will be applied.
        new_duration (float, optional): The new duration for the clip after acceleration/deceleration.
                                        If None, the effect will determine a suitable duration.
    """
    output = input_source.with_effects([AccelDecel(new_duration=new_duration)])
    return output
