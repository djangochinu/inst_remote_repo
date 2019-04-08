from django import forms
from multiselectfield import MultiSelectFormField

class ContactForm(forms.Form):
    name = forms.CharField(
        label='enter your name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your name'
            }
        )
    )
    email = forms.EmailField(
        label='enter your email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email'
            }
        )
    )
    mobile = forms.IntegerField(
        label='enter your mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your mobile Number'
            }
        )
    )
    COURSE_CHOICES = (
        ('python', 'python'),
        ('django', 'Django'),
        ('api', 'API'),
        ('ui', 'UI'),
        ('flask', 'FLASK')
    )
    courses = MultiSelectFormField(max_length=200, choices = COURSE_CHOICES)

    LOCATION_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Bangalore'),
        ('che', 'Chennai')
    )
    location = MultiSelectFormField(max_length=200, choices=LOCATION_CHOICES)
    SHIFT_CHOICES = (
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('night', 'Night')
    )
    shift = MultiSelectFormField(max_length=200, choices=SHIFT_CHOICES)


class FeedbackForm(forms.Form):
    name=forms.CharField(
        label='enter your name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your name'
            }
        )
    )
    rating = forms.IntegerField(
        label='enter your rating',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your rating'
            }
        )
    )
    feedback = forms.CharField(
        label='enter your feedback:',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'your feedback'
            }
        )
    )
