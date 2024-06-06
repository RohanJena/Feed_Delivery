# Feed_Delivery

## Objective:-
The objective of the task was to develop a ROS service and client system that 
simulates a basic fleet management system. The client sends a request of 
delivery and the service responds to the request.
[See Documentaion](https://drive.google.com/file/d/1MxKEmXAqXmxK5CmgNfMRCJ4xCuGZI67z/view?usp=drive_link)

## Implementation:-

A service in ROS is a communication mechanism that allows nodes to send a 
request and receive a response. It is useful for tasks that are well defined and 
can be completed relatively quickly. ROS services are defined by a pair of 
message type one for the request and one for the response of the request. The 
message type is defined inside a .srv file.
A client in ROS is a node that requests a service. The client sends a request
message to the service server and waits for a response. Clients can be any ROS 
node, such as a robot controller, a sensor interface, or a user interface.

### 1.	ROS1 :-
System Specification:- ROS1 Noetic running on Ubuntu 20.04.
Steps:- 
-	 A package named delivery_service was built inside a ROS workspace with dependencies:- message_generation, std_msgs, rospy.
-	Inside the package a directory named srv was created which contained the FeedDelivery.srv file. Int32 datatype was used for the incoming query for number of feeds while string datatype was set as output.
-	Follwing this inside the scripts directory of the package two ROS nodes were created with file names as server.py and client.py.
-	The client node takes input using system arguments from the command line. The request is them sent to the service when available which returns a string in response: “Success” meaning the delivery was success and “Insufficient Feed” informing that the feed present is not enough to fulfil the clients request.
-	In the Server node, the service is initialised and continuously kept spinning for receiving the request. An internal counter names self.int_ctr was initialised with a default value of 10. This internal counter can be dynamically updated using dynamic_reconfiguration and rqt_reconfiguration node.
-	The parameters were updated in the Cmakelist and package.xml file

    ### How to run the nodes:-
-	The package contains a launch file which initiated the Dynamic Reconfigure Node along with service node and the type the following commands in separate terminals to initiate the Service Client.	

        roslaunch delivery_service 
        rosrun delivery_service client.py 7

    Where 7 is feed quantity specified feed quantity.
-	Change the slider value to dynamically increase the feed using rqt_reconfigure.

[Link for ROS1 task video solution]( https://drive.google.com/file/d/1kbKI354APoEtuVnq4dy2fbdjsPEiT6pu/view?usp=sharing )

### 2.	ROS2:-
System Specification:- ROS2 Foxy running on Ubuntu 20.04
Steps:-
-	A package named delivery_services was created with with build type as lament_cmake. Inside the package a directory called srv was created which contained FeedDelivery.srv file similar to the process done in ROS1.
-	Changes were done in the CmakeList and package.xml file in order to the perceive it as a service.
-	Next another package named srv_cli was created with build type as lament_python.
-	Now inside the directory named the same as that of the package service and client nodes were defined.
-	In a similar fashion as in the ROS1 approach the client node takes input using system arguments from the command line. The request is them sent to the service when available which returns a string in response: “Success” meaning the delivery was success and “Insufficient Feed” informing that the feed present is not enough to fulfil the clients request.
-	However the internal counter that contained the amount of remaining feed was declared as a ROS2 Parameter which can be modified whenever required to update the feed.
How to run the nodes:-
-	In two separate terminals run the following commands to run the nodes. Specify the feed quantity while running the client node.

        ros2 run srv_cli additional_service
        ros2 run srv_cli additional_client 8

-	You can increase the value of the internal counter by using the following command in separate terminal.

        ros2 param set /feed_delivery_service initial_feed 10

[Link for ROS2 task video solution]( https://drive.google.com/file/d/1lXknmT0MxECznBpVd-pXU5Ut-E3ZMW_A/view?usp=sharing )