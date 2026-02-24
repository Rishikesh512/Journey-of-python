def calculate_total(price,quantity):
    return price*quantity

def calculate_gst(total):
    return total*0.18

def print_bill(price,quantity,total,gst,final_amount):

    print("\n------BILL------")
    print("Price per item :",price)
    print("Quantity :",quantity)
    print("Total :",total)
    print("GST(18%) :",gst)
    print("Final Amount :",final_amount)
    print("Thank you")
    print("Visit Again")
    print("---------------------------------")


def main():
    price = float(input(" Enter the price of item:"))

    quantity = int(input("quantity:"))

    total = calculate_total(price,quantity)
    gst = calculate_gst(total)
    final_amount = total+gst

    print_bill(price,quantity,total,gst,final_amount)

main()