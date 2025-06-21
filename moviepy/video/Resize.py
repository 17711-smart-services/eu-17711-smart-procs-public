# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.Resize.Resize',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, new_size=None, height=None, width=None):
    """
    Returns a resized version of the provided input video clip.

    Args:
        input_source: The video clip to which the effect will be applied.
        new_size (tuple or float, optional): The new size of the clip. Can be (width, height) in pixels, or a float to scale uniformly.
                                            If None, 'height' or 'width' must be specified.
        height (int, optional): The new height of the clip in pixels. If 'width' is None, the aspect ratio is maintained.
        width (int, optional): The new width of the clip in pixels. If 'height' is None, the aspect ratio is maintained.
    """
    output = input_source.with_effects([Resize(new_size=new_size, height=height, width=width)])
    return output

