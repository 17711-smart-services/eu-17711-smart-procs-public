# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.editor.CompositeVideoClip',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(clips, method='chain', transition=None, bg_color=None, is_mask=False, padding=0):
    """
    Concatenates several video clips together, playing them one after another.

    Args:
        clips (list): A list of video clips to concatenate. Each clip must have its 'duration' attribute set.
        method (str, optional): The concatenation method. Can be 'chain' (simple sequence) or 'compose' (handles different resolutions, centering smaller clips). Defaults to 'chain'.
        transition (moviepy.editor.VideoClip, optional): A clip that will be played between each two clips in the list. Defaults to None.
        bg_color (tuple, optional): Only for method='compose'. The RGB color of the background. Set to None for a transparent clip. Defaults to None.
        is_mask (bool, optional): If True, treats the clips as masks. Defaults to False.
        padding (float, optional): Only for method='compose'. The duration of silence or overlap between two consecutive clips.
                                   Negative padding means clips will overlap. A non-zero padding automatically sets the method to 'compose'. Defaults to 0.
    """
    if padding != 0 and method == 'chain':
        method = 'compose' # padding automatically sets the method to 'compose'

    output = CompositeVideoClip.concatenate_videoclips(clips, method=method, transition=transition, bg_color=bg_color, is_mask=is_mask, padding=padding)
    return output

