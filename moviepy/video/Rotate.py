# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.Rotate.Rotate',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, angle=0, unit='degrees', resample_method='bicubic', expand=True, center=None, translate=None, bg_color=None):
    """
    Rotates the provided input clip by a specified angle anticlockwise.

    Args:
        input_source: The video clip to which the effect will be applied.
        angle (float, optional): The angle of rotation. Defaults to 0.
        unit (str, optional): The unit of the angle, either 'degrees' or 'radians'. Defaults to 'degrees'.
        resample_method (str, optional): The resampling method for rotation. Defaults to 'bicubic'.
        expand (bool, optional): If True, the clip's dimensions will expand to fit the rotated content without cropping. Defaults to True.
        center (tuple, optional): A 2-tuple (x, y) representing the center of rotation. If None, it rotates around the clip's center.
        translate (tuple, optional): A 2-tuple (dx, dy) to translate the clip after rotation.
        bg_color (tuple, optional): A 3-tuple (R, G, B) representing the background color for new areas exposed by rotation. Defaults to None (black borders if not expanded).
    """
    output = input_source.with_effects([Rotate(angle=angle, unit=unit, resample_method=resample_method, expand=expand, center=center, translate=translate, bg_color=bg_color)])
    return output

