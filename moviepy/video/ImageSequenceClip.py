# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.io.ImageSequenceClip.ImageSequenceClip',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(sequence, fps=None, durations=None, with_mask=True, is_mask=False, load_images=False):
    """
    Creates a VideoClip from a sequence of images.

    Args:
        sequence (str or list): The source of the images.
                                Can be the name of a folder containing only pictures (alphanumerical order),
                                a list of image file names, or a list of NumPy arrays representing images.
                                Masks are not currently supported for NumPy array sequences.
        fps (float, optional): The number of picture frames to read per second.
                               If 'durations' is provided, this parameter is ignored. Defaults to None.
        durations (list, optional): A list of the duration in seconds for each picture in the sequence.
                                    If provided, 'fps' is ignored. Defaults to None.
        with_mask (bool, optional): Determines if the alpha layer of PNG images should be considered as a mask. Defaults to True.
        is_mask (bool, optional): Specifies if this sequence of pictures will be used as an animated mask. Defaults to False.
        load_images (bool, optional): If True, all images will be loaded into RAM. This is useful for a small number of images
                                      that will be used multiple times to improve performance. Defaults to False.
    """
    output = ImageSequenceClip(sequence=sequence, fps=fps, durations=durations, with_mask=with_mask, is_mask=is_mask, load_images=load_images)
    return output

