import rospy
import time
from sensor_msgs.msg import JointState
#from mobiman_msgs.msg import ArmBasicCommand
from signal_arm.msg import arm_control

class JointStateData:
    def __init__(self, robot_name):
        self.joint_states = JointState()
        self.joint_states.header.seq = 0
        self.joint_states.header.stamp = rospy.Time.now()
        if (robot_name == "a1_robot_left"):
            self.joint_states.name = ['left_arm_joint1', 'left_arm_joint2', 'left_arm_joint3', 'left_arm_joint4', 'left_arm_joint5', 'left_arm_joint6']
            self.joint_states_sub = rospy.Subscriber('/a1_robot_left/arm_joint_command', arm_control, self.updatestatusCallback)
        if (robot_name == "a1_robot_right"):
            self.joint_states.name = ['right_arm_joint1', 'right_arm_joint2', 'right_arm_joint3', 'right_arm_joint4', 'right_arm_joint5', 'right_arm_joint6']
            self.joint_states_sub = rospy.Subscriber('/a1_robot_right/arm_joint_command', arm_control, self.updatestatusCallback)

        self.joint_states.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.joint_states.velocity = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.joint_states.effort = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    def updatestatusCallback(self, data):
        ##print("Update Status")

        self.joint_states.position = data.p_des
        self.joint_states.velocity = data.v_des
        return

    def get_joint_states(self):
        self.joint_states.header.seq += 1
        self.joint_states.header.stamp = rospy.Time.now()
        return self.joint_states


def dummy_node():
    rospy.init_node('a1_dummy_node', anonymous=True)
    joint_state_left = JointStateData("a1_robot_left")
    joint_state_right = JointStateData("a1_robot_right")
    rate = rospy.Rate(500)  # 每秒发布一次消息
    left_pub = rospy.Publisher('/a1_robot_left/joint_states', JointState, queue_size=10)
    right_pub = rospy.Publisher('/a1_robot_right/joint_states', JointState, queue_size=10)
    while not rospy.is_shutdown():
        left_pub.publish(joint_state_left.get_joint_states())
        right_pub.publish(joint_state_right.get_joint_states())
        rate.sleep()

if __name__ == '__main__':
    try:
        dummy_node()
    except rospy.ROSInterruptException:
        pass