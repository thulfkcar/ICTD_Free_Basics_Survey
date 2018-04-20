# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.shortcuts import render
from Survey.models import Answers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from Survey.forms import ResultsForm

def survey1(request):
    return render(request, "survey1.html", {})

# Rendering the survey page, which will have a results form displayed. See SampleSurvey/templates/home.html
# to see how the form is displayed. To change the display, edit that file. Read more about forms here:
# https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/
@csrf_protect
def basicInfo(request):
    #form = ResultsForm()
    return render(request, "basicInfo.html", {})
