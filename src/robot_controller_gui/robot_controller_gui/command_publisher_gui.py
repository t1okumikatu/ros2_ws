<<<<<<< HEAD
def main():
    print('Hi from robot_controller_gui.')


if __name__ == '__main__':
    main()
=======
#ros
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
#pyqtGui
import sys
from .controller import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication

class CommandPublisherGui(QMainWindow):

    def __init__(self, parent=None):
        #GUI
        super(CommandPublisherGui, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #ros
        rclpy.init()
        self.node = Node('commander')
        self.publisher_ = self.node.create_publisher(Twist, 'cmd_vel', 10)
        self.vel = Twist()
        self.vel.linear.x = 0.0
        self.vel.angular.z = 0.0

    def fwrd(self):
        self.vel.linear.x += 0.1
        self.publisher_.publish(self.vel)

    def stop(self):
        self.vel.linear.x = 0.0
        self.vel.angular.z = 0.0
        self.publisher_.publish(self.vel)

    def bwrd(self):
        self.vel.linear.x -= 0.1
        self.publisher_.publish(self.vel)

    def ltrn(self):
        self.vel.angular.z += 0.1
        self.publisher_.publish(self.vel)

    def rtrn(self):
        self.vel.angular.z -= 0.1
        self.publisher_.publish(self.vel)
    
def main(args=None):
    app = QApplication(sys.argv)
    window = CommandPublisherGui()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

    
>>>>>>> 6fd6f515ef382b60d98de2f125d779f8e82fe435
