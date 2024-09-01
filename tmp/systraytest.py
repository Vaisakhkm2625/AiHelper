import pystray

from PIL import Image, ImageDraw
from generate_penguine_logo import draw_penguin_logo


def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image


# In order for the icon to be displayed, you must provide an icon
icon = pystray.Icon(
    'test name',
    icon=draw_penguin_logo(64, 64))


# To finally show you icon, call run
icon.run()
