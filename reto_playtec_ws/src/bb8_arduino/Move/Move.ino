/* 
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <geometry_msgs/Twist.h>

ros::NodeHandle  nh;

geometry_msgs::Twist _move;

ros::Publisher chatter("cmd_vel",&_move);

bool getDir=0;
bool getRot=0;
int dir=8;
int rot=7;

void setup()
{ 
  pinMode(dir, INPUT_PULLUP);
  pinMode(rot, INPUT_PULLUP);
  
  nh.initNode();
  nh.advertise(chatter);
}

void loop()
{ 
  
  getDir=digitalRead(dir);
  getRot=digitalRead(rot);
  
  if(getDir){
    nh.loginfo("Avanzar");
    _move.linear.x=1.0;
  }

  else if(!getDir){
    _move.linear.x=0.0;
    nh.logwarn("No move");
  }
  
  if(getRot){
    nh.loginfo("Girar");
    _move.angular.z=1.0;
  }

  else if(!getRot){
    _move.angular.z=0.0;
    nh.logwarn("No turn");
  }

  chatter.publish(&_move);
  
  nh.spinOnce();
  delay(100);
}
