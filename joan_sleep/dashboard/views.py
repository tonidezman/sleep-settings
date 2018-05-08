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
        context = { 'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        self._create_sleep_setting_if_none_present()
        sleep_setting = SleepSetting.objects.first()
        form = SleepSettingsForm(request.POST or None, instance=sleep_setting)

        if form.is_valid():
            form.save()
            return redirect('dashboard-settings')
        return render(request, self.template_name, {'form': form})

    def _create_sleep_setting_if_none_present(self):
        if SleepSetting.objects.count() == 0:
            SleepSetting().save()