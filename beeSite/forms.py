from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message


class BusinessForm(forms.Form):
    subject = forms.CharField(max_length=10,initial="Business")
    email = forms.EmailField(required=True,initial="mail@mail.com")
    
    #Expenses
    rent = forms.IntegerField(widget=forms.NumberInput,initial=10)
    staff_salary = forms.IntegerField(widget=forms.NumberInput,initial=10)
    staff_count = forms.IntegerField(widget=forms.NumberInput,initial=10)
    electricity = forms.IntegerField(widget=forms.NumberInput,initial=10)
    tax = forms.IntegerField(widget=forms.NumberInput,initial=10)

    #Incomes
    income = forms.IntegerField(widget=forms.NumberInput,initial=10)
    
    #Details
    #ort_choices = (('1', 'Stockholm',), ('2', 'Uppsala',))
    #ort = forms.ChoiceField(widget=forms.Select, choices=ort_choices)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message		

class BusinessResultForm(forms.Form):

    #Results
    expenses = forms.IntegerField(widget=forms.NumberInput)
    income = forms.IntegerField(widget=forms.NumberInput)
    result = forms.IntegerField(widget=forms.NumberInput)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
