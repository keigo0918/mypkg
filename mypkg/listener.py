import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def main():
    rclpy.init()
    node = Node("listener")
    client = node.create_client(Query, 'query')
    while not client.wait_for_service(timeout_sec=0.5):
        node.get_logger().info('待機中')

    req = Query.Request()
    req.name = "上田隆一"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('')
            else:
                node.get_logger().info("age: {}".format(response.age))

            break

    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
