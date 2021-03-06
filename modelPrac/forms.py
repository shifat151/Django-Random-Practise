from .models import Document
from django import forms
from django.core.exceptions import ValidationError

class DocumentForm(forms.ModelForm):




    def clean_image(self):

        IMAGE_FILE_TYPES = ['jpg', 'jpeg']

        uploaded_image = self.cleaned_data.get("image",  False)

        extension = str(uploaded_image).split('.')[-1]

        file_type = extension.lower()

        if not uploaded_image:       
            raise ValidationError("please upload an Image") # handle empty image


        if file_type not in IMAGE_FILE_TYPES:
            raise ValidationError("File is not image.")

        return uploaded_image





    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name  = cleaned_data.get('last_name')

        if first_name == last_name:
            raise ValidationError( "First name and last name cannot be the same." )

    class Meta:
        model = Document
        fields = ('first_name', 'last_name', 'image', )
