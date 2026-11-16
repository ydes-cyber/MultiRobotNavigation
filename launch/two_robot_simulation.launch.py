"""Launch the two-robot cooperative exploration system."""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    robot1 = Node(
        package='cooperative_exploration',
        executable='robot_controller',
        namespace='robot1',
        name='robot_controller',
        output='screen',
        parameters=['config/robot1.yaml']
    )

    robot2 = Node(
        package='cooperative_exploration',
        executable='robot_controller',
        namespace='robot2',
        name='robot_controller',
        output='screen',
        parameters=['config/robot2.yaml']
    )

    sensor1 = Node(
        package='cooperative_exploration',
        executable='sensor_processing',
        namespace='robot1',
        output='screen'
    )

    sensor2 = Node(
        package='cooperative_exploration',
        executable='sensor_processing',
        namespace='robot2',
        output='screen'
    )

    map_manager = Node(
        package='cooperative_exploration',
        executable='map_manager',
        output='screen'
    )

    communication = Node(
        package='cooperative_exploration',
        executable='robot_communication',
        output='screen'
    )

    coordinator = Node(
        package='cooperative_exploration',
        executable='exploration_coordinator',
        output='screen'
    )

    return LaunchDescription([
        robot1,
        robot2,
        sensor1,
        sensor2,
        map_manager,
        communication,
        coordinator
    ])
