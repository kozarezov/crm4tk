from django.db.models.fields.related import ForeignKey
from django.forms.widgets import CheckboxInput, ChoiceWidget, DateInput, EmailInput, Select
from .models import Address
from django.forms import ModelForm, TextInput



class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ["name", "city", "address", "client", "phone", "contact_person", "drop_on", "drop_off"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите наименование адреса",
                'id':"inputName",
                'required': True,
            }),
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите Город",
                'id':"inputCity",
                'required': True,
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите Адрес",
                'id':"inputAddress",
                'required': True,
            }),
            "client": Select(attrs={
                'class': 'js-states form-control',
                'tabindex': '-1',
                'style':"display: none; width: 100%",
                'placeholder':"Выберите клиента",
                'id':"inputClient",
                'required': True,
            }),
            "phone": TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder':"Введите Телефон",
                'id':"inputMask3",
                'required': True,
                'aria-label': "Phone",
                'data-inputmask': "'alias': '+7(999)9999999'",
                'inputmode':"phone",
            }),
            "contact_person": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите Контактное лицо",
                'id':"inputContact1",
            }),
            "drop_on": CheckboxInput(attrs={
                'type':"checkbox",
                'class':"form-check-input",
                'id': "flexSwitchCheckDefault",
            }),
            "drop_off": CheckboxInput(attrs={
                'type':"checkbox",
                'class':"form-check-input",
                'id':"flexSwitchCheckDefault1"
            }),
        }
