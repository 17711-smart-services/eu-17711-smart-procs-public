# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.Freeze.Freeze',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, t=0):
    """
    Momentarily freezes the provided input clip at a specific time.

    Args:
        input_source: The video clip to which the effect will be applied.
        t (float, optional): The time in seconds at which to freeze the clip. Defaults to 0 seconds (the beginning).
    """
    output = input_source.with_effects([Freeze(t=t)])
    return output
