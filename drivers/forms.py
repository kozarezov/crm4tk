from django.forms.widgets import DateInput, NumberInput
from .models import Driver
from django.forms import ModelForm, TextInput, MultiWidget, MultiValueField, CharField



class MyDateInput(DateInput):
    input_type = 'date'
    format = '%d-%m-%Y'

class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = ["name", "birthday", "passport_numbers", "passport", "passport_date", "registration", "phone", "driver_license", "inn"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите ФИО",
                'id':"input_name",
                'required': True,
            }),
            "birthday": DateInput(attrs={
                'type':"text",
                'class': 'form-control',
                'placeholder':"Введите дату рождения",
                'id':"inputMask1",
                'required': True,
                'aria-label': "Date",
                'data-inputmask-inputformat':"dd.mm.yyyy",
                'data-inputmask-alias':"datetime",
            }),
            "passport_numbers": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите серию/номер паспорта",
                'id':"inputMask_passport_numbers",
                'required': True,
            }),
            "passport": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите паспортные данные",
                'id':"input_passport",
                'required': True,
            }),
            "passport_date": DateInput(attrs={
                'type':"text",
                'class': 'form-control',
                'placeholder':"Введите дату выдачи паспорта",
                'id':"inputMask2",
                'required': True,
                'aria-label': "Date",
                'data-inputmask-inputformat':"dd.mm.yyyy",
                'data-inputmask-alias':"datetime",
            }),
            "registration": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите прописку",
                'id':"input_registration",
                'required': True,
            }),
            "phone": TextInput(attrs={
                'type':"text",
                'class': 'form-control',
                'placeholder':"Введите номер телефона",
                'id':"inputMask3",
                'required': True,
                'aria-label': "Phone",
                'data-inputmask': "'alias': '+7(999)9999999'",
                'inputmode':"phone",
            }),
            "driver_license": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите номер водительского удостоверения",
                'id':"input_driver_license",
                'required': True,
            }),
            "inn": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите ИНН",
                'id':"input_inn",
                'required': True,
            }),
        }
