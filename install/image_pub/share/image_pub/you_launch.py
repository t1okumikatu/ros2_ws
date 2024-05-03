
from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
   return LaunchDescription([ 
     Node(
       package='image_pub',
       executable='img_publisher',  #razpaiからの受信 3
     ),
     Node(
       package='robot_controller', 
       executable='robot_controller_action', #ノートから送信 4
     ),
   ])

