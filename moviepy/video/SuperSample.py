# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.fx.SuperSample.SuperSample',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, d=0.1, n_frames=5):
    """
    Replaces each frame at time 't' by the mean of 'n_frames' equally spaced frames taken in the interval [t-d, t+d]. This can smooth motion.

    Args:
        input_source: The video clip to which the effect will be applied.
        d (float, optional): The half-interval duration in seconds around 't' for sampling frames. Defaults to 0.1 seconds.
        n_frames (int, optional): The number of frames to sample within the interval [t-d, t+d]. Defaults to 5 frames.
    """
    output = input_source.with_effects([SuperSample(d=d, n_frames=n_frames)])
    return output

