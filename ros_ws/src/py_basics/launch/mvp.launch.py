from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='py_basics', executable='talker', name='talker', output='screen'),
        Node(package='py_basics', executable='bridge', name='bridge', output='screen'),
    ])
