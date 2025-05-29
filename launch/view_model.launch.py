from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import LogInfo
import os
import xacro

def generate_launch_description():
    # Get package share directory
    pkg_share = get_package_share_directory('joint_description')
    
    # Path to the XACRO file
    xacro_path = os.path.join(pkg_share, 'urdf', 'joint_model.urdf.xacro')

    # Process Xacro to URDF
    robot_description = xacro.process_file(xacro_path).toxml()

    # Get RViz config path
    rviz_config_path = os.path.join(pkg_share, 'config', 'config.rviz')

    # Log info
    log = LogInfo(msg=f"Using Xacro file: {xacro_path}")

    return LaunchDescription([
        log,
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        )
    ])