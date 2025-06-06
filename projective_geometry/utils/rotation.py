import numpy as np
from scipy.spatial.transform import Rotation


def rotation_matrix_from_angles(rx, ry, rz):
    return Rotation.from_euler("xyz", [rx, ry, rz], degrees=True).as_matrix()


def angles_from_rotation_matrix(R, tol=1e-6):
    # For Gimbal lock, we force roll=0
    # https://en.wikipedia.org/wiki/Rotation_matrix#General_rotations
    if np.abs(np.abs(R[2, 0]) - 1) < tol:
        ry = -np.sign(R[2, 0]) * 90
        rx = 0
        rz = np.rad2deg(np.arctan2(R[0, 1] * R[2, 0], R[0, 2]))
    else:
        rx, ry, rz = Rotation.from_matrix(R).as_euler("xyz", degrees=True)
    return rx, ry, rz
