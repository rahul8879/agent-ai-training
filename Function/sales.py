def calculate_order_total(price, quantity, discount=0):
    total = price * quantity
    return total - (total * discount)


def get_shipping_cost(total_weight):
    if total_weight <= 5:
        return 50.0, "Standard"
    elif total_weight < 20:
        return 100.0, "Express"
    else:
        return 200.0, "Next-Day"
    

def process_order(item_price, item_quantity, item_weight, discount=0):
    final_result = {
        'subtotal': calculate_order_total(item_price, item_quantity, discount),
        'shipping_cost': get_shipping_cost(item_weight)[0],
        'shipping_message': get_shipping_cost(item_weight)[1],
    }
    final_result['final_total'] = final_result['subtotal'] + final_result['shipping_cost']
    return final_result