# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.MasksAnd.MasksAnd',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, other_clip):
    """
    Performs a logical 'and' (minimum pixel color values) between the mask of the provided input clip and another clip's mask.

    Args:
        input_source: The video clip whose mask will be combined.
        other_clip: The other clip whose mask will be used for the 'and' operation.
    """
    output = input_source.with_effects([MasksAnd(other_clip=other_clip)])
    return output
