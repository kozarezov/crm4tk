from orders.models import Order
from clients.models import Client
from django.db.models import Q
import datetime

class Utils:
    
    def percent_of_day_indicators(self):
        
        day_margin, day_gross, day_count_done, day_count_not_done = self.day_indicators()
        month_margin, month_gross, month_count_done, month_count_not_done = self.month_indicators()
        
        medians_margin = month_margin / datetime.date.today().day
        medians_gross = month_gross / datetime.date.today().day
        medians_count_done = month_count_done / datetime.date.today().day
        medians_count_not_done = month_count_not_done / datetime.date.today().day 
        
        percent_margin = 0
        percent_gross = 0
        percent_count_done = 0
        percent_count_not_done = 0
        
        if day_gross == 0:
            percent_margin = 0
        else:
            percent_margin = round(day_margin / day_gross * 100, 2)
            
        if day_gross == 0:
            percent_gross = -100
        else: 
            percent_gross = round((day_gross - medians_gross) / day_gross * 100)
            
        if day_count_done == 0:
            percent_count_done = -100
        else:
            percent_count_done = round((day_count_done - medians_count_done) / day_count_done * 100)
            
        if day_count_not_done == 0:
            percent_count_not_done = -100
        else:
            percent_count_not_done = round((day_count_not_done - medians_count_not_done) / day_count_not_done * 100)
            
        return percent_margin, percent_gross, percent_count_done, percent_count_not_done

    def day_indicators(self):
        
        done_orders = Order.objects.filter((Q(status='ТС назначен') | Q(status='Выполнена')) & Q(date=datetime.date.today()))
        count_not_done = Order.objects.filter((Q(status='Срыв') | Q(status='Закрыта КА')) & Q(date=datetime.date.today())).filter(Q(date__month=datetime.date.today().month)).count()
        margin = 0
        gross = 0
        count_done = 0
        
        for el in done_orders:
            margin += el.margin()
            gross += el.gross()
            count_done += 1
        
        return margin, gross, count_done, count_not_done
    
    def tomorrow_indicators(self):
        
        done_orders = Order.objects.filter((Q(status='ТС назначен') | Q(status='Выполнена')) & Q(date=datetime.date.today() - datetime.timedelta(days=1)))
        count_not_done = Order.objects.filter((Q(status='Срыв') | Q(status='Закрыта КА')) & Q(date=datetime.date.today() - datetime.timedelta(days=1))).filter(Q(date__month=datetime.date.today().month)).count()
        margin = 0
        gross = 0
        count_done = 0
        
        for el in done_orders:
            margin += el.margin()
            gross += el.gross()
            count_done += 1
        
        return margin, gross, count_done, count_not_done
    
    
    def month_indicators(self):
        done_orders = Order.objects.filter((Q(status='ТС назначен') | Q(status='Выполнена'))).filter(Q(date__month=datetime.date.today().month))
        
        count_not_done = Order.objects.filter((Q(status='Срыв') | Q(status='Закрыта КА'))).filter(Q(date__month=datetime.date.today().month)).count()
        margin = 0
        gross = 0
        count_done = 0
        
        for el in done_orders: 
            margin += el.margin()
            gross += el.gross()
            count_done += 1
                
        return margin, gross, count_done, count_not_done
    
    def day_choose(self, day=datetime.date.today()):
        done_orders = Order.objects.filter((Q(status='ТС назначен') | Q(status='Выполнена')) & Q(date=day)).count()

        return done_orders
    
    def month_choose(self, month=datetime.date.today().month):
        done_orders = Order.objects.filter((Q(status='ТС назначен') | Q(status='Выполнена'))).filter(Q(date__year=datetime.date.today().year)).filter(Q(date__month=month)).count()
        
        return done_orders
    
    def weekday_choose(self, day=datetime.date.today().weekday()):
        done_orders = Order.objects.filter((Q(status='ТС назначен') | Q(status='Выполнена'))).filter(Q(date__year=datetime.date.today().year)).filter(Q(date__month=datetime.date.today().month)).filter(Q(date__week_day=day+2)).count()
        
        return done_orders
    
    def all_orders_in_month(self):
        all_orders = []
        
        for el in range(1, datetime.date.today().day + 1):
            day = datetime.date.today() - datetime.timedelta(datetime.date.today().day - el)
            all_orders.append(self.day_choose(day))
            
        return all_orders
    
    def all_orders_in_year(self):
        all_orders = []
        
        for el in range(1, 13):
            all_orders.append(self.month_choose(el))
            
        return all_orders
    
    def all_orders_in_weekday(self):
        all_orders = []
        
        for el in range(0, 7):
            all_orders.append(self.weekday_choose(el))
            
        return all_orders
    
    def client_indicators(self):
        done_orders = Order.objects.filter((Q(status='ТС назначен') | Q(status='Выполнена'))).filter(Q(date__year=datetime.date.today().year)).filter(Q(date__month=datetime.date.today().month))
        all_clients = Client.objects.filter(client_bool=True)
        
        total_orders = []
        clients_array = []
        for el in all_clients:
            count = done_orders.filter(client=el).count()
            if (count > 0):
                total_orders.append(count)
                clients_array.append(str(el))
            
        return clients_array, total_orders