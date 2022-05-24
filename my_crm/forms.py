from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField, PasswordInput, TextInput
from .models import FileStorage, Profile, User
from django.forms import ModelForm, TextInput
from django.forms.widgets import FileInput
from django.forms.widgets import CheckboxInput

class LoginUserForm(AuthenticationForm):
     username = CharField(label="Логин", widget=TextInput(attrs={
     'class': 'form-control m-b-md', 
     'id': "signInEmail",
     'aria-describedby': "signInEmail",
     'placeholder': "Введите логин",
     }))
     password = CharField(label="Пароль", widget=PasswordInput(attrs={
     'type':"password",
     'class': 'form-control',
     'id':"signInPassword",
     'aria-describedby':"signInPassword",
     'placeholder':"Введите пароль",
     }))
     
class FileStorageForm(ModelForm):
    class Meta:
        model = FileStorage
        fields = ["file_name", "document"]
        widgets = {
            "file_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Наименование файла",
                'id': 'customFileLangHTML',
            }),
            "document": FileInput(attrs={
                'type':"file",
                'class': 'form-control',
                'id': 'customFileLangHTML',
            }),
        }
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            "first_name": TextInput(attrs={
                'type':"text",
                'class':"form-control",
                'id':"settingsInputFirstName",
                'placeholder':"Введите имя"
            }),
            "last_name": TextInput(attrs={
                'type':"text",
                'class':"form-control",
                'id':"settingsInputLastName",
                'placeholder':"Введите фамилию"
            }),
            "email": TextInput(attrs={
                'type':"email",
                'class':"form-control",
                'id':"settingsInputEmail",
                'aria-describedby': "settingsEmailHelp",
                'placeholder':"Введите почту"
            }),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['theme',]
        widgets = {
            "theme": CheckboxInput(attrs={
                'type':"checkbox",
                'class':"form-check-input",
                'id':"flexSwitchCheckDefault"
            }),
        }