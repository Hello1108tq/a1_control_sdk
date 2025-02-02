# 关节与末端移动接口

## 目录
- [关节与末端移动接口](#关节与末端移动接口)
  - [目录](#目录)
  - [项目介绍](#项目介绍)
  - [末端移动示例](#末端移动示例)
    - [使用如影片所示](#使用如影片所示)
  - [末端轨迹移动示例](#末端轨迹移动示例)
    - [实际效果如影片所示](#实际效果如影片所示)
  - [关节移动示例](#关节移动示例)

## 项目介绍
本项目旨在提供a1机械臂的关节与末端移动控制接口，通过ROS系统实现机械臂的高效控制。无论是末端移动还是关节移动，均需先启动signal_arm接口，详细操作参见signal_arm文档。本项目包含以下几个主要功能：

- **末端移动**：允许用户通过发布目标姿态消息来控制机械臂末端的位置和方向，适用于需要精确定位的应用。
- **末端轨迹移动**：通过发布一系列姿态消息，实现机械臂末端沿特定轨迹移动，适用于复杂路径规划和执行。
- **关节移动**：提供关节级别的控制接口，用户可以设置每个关节的目标位置，从而实现机械臂的整体协调运动。

## 末端移动示例

先启动末端移动脚本, 这会开启一个a1机械臂的rviz, 默认在关节位置在零点。

```bash
cd release/install
source setup.bash
roslaunch mobiman eeTrackerdemo.launch

```
该launch档中
```
<param name="joint_states_topic" value="/joint_states" />
```
/joint_states代表拿仿真的值的topic
```
<param name="joint_command" value="/a1_robot_right/arm_joint_command" />
```
/a1_robot_right/arm_joint_command代表要发布的电机topic

发布消息给末端移动,该消息名称是/a1_mpc_target, 这是非阻塞式的, 可以连续发布, 机械臂末端就可
以连续动, 注意这个末端别离当前的机械臂末端太远

```
rostopic pub /a1_mpc_target geometry_msgs/PoseStamped "{
header: {
seq: 0,
stamp: {secs: 0, nsecs: 0},
frame_id: 'world'
},
pose: {
position: {x: 0.08, y: 0.0, z: 0.5},
orientation: {x: 0.5, y: 0.5, z: 0.5, w: 0.5}
}
}"
```

```
#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
def publish_pose():
rospy.init_node('pose_stamped_publisher', anonymous=True)
pose_pub = rospy.Publisher('/a1_mpc_target', PoseStamped, queue_size=10)
# 创建PoseStamped消息
pose_msg = PoseStamped()
pose_msg.header.seq = 0
pose_msg.header.stamp = rospy.Time.now()
pose_msg.header.frame_id = 'world'
pose_msg.pose.position.x = 0.
pose_msg.pose.position.y = 0.
pose_msg.pose.position.z = 0.
pose_msg.pose.orientation.x = 0.
pose_msg.pose.orientation.y = 0.
pose_msg.pose.orientation.z = 0.
pose_msg.pose.orientation.w = 0.
# 等待订阅者连接
rospy.sleep(1)
# 发布消息
pose_pub.publish(pose_msg)
rospy.loginfo("Published PoseStamped message to /a1_mpc_target")
if __name__ == '__main__':
try:
publish_pose()
except rospy.ROSInterruptException:
pass
```

### 使用如影片所示

<video width="600" controls>
  <source src="install/resource/eeDemo.mp4" type="video/mp4">
</video>

## 末端轨迹移动示例

先启动末端轨迹移动脚本,这会开启一个a1机械臂的rviz,默认在关节位置在零点

```
cd release/install
source setup.bash
roslaunch mobiman eeTrajTrackerdemo.launch
```

该launch档中
```
<param name="joint_states_topic" value="/joint_states" />
```
/joint_states代表拿仿真的值的topic
```
<param name="joint_command" value="/a1_robot_right/arm_joint_command" />
```
/a1_robot_right/arm_joint_command代表要发布的电机topic
发布消息给末端移动指定轨迹,注意该轨迹不可以偏离当前末端点,该消息名称
是/arm_target_trajectory,这是非阻塞式的,可以连续发布,但建议等轨迹移动完再发布,以免追踪不准

```
int main(int argc, char** argv)
{
ros::init(argc, argv, "pose_array_publisher");
ros::NodeHandle nh;
ros::Publisher pose_pub = nh.advertise<geometry_msgs::PoseArray>
("/arm_target_trajectory", 10);
// 等待订阅者连接
ros::Rate wait_rate(10);
while (pose_pub.getNumSubscribers() == 0)
{
wait_rate.sleep();
}
geometry_msgs::PoseArray poseArrayMsg;
geometry_msgs::Pose pose1;
pose1.position.x = 0.08;
pose1.position.y = 0.0;
pose1.position.z = 0.3;
pose1.orientation.w = 0.5;
pose1.orientation.x = 0.5;
pose1.orientation.y = 0.5;
pose1.orientation.z = 0.5;
geometry_msgs::Pose pose2;
pose2.position.x = 0.08;
pose2.position.y = 0.0;
pose2.position.z = 0.4;
pose2.orientation.w = 0.5;
pose2.orientation.x = 0.5;
pose2.orientation.y = 0.5;
pose2.orientation.z = 0.5;
geometry_msgs::Pose pose3;
pose3.position.x = 0.08;
pose3.position.y = 0.0;
pose3.position.z = 0.54;
pose3.orientation.w = 0.5;
pose3.orientation.x = 0.5;
pose3.orientation.y = 0.5;
pose3.orientation.z = 0.5;
poseArrayMsg.poses.push_back(pose1);
poseArrayMsg.poses.push_back(pose2);
poseArrayMsg.poses.push_back(pose3);
pose_pub.publish(poseArrayMsg);
ROS_INFO("Published PoseArray with 3 poses");
return 0;
}
```
### 实际效果如影片所示
<video width="600" controls>
  <source src="install/resource/eeTrajTrackerdemo.mp4" type="video/mp4">
</video>


## 关节移动示例

先启动关节移动脚本,这会开启一个a1机械臂的rviz,默认在关节位置在零点

```
cd release/install
source setup.bash
roslaunch mobiman jointTrackerdemo.launch
```
该launch档中
```
<param name="joint_states_topic" value="/joint_states" />
```
/joint_states代表拿仿真的值的topic
```
<param name="joint_command" value="/a1_robot_right/arm_joint_command" />
```
/a1_robot_right/arm_joint_command代表要发布的电机topic


发布消息给关节移动,该消息名称是/arm_joint_target_position,这是非阻塞式的,可以连续发布,机械臂关节可以连续动
```
import rospy
from sensor_msgs.msg import JointState
def publish_joint_state():
rospy.init_node('joint_state_publisher', anonymous=True)
pub = rospy.Publisher('/arm_joint_target_position', JointState,
queue_size=10)
rate = rospy.Rate(10) # 10 Hz
joint_state = JointState()
joint_state.header.seq = 0
joint_state.header.stamp = rospy.Time.now()
joint_state.header.frame_id = 'world'
joint_state.name = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5',
'joint6']
joint_state.velocity = []
joint_state.effort = []
# Initialize positions to zeros
joint_state.position = [0, 0, 0, 0, 0, 0]
steps = 100 # Number of steps to reach the target position
target_position = [0.5, 0, 0, 0, 0, 0]
step_increment = [(target - current) / steps for target, current in
zip(target_position, joint_state.position)]
for step in range(steps):
joint_state.header.stamp = rospy.Time.now() # Update the timestamp
joint_state.position = [current + increment for current, increment in
zip(joint_state.position, step_increment)]
pub.publish(joint_state)
rate.sleep()
# Ensure final target position is reached
joint_state.position = target_position
pub.publish(joint_state)
if __name__ == '__main__':
try:
publish_joint_state()
except rospy.ROSInterruptException:
pass
```
