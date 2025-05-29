from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch.actions import LogInfo
import xacro

def generate_launch_description():
    # Path to the URDF file
    urdf_path = os.path.join(
        get_package_share_directory('joint_description'),
        'urdf',
        'joint_model.urdf'
    )

    xacro_file = os.path.join(get_package_share_directory("joint_description"),"urdf","joint_model.urdf")
    robot_description_content = xacro.process_file(xacro_file).toxml()  

    log = LogInfo(msg=os.path.join(get_package_share_directory("joint_description"), 'config', 'config.rviz'))
    

    return LaunchDescription([log,
        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description_content}]
        ),
        
        # RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', [os.path.join(get_package_share_directory("joint_description"), 'config', 'config.rviz')]]
        )
    ])