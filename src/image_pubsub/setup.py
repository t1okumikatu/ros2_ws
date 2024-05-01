from setuptools import find_packages, setup
<<<<<<< HEAD
from glob import glob
import os 
=======
import os
>>>>>>> 535e23d86d06c52a8eff0f96d95afbb6a935038f
package_name = 'image_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
<<<<<<< HEAD
        (os.path.join('share', package_name), glob('launch/*.py'))
=======
        (os.path.join('share', package_name),
        glob('launch/my_launch.py')),
>>>>>>> 535e23d86d06c52a8eff0f96d95afbb6a935038f
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
