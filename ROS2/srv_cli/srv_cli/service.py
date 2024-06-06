import rclpy
from rclpy.node import Node
from delivery_services.srv import FeedDelivery

class DeliveryServer(Node):

    def __init__(self):
        super().__init__('feed_delivery_service')
        self.declare_parameter('initial_feed')
        self.int_ctr = 10
        self.srv = self.create_service(FeedDelivery, 'feed_delivery', self.delivery_callback)

    def delivery_callback(self, request, response):
        self.int_ctr += self.get_parameter('initial_feed').get_parameter_value().integer_value
        print(self.int_ctr)
        self.get_logger().info('Incoming request\nquantity: %d ' % (request.quantity))
        if(self.int_ctr>=request.quantity):
            self.int_ctr-=request.quantity
            response.status="Success"
            print("-"*40)
            return response
        else:
            response.status="Insufficient Feed"
            return response

def main(args=None):
    rclpy.init(args=args)
    del_srv = DeliveryServer()
    rclpy.spin(del_srv)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
