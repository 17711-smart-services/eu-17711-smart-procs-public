# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.Blink.Blink',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, duration_on=1, duration_off=1):
    """
    Makes the provided input clip blink on and off.

    Args:
        input_source: The video clip to which the effect will be applied.
        duration_on (float, optional): The duration in seconds the clip remains visible. Defaults to 1 second.
        duration_off (float, optional): The duration in seconds the clip remains invisible. Defaults to 1 second.
    """
    output = input_source.with_effects([Blink(duration_on=duration_on, duration_off=duration_off)])
    return output
