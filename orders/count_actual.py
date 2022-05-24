from .models import Order

def count_actual(request):
    count = Order.total()
    return {'count':count}

def count_in_way(request):
    count_in_way = Order.total_in_way()
    return {'count_in_way':count_in_way}