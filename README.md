# EN.601.654 Introduction to Augmented Reality – Assignment 3

**Author:** [Your Full Name] (JHED: jcheng77)

## Contents
- `Q2/` – WebXR AR app in Babylon.js for Meta Quest 3: hit-test placement of a `car.glb` model plus controller interaction, built up one sub-part per folder (`Q2b` spawn on trigger, `Q2c` + thumbstick move, `Q2d` + rotate, `Q2e` + A/B scale, `Q2f` + X reset — `Q2f` is the full version).
- `Q3e/` – `camera_projection.py`: builds the OpenGL projection matrix from camera intrinsics and takes a camera-space point through clip space → NDC → pixel `(u, v)`, with a pinhole sanity check.
- `Q4/` – Babylon.js Playground custom GLSL shaders: `4a.js` is the Phong vertex/fragment shader with one attenuated point light, `4c.js` adds a second (warm) point light; `index.html` is a standalone bundled page that runs the final scene outside the Playground.

Written answers are in the Gradescope PDF and are not included here.

## How to run

**Q3e (Python):**

    pip install numpy
    python Q3e/camera_projection.py                        # default point (0.3, -0.15, -6)
    python Q3e/camera_projection.py --point 0.3 -0.15 -6 --fx 800 --fy 800 --W 800 --H 600

**Q2 (WebXR, Meta Quest 3):** serve the repo over HTTPS (WebXR requires a secure context) and open `Q2/Q2f/` in the Quest browser, then press *Enter AR*:

    python -m http.server 8000      # then tunnel over HTTPS, e.g. ngrok http 8000

For desktop testing without a headset, append `?emulate` (e.g. `http://localhost:8000/Q2/Q2f/?emulate`) to load Meta's IWER Quest 3 emulator.

**Q4 (Babylon.js Playground):** open <https://playground.babylonjs.com>, paste the contents of `Q4/4a.js` or `Q4/4c.js`, and press Run. Alternatively serve the repo and open `Q4/index.html`, which runs the same scene from a bundled snapshot.
