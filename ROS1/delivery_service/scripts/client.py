#!/usr/bin/env python3

import sys
import rospy
from delivery_service.srv import *

def delivery_client(x):
    rospy.wait_for_service('feed_delivery')
    try:
        feed = rospy.ServiceProxy('feed_delivery', FeedDelivery)
        resp1 = feed(x)
        return resp1.Status
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x] ; Enter quantity atleast and atmost once"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = int(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting FeedDelivery Service for quantity of %s"%x)
    print("Delivery Status : %s"%(delivery_client(x)))
