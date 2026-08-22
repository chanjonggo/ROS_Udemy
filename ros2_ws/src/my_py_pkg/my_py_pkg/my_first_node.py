#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

#template Code 
class MyNode(Node):
    def __init__(self):
        #first arg pass node_name
        super().__init__("py_test")
        self.counter = 0
        self.get_logger().info("Hello class world")
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("tick tock " + str(self.counter))
        self.counter += 1


def main(args=None):
    #start
    rclpy.init(args=args)

    #create node
    node = MyNode()
    #node = Node("py_test")
    #node.get_logger().info("Hello world")

    #spin - keep node lives
    rclpy.spin(node)

    #end
    rclpy.shutdown() 
if __name__ == "__main__":
    main()