from setuptools import setup

package_name = 'assignment_2_turtlesim_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ana',
    maintainer_email='up202004753@up.pt',
    description='ROS2 package for Turtlesim assignment',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'controller_node = assignment_2_turtlesim_ros2.controller_node:main',  # Verifique se isso está correto
        ],
    },
)

