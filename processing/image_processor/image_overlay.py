from PIL import Image
import numpy as np


def overlay_images(foreground_path, output_path):
    foreground = Image.open(foreground_path)

    gradient = np.linspace((200, 200, 200), (100, 100, 100), 900)[np.newaxis, :, :]
    background = Image.fromarray(np.uint8(gradient), 'RGB')

    background = background.resize(foreground.size, Image.ADAPTIVE)

    merged_image = Image.alpha_composite(background.convert('RGBA'), foreground.convert('RGBA'))

    merged_image.save(output_path, format='PNG')