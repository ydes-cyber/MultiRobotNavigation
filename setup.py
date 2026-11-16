from setuptools import setup
from glob import glob
import os

package_name = 'cooperative_exploration'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'robot_controller',
        'sensor_processing',
        'frontier_detection',
        'task_allocator',
        'map_manager',
        'communication',
        'exploration_coordinator',
        'metrics',
    ],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'),
         glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Project Maintainer',
    maintainer_email='maintainer@example.com',
    description='Cooperative multi-robot exploration using ROS 2 Jazzy',
    license='MIT',
    entry_points={
        'console_scripts': [
            'robot_controller = robot_controller:main',
            'sensor_processing = sensor_processing:main',
            'map_manager = map_manager:main',
            'robot_communication = communication:main',
            'exploration_coordinator = exploration_coordinator:main',
        ],
    },
)
