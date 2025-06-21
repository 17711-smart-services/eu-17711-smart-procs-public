# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.Margin.Margin',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, margin_size=None, left=0, right=0, top=0, bottom=0, color=(0, 0, 0)):
    """
    Draws an external margin around the frame of the provided input clip.

    Args:
        input_source: The video clip to which the effect will be applied.
        margin_size (int, optional): The size of the margin in pixels. If specified, it applies uniformly to all sides.
                                     If None, individual 'left', 'right', 'top', 'bottom' values are used.
        left (int, optional): The size of the left margin in pixels. Defaults to 0.
        right (int, optional): The size of the right margin in pixels. Defaults to 0.
        top (int, optional): The size of the top margin in pixels. Defaults to 0.
        bottom (int, optional): The size of the bottom margin in pixels. Defaults to 0.
        color (tuple, optional): A 3-tuple (R, G, B) representing the color of the margin. Defaults to black (0, 0, 0).
    """
    output = input_source.with_effects([Margin(margin_size=margin_size, left=left, right=right, top=top, bottom=bottom, color=color)])
    return output
