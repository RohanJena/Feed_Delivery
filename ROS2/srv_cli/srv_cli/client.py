import sys
from delivery_services.srv import FeedDelivery
import rclpy
from rclpy.node import Node


class DeliveryClient(Node):

    def __init__(self):
        super().__init__('feed_delivery_client_async')
        self.cli = self.create_client(FeedDelivery, 'feed_delivery')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = FeedDelivery.Request()

    def send_request(self, a):
        self.req.quantity = a
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)

    del_client = DeliveryClient()
    response = del_client.send_request(int(sys.argv[1]))
    del_client.get_logger().info(
        'Delivery Status for feed quantity of %d : %s' %
        (int(sys.argv[1]), response.status))
    print("-"*40)
    del_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()