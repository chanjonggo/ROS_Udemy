#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
 
class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station") 
        #create publisher 
        #arg 1 = data Type, arg2 = name , arg3 = size of network buffer
        self.publisher = self.create_publisher(String, "robot_news", 10)

    def publish_news(self):
        msg = String()
        msg.data = 

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
