from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from game import game_object
from game import player
from geometry import model
from geometry import util
import numpy as np
import math


class HumanModel(model.Model, game_object.GameObject):
    def __init__(self, position=np.zeros(3), angle=0, scale=np.ones(3)):
        super().__init__(position, angle, scale)

        self.right_arm_angle = 0
        self.wave_progress = 0
        self.target_yaw = 0
        self.arm_movement = True
        self.waving = False
        self.ticks = 0

    def tick(self):
        self.ticks += 1
        if not self.waving:
            self.wave_progress = 0
            self.right_arm_angle = 0
            return

        self.wave_progress += 1
        if self.wave_progress >= 500:
            if self.right_arm_angle > 5:
                self.right_arm_angle -= 5
            else:
                self.waving = False
                self.right_arm_angle = 0
            return

        # Check if we should turn toward the player.
        if self.wave_progress == 1:
            # Get the angle between X/Z coordinates
            difference = player.PLAYER_OBJECT.position[::2] - self.position[::2]
            difference = difference / np.linalg.norm(difference)
            self.target_yaw = math.degrees(math.atan2(difference[0], difference[1])) + 90

        if self.target_yaw != self.angle:
            if abs(self.target_yaw - self.angle) < 5:
                self.angle = self.target_yaw
            else:
                movement = (self.target_yaw - self.angle) / 5
                self.angle += movement
            return

        # Raise the arm.
        if self.arm_movement:
            if self.right_arm_angle > 170:
                self.arm_movement = False
            else:
                self.right_arm_angle += 2
        else:
            if self.right_arm_angle < 120:
                self.arm_movement = True
            else:
                self.right_arm_angle -= 2
        return

    def start_waving(self):
        if not self.waving:
            self.waving = True


def draw_head(human: HumanModel) -> None:
    # Draw the head.
    glPushMatrix()
    util.set_mat([1, 1, 0, 1.])
    glTranslatef(0, 1.5, 0)
    glRotatef(-90, 1, 0, 0)
    glutSolidCylinder(0.25, 0.5, 50, 50)
    glPopMatrix()

    # Draw the ears
    glPushMatrix()
    util.set_mat([1, 1, 1, 1.])
    glTranslatef(0, 1.75, -0.25)
    glutSolidSphere(0.1, 5, 5)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0, 1.75, 0.25)
    glutSolidSphere(0.1, 20, 20)
    glPopMatrix()

    # Draw the eyes
    glPushMatrix()
    util.set_mat([1, 1, 1, 1.])
    glTranslatef(-0.25, 1.75, -0.125)
    glutSolidSphere(0.05, 5, 5)
    glPopMatrix()
    glPushMatrix()
    util.set_mat([1, 1, 1, 1.])
    glTranslatef(-0.25, 1.75, 0.125)
    glutSolidSphere(0.05, 20, 20)
    glPopMatrix()


def draw_torso(human: HumanModel) -> None:
    util.set_mat([0., 0., 1., 1.])
    glTranslatef(0, 1, 0)
    glScalef(0.5, 1, 1)
    glutSolidCube(1)


def draw_leg(human: HumanModel, offset) -> None:
    util.set_mat([0., 0., 1., 1.])
    glTranslatef(*offset)
    glScalef(0.25, 1, 0.25)
    glutSolidCube(1)


def draw_left_arm(human: HumanModel) -> None:
    util.set_mat([0., 0., 1., 1.])
    glTranslatef(0, 1, 0.6325)
    glScalef(0.25, 1, 0.25)
    glutSolidCube(1)


def draw_right_arm(human: HumanModel) -> None:
    glTranslatef(0, 1.5, -0.6325)
    glRotatef(human.right_arm_angle, 1, 0, 0)
    glTranslatef(0, -0.5, 0)
    glScalef(0.25, 1, 0.25)

    # Try to rotate
    util.set_mat([0, 0, 1, 1.])
    glutSolidCube(1)


def draw_human(human: HumanModel) -> None:
    glPushMatrix()

    util.set_mat([0.7, 0.7, 0.7, 1.])

    glTranslatef(*human.position)
    glRotatef(human.angle, 0, 1, 0)
    glScalef(*human.scale)
    glPushMatrix()
    draw_head(human)
    glPopMatrix()

    glPushMatrix()
    draw_torso(human)
    glPopMatrix()

    glPushMatrix()
    draw_leg(human, [0, 0, -0.25])
    glPopMatrix()

    glPushMatrix()
    draw_leg(human, [0, 0, 0.25])
    glPopMatrix()

    glPushMatrix()
    draw_left_arm(human)
    glPopMatrix()

    glPushMatrix()
    draw_right_arm(human)
    glPopMatrix()
    glPopMatrix()
