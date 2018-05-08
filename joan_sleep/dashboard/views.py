from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import SleepSettingsForm

from .models import SleepSetting

class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def get(self, request):
        self._create_sleep_setting_if_none_present()
        sleep_setting = SleepSetting.objects.filter().values()[0]
        form = SleepSettingsForm(initial=sleep_setting)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        self._create_sleep_setting_if_none_present()
        sleep_setting = SleepSetting.objects.first()
        form = SleepSettingsForm(request.POST or None, instance=sleep_setting)

        if form.is_valid():
            if self._at_least_one_day_chosen(form.cleaned_data):
                form.save()
            return redirect('dashboard-settings')
        return render(request, self.template_name, {'form': form})

    def _create_sleep_setting_if_none_present(self):
        if SleepSetting.objects.count() == 0:
            SleepSetting().save()

    def _at_least_one_day_chosen(self, form_data):
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        for day in days:
            if form_data.get(day):
                return True
        return False
