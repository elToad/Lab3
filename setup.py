from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'joint_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include ALL files in urdf directory
        (os.path.join('share', package_name, 'urdf'), 
            glob('urdf/*')),
        # Include launch files
        (os.path.join('share', package_name, 'launch'), 
            glob('launch/*.py')),
        # Include config files
        (os.path.join('share', package_name, 'config'), 
            glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='toad',
    maintainer_email='tobiasnl@hotmail.no',
    description='Joint mechanism description package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)