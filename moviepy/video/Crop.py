# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.Crop.Crop',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, x1=None, y1=None, x2=None, y2=None):
    """
    Crops the provided input clip to a specified rectangular subregion.

    Args:
        input_source: The video clip to which the effect will be applied.
        x1 (int, optional): The x-coordinate of the top-left corner of the crop region.
                            If None, it defaults to the left edge of the clip.
        y1 (int, optional): The y-coordinate of the top-left corner of the crop region.
                            If None, it defaults to the top edge of the clip.
        x2 (int, optional): The x-coordinate of the bottom-right corner of the crop region.
                            If None, it defaults to the right edge of the clip.
        y2 (int, optional): The y-coordinate of the bottom-right corner of the crop region.
                            If None, it defaults to the bottom edge of the clip.
    """
    output = input_source.with_effects([Crop(x1=x1, y1=y1, x2=x2, y2=y2)])
    return output
