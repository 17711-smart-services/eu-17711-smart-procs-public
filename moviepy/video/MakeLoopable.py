# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.MakeLoopable.MakeLoopable',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, overlap_duration=1.0):
    """
    Makes the provided input clip loopable by fading it in progressively at its own end.

    Args:
        input_source: The video clip to which the effect will be applied.
        overlap_duration (float, optional): The duration in seconds of the fade-in overlap at the end of the clip. Defaults to 1.0 second.
    """
    output = input_source.with_effects([MakeLoopable(overlap_duration=overlap_duration)])
    return output
