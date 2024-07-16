#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from signal_arm.msg import gripper_joint_command
from signal_arm.msg import arm_control


def cmd_vel_callback(data):
    # 接收到 "cmd_vel" 消息后的回调函数
    # 在这里，你可以编写处理接收到的消息的代码
    # 对于这个示例，我们只是打印收到的消息

    cmd_msg = arm_control()
    cmd_msg.kp = [100]
    cmd_msg.kd = [0]
    cmd_msg.p_des = [-1.6]
    cmd_msg.v_des = [0]
    cmd_msg.t_ff = [0]
    if abs(data.linear.x) < 1.0:
        cmd_msg.t_ff = [0]
    else:
        cmd_msg.p_des = [data.angular.z]
        cmd_msg.t_ff = [data.linear.x]

    # 发布消息到 "/cmd" topic
    cmd_pub.publish(cmd_msg)

def cmd_vel_subscriber():
    # 初始化 ROS 节点
    rospy.init_node('cmd_vel_subscriber', anonymous=True)

    # 订阅名为 "cmd_vel" 的 topic，并指定消息类型为 Twist
    rospy.Subscriber("cmd_vel", Twist, cmd_vel_callback)

    # 循环等待接收消息
    rospy.spin()

if __name__ == '__main__':
    try:
        # 初始化一个发布者，用于发送消息到 "/cmd" topic
        cmd_pub = rospy.Publisher("/gripper_aloha_command_host", arm_control, queue_size=10)
        cmd_vel_subscriber()
    except rospy.ROSInterruptException:
        pass
