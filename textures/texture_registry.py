from PIL import Image
import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
import os


def read_texture(filename):
    img = Image.open(os.path.join('assets', filename))
    img_data = np.array(list(img.getdata()), np.int8)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    return texture_id


GRASS = read_texture('grass.jpg')
STONE = read_texture('stoned.jpg')
BLACK_CONCRETE_POWDER = read_texture('black_concrete_powder.png')
LANDSCAPE_DAY = read_texture('landscape_day.png')
LANDSCAPE_NIGHT = read_texture('landscape_night.png')

SKY_DAY = read_texture('sky_day.png')
SKY_NIGHT = read_texture('sky_night.png')
