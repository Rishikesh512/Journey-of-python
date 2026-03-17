class Order:
    def order_info(self):
        print("Order placed")

class Delivery:
    def delivery_status(self):
        print("Out for delivery")

class OnlineOrder(Order, Delivery):
    pass

o = OnlineOrder()
o.order_info()
o.delivery_status()
