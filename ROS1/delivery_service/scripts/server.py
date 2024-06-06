#!/usr/bin/env python3

from delivery_service.srv import FeedDelivery,FeedDeliveryResponse
import rospy
from dynamic_reconfigure.server import Server
from delivery_service.cfg import DynamicFeedConfig

class Delivery():
    def __init__(self):
        self.int_ctr=10
        rospy.init_node('FeedDelivery_server')
        srv = Server(DynamicFeedConfig, self.callback)

    def callback(self,config, level):
        if config['int_param']>0:
            rospy.loginfo("""Reconfigure Request: {int_param}""".format(**config))
            print("------Updated the feed------")
            self.int_ctr+=config['int_param']
        return config

    def handle_delivery(self,req):
        print("Processing Request for feed quantity : %s"%(req.quantity))
        if req.quantity>self.int_ctr:
            print("Completed")
            return FeedDeliveryResponse("Insufficient feed")
        else:
            print("Completed")
            print("-----------------------------------------------------------")
            self.int_ctr-=req.quantity
            return FeedDeliveryResponse("Success")     

    def FeedDelivery_server(self):
        s = rospy.Service('feed_delivery', FeedDelivery, self.handle_delivery)
        print("Waiting for feed...")
        rospy.spin()

if __name__ == "__main__":
    fd=Delivery()
    fd.FeedDelivery_server()