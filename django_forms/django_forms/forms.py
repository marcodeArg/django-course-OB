from django import forms

class Comment(forms.Form):
    name = forms.CharField(label="Nombre")
    url = forms.URLField(label="Tu sitio web", required=False)
    comment = forms.CharField(label="Comentario", required=False)

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre", 
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label="Email", 
        max_length=100,
        widget=forms.EmailInput(attrs={'class':'form-control'}))
    message= forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs= {'class':'form-control'}))
    
    def clean_name(self):
        name = self.cleaned_data["name"]

        if name != 'Open':
            raise forms.ValidationError('Name must be Open')
        else:
            return name