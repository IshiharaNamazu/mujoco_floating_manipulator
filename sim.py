import mujoco
import mujoco.viewer
import mediapy as media
import xacro

model = mujoco.MjModel.from_xml_string(xacro.process_file("floating_manipulator.xacro").toxml())
data = mujoco.MjData(model)

# "spinning" キーフレームの状態でシミュレーションを開始
mujoco.mj_resetDataKeyframe(model, data, model.keyframe('stationary').id)

n_frames = 300
height = 720
width = 1280
frames = []

# インタラクティブビューアを起動
with mujoco.Renderer(model, height, width) as renderer:
  for i in range(n_frames):
    while data.time < i/30.0:
      mujoco.mj_step(model, data)
    renderer.update_scene(data, "overview")
    frame = renderer.render()
    frames.append(frame)

media.write_video('output/output.mp4', frames, fps=30)