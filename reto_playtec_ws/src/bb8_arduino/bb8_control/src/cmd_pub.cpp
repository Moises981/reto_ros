#include<ros/ros.h>
#include<geometry_msgs/Twist.h>
#include<std_msgs/Float64.h>

float move , turn;

void Callback(const geometry_msgs::Twist::ConstPtr &msg){
    move=msg->linear.x;
    turn=msg->angular.z;
}

int main(int argc , char** argv){
    ros::init(argc,argv,"control");
    ros::NodeHandle nh;
    ros::Subscriber sub= nh.subscribe("cmd_vel",1000,Callback);
    ros::Publisher pub_direction=nh.advertise<std_msgs::Float64>("/bb8/direction/command",1000);
    ros::Publisher pub_rotation=nh.advertise<std_msgs::Float64>("/bb8/rotation/command",1000);
    ros::Rate loop_rate(2);
    std_msgs::Float64 direction;
    std_msgs::Float64 rotation;
    
    while(ros::ok()){
        direction.data=move;
        rotation.data=turn;
        pub_direction.publish(direction);
        pub_rotation.publish(rotation);
        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}