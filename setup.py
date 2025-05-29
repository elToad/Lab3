from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'joint_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include URDF file
        (os.path.join('share', package_name, 'urdf'), ['urdf/joint_model.urdf']),
        # Include launch file
        (os.path.join('share', package_name, 'launch'), ['launch/view_model.launch.py']),
        # Include RViz config (if needed)
        #(os.path.join('share', package_name, 'config'), ['config/view_robot.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='toad',
    maintainer_email='tobiasnl@hotmail.no',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)