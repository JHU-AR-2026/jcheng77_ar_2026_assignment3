"""
Q3e - Camera point -> OpenGL clip space -> NDC -> pixel coordinates.

Conventions (as specified in Q3):
  * column vectors
  * camera looks along -Z (points in front of the camera have Z < 0)
  * pixel v increases with NDC y:  u = 0.5(x_ndc + 1)W,  v = 0.5(y_ndc + 1)H
"""
import argparse
import numpy as np


def projection_from_intrinsics(fx, fy, ox, oy, W, H, n, f):
    """Symbolic form (Q3a):
        [ 2fx/W    0      1 - 2ox/W        0       ]
        [   0    2fy/H    1 - 2oy/H        0       ]
        [   0      0    -(f+n)/(f-n)  -2fn/(f-n)   ]
        [   0      0         -1            0       ]
    """
    return np.array([
        [2 * fx / W, 0.0,        1 - 2 * ox / W,     0.0],
        [0.0,        2 * fy / H, 1 - 2 * oy / H,     0.0],
        [0.0,        0.0,        -(f + n) / (f - n), -2 * f * n / (f - n)],
        [0.0,        0.0,        -1.0,               0.0],
    ])


def camera_to_pixel(Pc, fx, fy, ox, oy, W, H, n, f):
    P = projection_from_intrinsics(fx, fy, ox, oy, W, H, n, f)
    Pc = np.asarray(Pc, dtype=float).reshape(4)
    clip = P @ Pc                       # clip-space coordinates
    if clip[3] <= 0:
        raise ValueError("Point is behind the camera (w_clip <= 0).")
    ndc = clip[:3] / clip[3]            # perspective divide
    u = 0.5 * (ndc[0] + 1.0) * W
    v = 0.5 * (ndc[1] + 1.0) * H
    return P, clip, ndc, np.array([u, v])


def main():
    ap = argparse.ArgumentParser(description="Camera point to pixel (OpenGL convention)")
    ap.add_argument("--point", nargs=3, type=float, default=[0.3, -0.15, -6.0],
                    metavar=("X", "Y", "Z"), help="camera-frame point")
    ap.add_argument("--fx", type=float, default=800); ap.add_argument("--fy", type=float, default=800)
    ap.add_argument("--ox", type=float, default=400); ap.add_argument("--oy", type=float, default=400)
    ap.add_argument("--W", type=float, default=800);  ap.add_argument("--H", type=float, default=600)
    ap.add_argument("--near", type=float, default=0.2); ap.add_argument("--far", type=float, default=20)
    a = ap.parse_args()

    P, clip, ndc, uv = camera_to_pixel([*a.point, 1.0], a.fx, a.fy, a.ox, a.oy,
                                       a.W, a.H, a.near, a.far)
    np.set_printoptions(precision=6, suppress=True)
    print("Projection matrix:\n", P)
    print("Clip coords :", clip)
    print("NDC         :", ndc)
    print("Pixel (u, v):", uv)

    # sanity check against the pinhole model directly
    X, Y, Z = a.point
    u_pin = a.fx * X / (-Z) + a.ox
    v_pin = a.fy * Y / (-Z) + a.oy
    assert np.allclose(uv, [u_pin, v_pin]), "mismatch with pinhole model"
    print("Pinhole check passed:", (u_pin, v_pin))


if __name__ == "__main__":
    main()
