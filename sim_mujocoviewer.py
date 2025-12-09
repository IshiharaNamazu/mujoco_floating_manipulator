import mujoco
import mujoco.viewer
import xacro
import time

model = mujoco.MjModel.from_xml_string(xacro.process_file("test_sat.xacro").toxml())
data = mujoco.MjData(model)

# 'stationary' キーフレームの状態でシミュレーションを開始
mujoco.mj_resetDataKeyframe(model, data, model.keyframe('stationary').id)

# インタラクティブビューアを起動
with mujoco.viewer.launch_passive(model, data) as viewer:
  # ビューアが起動している間、シミュレーションを実行
  while viewer.is_running():
    step_start = time.time()
    mujoco.mj_step(model, data)
    viewer.sync()