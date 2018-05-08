from django import forms
from .models import SleepSetting

class SleepSettingsForm(forms.ModelForm):
    class Meta:
        model = SleepSetting
        fields = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'from_time', 'to_time',)

    def clean_to_time(self, *args, **kwargs):
        from_time = self.cleaned_data.get("from_time")
        to_time = self.cleaned_data.get("to_time")

        if from_time > to_time:
            raise forms.ValidationError("'From time' needs to be earlier than 'To time'")
        return to_time

