# reto_ros
This a challenge provided by the playtec enterprise.

Details:

1.Topic publisher:

To access to this file launch the topic_pub.launch.

![fi](https://user-images.githubusercontent.com/59718261/80871992-c35d7b80-8c74-11ea-9286-2b82751c97c0.png)

2.Topic subscriber:

You can see the message the publish the topic publisher with "rostopic echo /reto",
the launcher is topic_pub.launch.

![image](https://user-images.githubusercontent.com/59718261/80871983-b476c900-8c74-11ea-9a3f-215ba78df878.png)


3.Launchers files:

These are the files that we have to launch if we want to try this project:

![vas](https://user-images.githubusercontent.com/59718261/80872455-b0987600-8c77-11ea-9faf-9f6006d50700.png)

4.Robot URDF :

This is the robot created in URDF and shown in Rviz.

![RVIZ](https://user-images.githubusercontent.com/59718261/80872373-1afce680-8c77-11ea-93d3-1434e5593062.png)


5.PointCloud challenge:

Create a publisher with CloudPoint2 msg.

![cloud](https://user-images.githubusercontent.com/59718261/80872423-80e96e00-8c77-11ea-9474-f74e1496a343.png)

![ba](https://user-images.githubusercontent.com/59718261/80872507-fce3b600-8c77-11ea-817f-9b6ac1fbb4ce.png)

BB8_SIMULATION_WITH_ARDUINO:
If you want to use it use the bb8.launch file that it's in the bb8_gazebo's folder.

![varb](https://user-images.githubusercontent.com/59718261/80872750-93fd3d80-8c79-11ea-8ae9-4026d981fda1.png)

If you wan to move the robot you can publish into the /cmd_vel with geometry_msgs for that you have to use "rostopic pub /cmd_vel geometry_msgs/Twist [TAB]+[TAB]" , you have to push two times TAB after copy that.

![top](https://user-images.githubusercontent.com/59718261/80872821-08d07780-8c7a-11ea-860d-56be9a021dbd.png)

![Peek 2020-05-02 13-42](https://user-images.githubusercontent.com/59718261/80872951-db37fe00-8c7a-11ea-83ea-ad8550404aae.gif)

The last step is to use the IDE ARDUINO and upload the code that is in the Move Folder.



