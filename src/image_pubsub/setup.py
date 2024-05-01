from setuptools import find_packages, setup
import os
package_name = 'image_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name),
        glob('launch/my_launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='keime',
    maintainer_email='t1okumikatu@gamil.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'img_publisher = image_pubsub.image_publisher:main',
            'img_subscriber = image_pubsub.image_subscriber:main',
            'command_publisher_gui = robot_controller_gui.command_publisher_gui:main'
        ],
    },
)
