#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn, Kill

class TurtleSubscriber(Node):

    def __init__(self):
        super().__init__('turtlebot_subscriber')
        self.publisher_ = self.create_publisher(Twist, 'rt1_turtle/cmd_vel', 10)
        self.subscription_ = self.create_subscription(
            Pose, 'rt1_turtle/pose', self.listener_callback, 10)
        self.subscription_ # prevent unused variable warning
        self.kill_client = self.create_client(Kill, '/kill')
        self.spawn_client = self.create_client(Spawn, '/spawn')

    def listener_callback(self, msg):
        self.get_logger().info(
            'Turtle subscriber@[%f, %f, %f]' % (msg.x, msg.y, msg.theta))

        my_vel = Twist()
        if msg.x > 9.0:
            my_vel.linear.x = 1.0
            my_vel.angular.z = 1.0

        elif msg.x < 1.5:
            my_vel.linear.x = 1.0
            my_vel.angular.z = -1.0

        else:
            my_vel.linear.x = 1.0
            my_vel.angular.z = 0.0

        self.publisher_.publish(my_vel)



def main(args=None):

    rclpy.init(args=args)
    turtle_subscriber = TurtleSubscriber()

    # Kill the turtle
    while not turtle_subscriber.kill_client.wait_for_service(timeout_sec=1.0):
        turtle_subscriber.get_logger().info('service not available, waiting...')

    request = Kill.Request()
    request.name = "turtle1"
    future = turtle_subscriber.kill_client.call_async(request )
    rclpy.spin_until_future_complete(turtle_subscriber, future)

    # Spawn a new turtle
    while not turtle_subscriber.spawn_client.wait_for_service(timeout_sec=1.0):
        turtle_subscriber.get_logger().info('service not available, waiting...')
    spawn_request = Spawn.Request()
    spawn_request.x = 1.5
    spawn_request.y = 1.5
    spawn_request.theta = 0.0
    spawn_request.name = "rt1_turtle"
    spawn_future = turtle_subscriber.spawn_client.call_async(spawn_request)
    rclpy.spin_until_future_complete(turtle_subscriber, spawn_future)
  
    rclpy.spin(turtle_subscriber)
    turtle_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
