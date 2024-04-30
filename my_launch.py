from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
   return LaunchDescription([ 
     Node(
       package='image_pubsub',
       executable='img_subscriber',
     ), 
     Node(      
       package='robot_controller_gui', 
       executable='command_publisher_gui',
     ),
   ])

