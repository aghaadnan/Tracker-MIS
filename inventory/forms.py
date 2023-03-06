from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_bootstrap5.bootstrap5 import BS5Accordion
from .models import TrackerDevice, Sim


class TrackerDeviceForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'Save'))
    class Meta:
        model = TrackerDevice
        fields = ['model_number', 'vendor', 'price', 'imei']



class SimFormModel(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        FloatingField('MSISDN'),
        FloatingField('ICC_ID'),
        FloatingField('OPERATOR'),
        FloatingField('PACKAGE'),
        Submit('submit', 'Save')
    )
    class Meta:
        model = Sim
        fields = ('MSISDN', 'ICC_ID', 'OPERATOR', 'PACKAGE')
        widgets = {
            'OPERATOR': forms.Select(choices=Sim.OPERATOR_CHOICES),
        }
        labels = {
            'MSISDN': 'MSISDN',
            'ICC_ID': 'ICC_ID',
            'PACKAGE': 'PACKAGE',
            'OPERATOR': 'OPERATOR'
        }
