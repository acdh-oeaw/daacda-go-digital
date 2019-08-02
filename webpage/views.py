from copy import deepcopy

import requests
import json

from django.conf import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext, loader
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

from entities.models import Airstrike, Bomber
from entities.utils import crash_places, attack_places
from . forms import form_user_login
from . metadata import PROJECT_METADATA as PM


def get_imprint_url():
    try:
        base_url = settings.ACDH_IMPRINT_URL
    except AttributeError:
        base_url = "https://provide-an-acdh-imprint-url/"
    try:
        redmine_id = settings.REDMINE_ID
    except AttributeError:
        redmine_id = "go-register-a-redmine-service-issue"
    return "{}{}".format(base_url, redmine_id)


class ImprintView(TemplateView):
    template_name = 'webpage/imprint.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        imprint_url = get_imprint_url()
        r = requests.get(get_imprint_url())

        if r.status_code == 200:
            context['imprint_body'] = "{}".format(r.text)
        else:
            context['imprint_body'] = """
            On of our services is currently not available. Please try it later or write an email to
            acdh@oeaw.ac.at; if you are service provide, make sure that you provided ACDH_IMPRINT_URL and REDMINE_ID
            """
        return context


class GenericWebpageView(TemplateView):
    template_name = 'webpage/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super(GenericWebpageView, self).get_context_data(**kwargs)
    #     context['apps'] = settings.INSTALLED_APPS
    #     print(self.get_template_names()[0])
    #     if self.get_template_names()[0] == "webpage/index.html":
    #         gj_dicts = [
    #             x.get_list_geojson() for x in Airstrike.objects.all().
    #             filter(target__lat__isnull=False)
    #         ]
    #         feature_collection = {
    #             'type': 'FeatureCollection',
    #             'features': gj_dicts
    #         }
    #         context['geojson_airstrike'] = json.dumps(feature_collection)
    #         gj_dicts = [
    #             x.get_list_geojson() for x in Bomber.objects.filter(crash_place__lat__isnull=False)
    #         ]
    #         feature_collection = {
    #             'type': 'FeatureCollection',
    #             'features': gj_dicts
    #         }
    #         context['geojson_crash'] = json.dumps(feature_collection)
    #     return context

    def get_template_names(self):
        template_name = "webpage/{}.html".format(self.kwargs.get("template", 'index'))
        try:
            loader.select_template([template_name])
            template_name = "webpage/{}.html".format(self.kwargs.get("template", 'index'))
        except:
            template_name = "webpage/index.html"
        return [template_name]


#################################################################
#               views for login/logout                          #
#################################################################

def user_login(request):
    if request.method == 'POST':
        form = form_user_login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
            return HttpResponse('user does not exist')
    else:
        form = form_user_login()
        return render(request, 'webpage/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render_to_response('webpage/user_logout.html')


def handler404(request, exception):
    return render(request, 'webpage/404-error.html', locals())


def project_info(request):

    """
    returns a dict providing metadata about the current project
    """

    info_dict = deepcopy(PM)

    if request.user.is_authenticated:
        pass
    else:
        del info_dict['matomo_id']
        del info_dict['matomo_url']
    info_dict['base_tech'] = 'django'
    info_dict['framework'] = 'djangobaseproject'
    return JsonResponse(info_dict)
