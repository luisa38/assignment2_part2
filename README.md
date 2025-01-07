# Part 2 - Assignment 2 - Research Track 1

## Description
This ROS2 package ccontrols the movement of a turtle in the Turtlesim simulator. The package performs the following tasks:
1. Removes the default turtle (`turtle1`).
2. Spawns a new turtle named `rt1_turtle` at a defined starting position.
3. Moves the turtle along the X-axis and performs smooth turns upon reaching limits.

## Package Structure
- **controller_node.py**: Contains the logic to control the turtle's movement.
- **package.xml**: ROS2 package configuration file.
- **setup.py**: Setup file for installing the ROS2 package.

## How to Use
1. Compile the package:
   ```bash
   cd ~/ros/ros2_ws/
   colcon build --packages-select turtle_basic_controller
   source install/setup.bash
   ```
2. Launch the Turtlesim simulator:
  ```bash
  ros2 run turtlesim turtlesim_node
  ```

3. Start the controller node:
  ```bash
  ros2 run assignment_2_turtlesim_ros2 controller_node
  ```

## Expected Behaviour
* The default turtle is removed
* The turtle moves forward along the X-axis until it reaches the limits (x > 9.0 or x < 1.5).
* Upon reaching the limits, the turtle performs turns to cover the whole area.
