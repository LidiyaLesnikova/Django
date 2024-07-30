from django import forms

class ClientCreateForm(forms.Form):
    name = forms.CharField(max_length=100, 
                           widget=forms.TextInput(attrs={'class':'form-control',
                                                         'placeholder': 'ФИО клиента'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                            'placeholder': 'user@mail.ru'}))
    phonenumber = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class':'form-control',
                                                                               'placeholder': '+71111111111'}))
    address = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))

class ProductCreateForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control',
                                                                         'placeholder': 'Наименование товара'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
                                                               'placeholder': 'описание '}))
    price = forms.DecimalField(max_digits=8, decimal_places=2, 
                               widget=forms.NumberInput(attrs={'class':'form-control',
                                                               'placeholder': 'цена '}))
    quantity = forms.DecimalField(max_digits=8, decimal_places=2, 
                                  widget=forms.NumberInput(attrs={'class':'form-control',
                                                                  'placeholder': 'остаток '}))
    photo = forms.ImageField()