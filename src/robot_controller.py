"""ROS 2 node responsible for controlling one robot."""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseStamped


class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')

        # TODO: Declare configurable parameters.
        # TODO: Create velocity publisher.
        # TODO: Create exploration target subscriber.
        # TODO: Initialize current robot state.

    def publish_velocity(self, linear: float, angular: float) -> None:
        """Publish a velocity command to the robot."""
        # TODO: Construct and publish Twist message.
        pass

    def receive_target(self, msg: PoseStamped) -> None:
        """Receive an assigned exploration target."""
        # TODO: Store target coordinates.
        # TODO: Trigger navigation toward target.
        pass

    def calculate_velocity(self) -> Twist:
        """Calculate velocity required to reach current target."""
        # TODO: Calculate distance and heading error.
        # TODO: Apply proportional control.
        pass

    def stop_robot(self) -> None:
        """Stop robot movement."""
        # TODO: Publish zero velocity.
        pass

    def control_loop(self) -> None:
        """Execute periodic movement control."""
        # TODO: Calculate and publish velocity.
        pass


def main(args=None):
    rclpy.init(args=args)
    node = RobotController()

    try:
        rclpy.spin(node)
    finally:
        node.stop_robot()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
