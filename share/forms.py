from django import forms 
from .models import *

class MaterialForm(forms.ModelForm): 
  
    class Meta: 
        model = Material
        fields = ['name', 'date_of_post','quantity' , 'zip_code','mob_no','location', 
       'addhar_number' , 'description', 'Material_Img'] 

        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'date_of_post':forms.DateInput(attrs={'class':'form-control'}),
        'mob_no':forms.NumberInput(attrs={'class':'form-control'}),
        'quantity':forms.NumberInput(attrs={'class':'form-control'}),
        'location':forms.TextInput(attrs={'class':'form-control'}),
        'zip_code':forms.NumberInput(attrs={'class':'form-control'}),
        'addhar_number':forms.NumberInput(attrs={'class':'form-control'}),
        'description':forms.Textarea(attrs={'class':'form-control'}),
         
        }



#Volunteer Forms===========================================
class VoltForm(forms.ModelForm): 
  
    class Meta: 
        model = Volt
        fields = ['name', 'date_of_post','location', 
        'zip_code', 'mob_no' , 'addhar_number', 'description', 'Volt_Img']
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'date_of_post':forms.DateInput(attrs={'class':'form-control'}),
        'mob_no':forms.NumberInput(attrs={'class':'form-control'}), 
        'location':forms.TextInput(attrs={'class':'form-control'}),
        'zip_code':forms.NumberInput(attrs={'class':'form-control'}),
        'addhar_number':forms.NumberInput(attrs={'class':'form-control'}),
        'description':forms.Textarea(attrs={'class':'form-control'}),
         
        }