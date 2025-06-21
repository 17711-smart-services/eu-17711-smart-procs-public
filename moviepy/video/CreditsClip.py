# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
   {"lib": "moviepy",
     "version": "2.2.1",
     "import": 'moviepy.video.tools.credits.CreditsClip',
   }
]

__version__ = '0.0.1'

__input_types__ = ['video']
__output_types__ = ['video']

def apply(input_source, creditfile, width, color='white', font='Arial', fontsize=20, duration=None, stroke_color='black', stroke_width=0, opacity=None, gap=0, align='center'):
    """
    Generates a video clip displaying scrolling credits from a text file or string.

    Args:
        input_source: This parameter is ignored for this specific effect as the 'CreditsClip'
                      creates a new clip directly from credit information. It's included for
                      structural consistency with other plugin definitions.
        creditfile (str): The path to a text file containing the credits, or a string
                          where each line represents a line of credits.
        width (int): The width in pixels for the generated credits clip.
        color (str, optional): The color of the text. Can be a color name (e.g., 'white', 'red')
                                or an RGB tuple (e.g., (255, 255, 255)). Defaults to 'white'.
        font (str, optional): The font family to use for the text. Defaults to 'Arial'.
        fontsize (int, optional): The size of the font. Defaults to 20.
        duration (float, optional): The total duration of the credits clip in seconds. If None,
                                    the duration is automatically determined based on the content
                                    and scrolling speed. Defaults to None.
        stroke_color (str, optional): The color of the text stroke (outline). Defaults to 'black'.
        stroke_width (float, optional): The width of the text stroke. Defaults to 0 (no stroke).
        opacity (float, optional): The opacity of the credits clip (0.0 for fully transparent,
                                   1.0 for fully opaque). Defaults to None (fully opaque).
        gap (int, optional): The vertical spacing between lines of credits in pixels. Defaults to 0.
        align (str, optional): The horizontal alignment of the text. Can be 'center', 'left', or 'right'.
                               Defaults to 'center'.
    """
    output = CreditsClip(creditfile=creditfile, width=width, color=color, font=font, fontsize=fontsize,
                         duration=duration, stroke_color=stroke_color, stroke_width=stroke_width,
                         opacity=opacity, gap=gap, align=align)
    return output

