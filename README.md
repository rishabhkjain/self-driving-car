# self_driving_car
ROS Project built for augmenting a remote controlled car with self driving capabilities

Hardware Used: 

New Bright RC Car
Raspberry Pi
PS Eye Monocular Camera 


Note: While testing, an Arduino connected to the computer is used instead of theRPi 

The RPi/Arduino control the car by sending signals to the remote control board. By emulating button presses, we are able to control the car using its original controller and do not need to make additional changes. 

Issues encountered along the way 
- Needed to manually set 'ROS_IP' and 'ROS_HOSTNAME' on both my computer and the RPi to get messages to robustly send 
- Ubuntu image requires some additional work to give the user access to the GPIOpins. Needed to add the user in a gpio group which has permissions on 'dev/gpiomem'  
