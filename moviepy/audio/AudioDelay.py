# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.audio.fx.AudioDelay.AudioDelay',
   }
]

__version__ = '0.0.1'
__input_types__ = ['audio', 'video']
__output_types__ = ['audio', 'video']

def apply(input_source, offset=0.1, n_delays=3, decay=1.0):
    """
    Applies an audio delay effect, repeating the audio at constant intervals with decaying volume.

    Args:
        input_source: The audio (or video) clip to which the effect will be applied.
        offset (float, optional): The time in seconds between each repeated audio instance. Defaults to 0.1 seconds.
        n_delays (int, optional): The number of times the audio will be repeated (delayed copies). Defaults to 3.
        decay (float, optional): The final volume multiplier for the last delayed audio instance.
                                 Volume levels decay linearly from 1 to this value. Defaults to 1.0 (no decay).
    """
    output = input_source.with_effects([AudioDelay(offset=offset, n_delays=n_delays, decay=decay)])
    return output

