from setuptools import find_packages, setup

package_name = 'image_pub' #raspi

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #(os.path.join('share', package_name), glob('launch/*.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='keime',
    maintainer_email='keime@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ #raspi
            'img_publisher = image_pub.image_publisher:main',
            'action = robot_controller.command_subscriber_action:main',
        ],
    },
)
