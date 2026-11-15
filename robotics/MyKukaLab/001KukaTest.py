import pybullet as p
import pybullet_data
import time
import math

# 1. 连接物理引擎（DIRECT为后台运行，GUI为可视化界面）
physicsClient = p.connect(p.GUI) 

# 2. 加载 PyBullet 自带的官方数据路径（包含地面、KUKA机械臂、各种物体）
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# 3. 加载地面和 KUKA 机械臂
planeId = p.loadURDF("plane.urdf")
# KUKA iiwa 的起始位置与姿态
kukaStartPos = [0, 0, 0]
kukaStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
kukaId = p.loadURDF("kuka_iiwa/model.urdf", kukaStartPos, kukaStartOrientation)

# 在机械臂前方放置一个红色小方块
cubeStartPos = [0.5, 0.0, 0.05]
cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
cubeId = p.loadURDF("cube.urdf", cubeStartPos, cubeStartOrientation, globalScaling=0.6)

# 假设从视觉/ML获取的目标抓取点坐标
target_x, target_y, target_z = 0.5, 0.0, 0.15

# 计算 KUKA 机械臂各关节的目标角度（KUKA iiwa 通常末端连杆索引是 6）
end_effector_link_index = 6
joint_angles = p.calculateInverseKinematics(
    kukaId, 
    end_effector_link_index, 
    [target_x, target_y, target_z]
)

# 将计算出的关节角度应用到机械臂上
for i, angle in enumerate(joint_angles):
    p.resetJointState(kukaId, i, angle)

