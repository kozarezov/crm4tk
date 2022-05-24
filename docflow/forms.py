from django.forms.widgets import DateInput, DateTimeInput, NumberInput, Select, FileInput, CheckboxInput
from .models import DocFlow
from django.forms import ModelForm, TextInput

class DocFlowForm(ModelForm):
    class Meta:
        model = DocFlow
        fields = ["date", "status", "account_number", "manager_do", "comment"]
        widgets = {
            "date": DateInput(attrs={
                'type':"text",
                'class': 'form-control',
                'placeholder':"Дата получения документов",
                'id':"inputMask1",
                'required': True,
                'aria-label': "Date",
                'data-inputmask-inputformat':"dd.mm.yyyy",
                'data-inputmask-alias':"datetime",
            }),
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder':"Статус документооборота",
                'id':"input_status",
                'required': True,
            }),
            "manager_do": Select(attrs={
                'class': 'form-control',
                'placeholder':"Ответственный специалист",
                'id':"input_manager_do",
                'required': True,
            }),
            "account_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Номер счета",
                'id':"input_account_number",
            }),
            "comment": TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder':"Комментарий",
                'id':"input_comment",
            }),
        }
        
class OrderDetailForm(DocFlowForm):
    class Meta:
        model = DocFlow
        fields = ["subclient_document", "ttn_document"]
        widgets = {
            "subclient_document": FileInput(attrs={
                'type':"file",
                'class': 'form-control',
                'id': 'customFileLangHTML',
            }),
            "ttn_document": FileInput(attrs={
                'type':"file",
                'class': 'form-control',
                'id': 'customFileLangHTML1',
            }),
        }