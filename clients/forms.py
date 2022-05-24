from django.forms.widgets import CheckboxInput, DateInput, EmailInput
from .models import Client
from django.forms import ModelForm, TextInput



class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["company_name", "contract_data", "juridical_address", "post_address", "inn", "kpp", "ogrn", "bik", "payment_score", "correspondent_score", "bank_name", "email", "phone", "contact_person", "client_bool", "subclient_bool"]
        widgets = {
            "company_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите Наименование фирмы",
                'id':"input_company_name",
                'required': True,
            }),
            "contract_data": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите номер и дату договора",
                'id':"input_contract_data",
            }),
            "juridical_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите Юридический адрес",
                'id':"input_juridical_address",
                'required': True,
            }),
            "post_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите Почтовый адрес",
                'id':"input_post_address",
                'required': True,
            }),
            "inn": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите ИНН",
                'id':"input_inn",
                'required': True,
            }),
            "kpp": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите КПП",
                'id':"input_kpp",
                'required': True,
            }),
            "ogrn": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите ОГРН",
                'id':"input_ogrn",
                'required': True,
            }),
            "bik": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите БИК",
                'id':"input_bik",
                'required': True,
            }),
            "payment_score": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите Расчетный счет",
                'id':"input_payment_score",
                'required': True,
            }),
            "correspondent_score": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите Корреспондентский счет",
                'id':"input_correspondent_score",
                'required': True,
            }),
            "bank_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите Наименование банка",
                'id':"input_bank_name",
                'required': True,
            }),
            "email": EmailInput(attrs={
                'type':"text",
                'class': 'form-control',
                'placeholder':"Введите Электронную почту",
                'id':"inputMask4",
                'required': True,
                'aria-label': "Email",
                'data-inputmask': "'alias': 'email'",
                'inputmode':"email",
            }),
            "phone": TextInput(attrs={
                'type':"text",
                'class': 'form-control',
                'placeholder':"Введите Контактный телефон",
                'id':"inputMask3",
                'required': True,
                'aria-label': "Phone",
                'data-inputmask': "'alias': '+7(999)9999999'",
                'inputmode':"phone",
            }),
            "contact_person": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите Контактное лицо",
                'id':"input_contact_person",
                'required': True,
            }),
            "client_bool": CheckboxInput(attrs={
                'type':"checkbox",
                'class':"form-check-input",
                'id':"flexSwitchCheckDefault"
            }),
            "subclient_bool": CheckboxInput(attrs={
                'type':"checkbox",
                'class':"form-check-input",
                'id':"flexSwitchCheckDefault1"
            }),
        }
