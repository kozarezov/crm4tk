from django.forms.widgets import DateInput, DateTimeInput, NumberInput, Select, FileInput, CheckboxInput
from .models import Ttn
from django.forms import ModelForm, TextInput

class TtnForm(ModelForm):
    class Meta:
        model = Ttn
        fields = [
            'date',
			'order_number',
			'client',
			'client_data',
			'cargoholder',
			'cargoholder_data',
			'drop_on',
			'cargorecipient',
			'cargorecipient_data',
			'drop_off',
			'subclient',
			'subclient_data',
			'driver',
			'truck',
			'model',
			'trailer',
			'cargo',
			'pallet',
			'weight',
			'subclient_contract',
			'client_contract',
		]
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
            "order_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_order_number",
            }),
            "client": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_client",
            }),
            "client_data": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_client_data",
            }),
            "cargoholder": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_cargoholder",
            }),
            "cargoholder_data": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_cargoholder_data",
            }),
            "drop_on": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_drop_on",
            }),
            "cargorecipient": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_cargorecipient",
            }),
            "cargorecipient_data": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_cargorecipient_data",
            }),
            "drop_off": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_drop_off",
            }),
            "subclient": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_subclient",
            }),
            "subclient_data": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_subclient_data",
            }),
            "driver": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_driver",
            }),
            "truck": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_truck",
            }),
            "model": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_model",
            }),
            "trailer": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_trailer",
            }),
            "cargo": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_cargo",
            }),
            "pallet": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_pallet",
            }),
            "weight": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_weight",
            }),
            "subclient_contract": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_subclient_contract",
            }),
            "client_contract": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Введите данные..",
                'id':"input_client_contract",
            }),
        }