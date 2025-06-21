# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.FreezeRegion.FreezeRegion',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, t=0, region=(0, 0, 1, 1)):
    """
    Freezes a specific region of the provided input clip while the rest remains animated.

    Args:
        input_source: The video clip to which the effect will be applied.
        t (float, optional): The time in seconds at which to freeze the specified region. Defaults to 0 seconds (the beginning).
        region (tuple, optional): A 4-tuple (x1, y1, x2, y2) representing the coordinates of the region to freeze.
                                  Coordinates are relative to the clip's dimensions (0 to 1). Defaults to the entire clip.
    """
    output = input_source.with_effects([FreezeRegion(t=t, region=region)])
    return output
