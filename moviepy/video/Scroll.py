# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.Scroll.Scroll',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, w=None, h=None, x_speed=0, y_speed=0, x_start=0, y_start=0):
    """
    Applies a horizontal or vertical scrolling effect to the provided input clip.

    Args:
        input_source: The video clip to which the effect will be applied.
        w (int, optional): The width of the scrolling window. If None, it uses the clip's width.
        h (int, optional): The height of the scrolling window. If None, it uses the clip's height.
        x_speed (int, optional): The horizontal scrolling speed in pixels per second. Positive for right, negative for left. Defaults to 0.
        y_speed (int, optional): The vertical scrolling speed in pixels per second. Positive for down, negative for up. Defaults to 0.
        x_start (int, optional): The initial x-coordinate of the visible window. Defaults to 0.
        y_start (int, optional): The initial y-coordinate of the visible window. Defaults to 0.
    """
    output = input_source.with_effects([Scroll(w=w, h=h, x_speed=x_speed, y_speed=y_speed, x_start=x_start, y_start=y_start)])
    return output

