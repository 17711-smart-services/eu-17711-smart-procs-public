# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.audio.fx.AudioLoop.AudioLoop',
   }
]

__version__ = '0.0.1'
__input_types__ = ['audio', 'video']
__output_types__ = ['audio', 'video']

def apply(input_source, n_loops=None, duration=None):
    """
    Loops the provided audio clip a specified number of times or for a total duration.

    Args:
        input_source: The audio (or video) clip to which the effect will be applied.
        n_loops (int, optional): The number of times the audio clip should loop. If None,
                                 and `duration` is also None, it loops indefinitely. Defaults to None.
        duration (float, optional): The total duration in seconds of the looped audio clip.
                                    If specified, `n_loops` is ignored. Defaults to None.
    """
    output = input_source.with_effects([AudioLoop(n_loops=n_loops, duration=duration)])
    return output

