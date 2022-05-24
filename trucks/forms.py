from django.forms.widgets import Select
from .models import Truck
from django.forms import ModelForm, TextInput



class TruckForm(ModelForm):
    class Meta:
        model = Truck
        fields = ["truck_number", "trailer_number", "type", "capacity", "vin_number", "brand", "owner"]
        widgets = {
            "truck_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите номер тягача",
                'id':"input_truck_number",
                'required': True,
            }),
            "trailer_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите номер прицепа",
                'id':"input_trailer_number",
                'required': True,
            }),
            "type": Select(attrs={
                'class': 'form-select',
                'placeholder':"Введите ТЕНТ/РЕФ/ТЕРМ",
                'id':"input_type",
                'required': True,
            }),
            "capacity": Select(attrs={
                'class': 'form-select',
                'placeholder':"Введите грузоподъёмность",
                'id':"input_capacity",
                'required': True,
            }),
            "vin_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите VIN номер (необязательно)",
                'id':"input_vin_number",
            }),
            "brand": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите Марка/Модель/Цвет (необязательно)",
                'id':"input_brand",
            }),
            "owner": Select(attrs={
                'class': 'form-control',
                'placeholder':"Введите собственника ТС (необязательно)",
                'id':"input_owner",
            }),
        }