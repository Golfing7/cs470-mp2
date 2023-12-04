from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from geometry import util
from geometry import model


def draw_tree(tree: model.BasicModel):
    glPushMatrix()
    glTranslatef(*tree.position)
    glRotatef(tree.angle, 0, 1, 0)
    glPushMatrix()
    util.set_mat([0.5, 0.25, 0., 1.])
    glScalef(0.25, 1, 0.25)
    glRotatef(-90, 1, 0, 0)
    glutSolidCylinder(1, 1, 20, 20)
    glPopMatrix()

    glPushMatrix()
    util.set_mat([0., 0.7, 0., 1.])
    glTranslatef(0, 1, 0)
    glRotatef(-90, 1, 0, 0)
    glutSolidCone(1, 3, 20, 20)
    glPopMatrix()

    glPopMatrix()
