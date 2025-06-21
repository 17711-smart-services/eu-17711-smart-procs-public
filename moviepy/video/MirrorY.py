# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.MirrorY.MirrorY',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, apply_to='both'):
    """
    Flips the provided input clip vertically and its mask.

    Args:
        input_source: The video clip to which the effect will be applied.
        apply_to (str, optional): Specifies what parts of the clip to mirror. Can be 'video', 'mask', or 'both'. Defaults to 'both'.
    """
    output = input_source.with_effects([MirrorY(apply_to=apply_to)])
    return output
