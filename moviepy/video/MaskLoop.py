# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.MaskColor.MaskColor',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, color=(0, 0, 0), thr=0, s=1.0):
    """
    Returns a new clip with a mask for transparency where the original clip is of the given color.

    Args:
        input_source: The video clip to which the effect will be applied.
        color (tuple, optional): A 3-tuple (R, G, B) representing the color to be masked (made transparent). Defaults to black (0, 0, 0).
        thr (float, optional): The threshold for color matching. A higher value means a wider range of colors around 'color' will be masked. Defaults to 0.
        s (float, optional): A sensitivity factor for the mask. Defaults to 1.0.
    """
    output = input_source.with_effects([MaskColor(color=color, thr=thr, s=s)])
    return output
