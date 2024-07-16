import rospy
import time
from sensor_msgs.msg import JointState
#from mobiman_msgs.msg import ArmBasicCommand
from signal_arm.msg import arm_control

class JointStateData:
    def __init__(self):
        self.joint_states = JointState()
        self.joint_states.header.seq = 0
        self.joint_states.header.stamp = rospy.Time.now()
        self.joint_states.name = ['arm_joint1', 'arm_joint2', 'arm_joint3', 'arm_joint4', 'arm_joint5', 'arm_joint6']
        self.joint_states.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.joint_states.velocity = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.joint_states.effort = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        self.joint_states_sub = rospy.Subscriber('/arm_joint_command_slave', arm_control, self.updatestatusCallback)

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
    rospy.init_node('a1_dummy_slave_node', anonymous=True)
    joint_state_ = JointStateData()
    rate = rospy.Rate(500)  # 每秒发布一次消息
    pub = rospy.Publisher('/joint_states_slave', JointState, queue_size=10)
    while not rospy.is_shutdown():
        pub.publish(joint_state_.get_joint_states())
        rate.sleep()

if __name__ == '__main__':
    try:
        dummy_node()
    except rospy.ROSInterruptException:
        pass