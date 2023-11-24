from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from geometry import model


def draw_tree(tree: model.BasicModel):
    glPushMatrix()
    glTranslatef(*tree.position)
    glRotatef(tree.angle, 0, 1, 0)
    glPushMatrix()
    no_mat = [0, 0, 0, 1.0]
    mat_diffuse = [0.7, 0.7, 0.7, 1.0]
    no_shininess = [0.0]
    mat_emission = [0.2, 0.2, 0.2, 0.0]
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.5, 0.25, 0., 1.])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat)
    glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess)
    glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
    glScalef(0.25, 1, 0.25)
    glRotatef(-90, 1, 0, 0)
    glutSolidCylinder(1, 1, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0., 0.7, 0., 1.])
    glTranslatef(0, 1, 0)
    glRotatef(-90, 1, 0, 0)
    glutSolidCone(1, 3, 20, 20)
    glPopMatrix()

    glPopMatrix()
