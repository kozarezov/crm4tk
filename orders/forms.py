from django.forms.widgets import DateInput, DateTimeInput, NumberInput, Select, FileInput, CheckboxInput
from .models import Order
from django.forms import ModelForm, TextInput



class MyDateInput(DateInput):
    input_type = 'date'
    format = '%d-%m-%Y'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["date", "status", "client", "order_number", "drop_on", "drop_off", "date_on", "date_off", "cargo", "pallet", "required_type", "required_info", "client_cost", "sale_manager", "drop_on_plus", "drop_off_plus", "date_on_plus", "date_off_plus"]
        widgets = {
            "date": DateInput(attrs={
                'type':"text",
                'class': 'form-control',
                'placeholder':"Дата рейса",
                'id':"inputMask1",
                'required': True,
                'aria-label': "Date",
                'data-inputmask-inputformat':"dd.mm.yyyy",
                'data-inputmask-alias':"datetime",
            }),
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder':"Статус заявки",
                'id':"input_status",
                'required': True,
            }),
            "client": Select(attrs={
                'class': 'form-control',
                'placeholder':"Клиент",
                'id':"input_client",
                'required': True,
            }),
            "order_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Номер заявки",
                'id':"input_order_number",
            }),
            "drop_on": Select(attrs={
                'class': 'form-control',
                'placeholder':"Точка погрузки",
                'id':"input_drop_on",
                'required': True,
            }),
            "drop_off": Select(attrs={
                'class': 'form-control',
                'placeholder':"Точка выгрузки",
                'id':"input_drop_off",
                'required': True,
            }),
            "date_on": DateTimeInput(attrs={
                'type':"text",
                'class': 'form-control flatpickr2',
                'placeholder':"Дата погрузки",
                'id':"input_date_on",
                'required': True,
            }),
            "date_off": DateTimeInput(attrs={
                'type':"text",
                'class': 'form-control flatpickr2',
                'placeholder':"Дата выгрузки",
                'id':"input_date_off",
                'required': True,
            }),
            "cargo": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Груз",
                'id':"input_cargo",
            }),
            "pallet": NumberInput(attrs={
                'class': 'form-control',
                'placeholder':"Количество паллет",
                'id':"input_pallet",
                'required': True,
            }),
            "required_type": Select(attrs={
                'class': 'form-control',
                'placeholder':"Требуемый тип транспорта",
                'id':"input_required_type",
                'required': True,
            }),
            "required_info": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Доп.требования",
                'id':"input_required_info",
            }),
            "client_cost": NumberInput(attrs={
                'class': 'form-control',
                'placeholder':"Ставка клиента",
                'id':"input_client_cost",
                'required': True,
            }),
            "sale_manager": Select(attrs={
                'class': 'form-control',
                'placeholder':"Клиентский менеджер",
                'id':"input_sale_manager",
            }),
             "drop_on_plus": Select(attrs={
                'class': 'form-control ',
                'placeholder':"Доп.Точка погрузки",
            }),
            "drop_off_plus": Select(attrs={
                'class': 'form-control',
                'placeholder':"Доп.Точка выгрузки",
                'id':"input_drop_off_plus",
                
            }),
            "date_on_plus": DateTimeInput(attrs={
                'type':"text",
                'class': 'form-control flatpickr2',
                'placeholder':"Дата погрузки на второй точке",
                'id':"input_date_on_plus",
            }),
            "date_off_plus": DateTimeInput(attrs={
                'type':"text",
                'class': 'form-control flatpickr2',
                'placeholder':"Дата выгрузки на второй точке",
                'id':"input_date_off_plus",
            }),
        }
        
class OrderUpdateForm(ModelForm):
    class Meta:
        model = Order
        fields = ["subclient", "truck", "driver", "subclient_cost", "logist", "status"]
        widgets = {
            "subclient": Select(attrs={
                'class': 'form-control',
                'placeholder':"Перевозчик",
                'id':"input_subclient",
            }),
            "truck": Select(attrs={
                'class': 'form-control',
                'placeholder':"Номер машины",
                'id':"input_truck",
            }),
            "driver": Select(attrs={
                'class': 'form-control',
                'placeholder':"Водитель",
                'id':"input_driver",
            }),
            "subclient_cost": NumberInput(attrs={
                'class': 'form-control',
                'placeholder':"Ставка перевозчика",
                'id':"input_subclient_cost",
            }),
            "logist": Select(attrs={
                'class': 'form-control',
                'placeholder':"Логист",
                'id':"input_logist",
            }),
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder':"Статус заявки",
                'id':"input_status",
                'required': True,
            }),
        }
        
class OrderDispatcherForm(OrderForm):
    class Meta:
        model = Order
        fields = ["date_on_fact", "date_off_fact", "comment", "status_dispatcher", "problem_bool", "status"]
        widgets = {
            "date_on_fact": DateTimeInput(attrs={
                'type':"text",
                'class': 'form-control flatpickr2',
                'placeholder':"Дата погрузки",
                'id':"input_date_on_fact",
            }),
            "date_off_fact": DateTimeInput(attrs={
                'type':"text",
                'class': 'form-control flatpickr2',
                'placeholder':"Дата выгрузки",
                'id':"input_date_off_fact",
            }),
            "comment": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Комментарий",
                'id':"input_comment",
            }),
            "status_dispatcher": Select(attrs={
                'class': 'form-control',
                'placeholder':"Статус заявки",
                'id':"input_status_dispatcher",
            }),
            "problem_bool": CheckboxInput(attrs={
                'type':"checkbox",
                'class':"form-check-input",
                'id':"flexSwitchCheckDefault"
            }),
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder':"Статус заявки",
                'id':"input_status",
                'required': True,
            }),
        }