from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

mat_diffuse = [0.7, 0.7, 0.7, 1.0]
mat_specular = [0.3, 0.3, 0.3, 1.0]
no_mat = [0., 0., 0., 1.]
shininess = [0.5]


def set_mat(color):
    glMaterialfv(GL_FRONT, GL_AMBIENT, color)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)
    glMaterialfv(GL_FRONT, GL_EMISSION, no_mat)
