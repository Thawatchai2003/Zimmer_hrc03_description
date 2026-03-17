from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    urdf_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'urdf',
        'HRC-03-118505(10)HRC-03_v1.urdf'
    )

    with open(urdf_path, 'r') as f:
        robot_desc = f.read()

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}]
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),

        Node(
            package='rviz2',
            executable='rviz2'
        )
    ])
