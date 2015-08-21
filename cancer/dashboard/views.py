# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template.defaulttags import register

from django.contrib.auth.decorators import login_required

from .models import Patient, Cancer, Symptom, Treatment, Test, FollowUp, Questionnaire

@login_required
def index(request):
	objs = Treatment.objects.filter(surgeon__iexact=u'刘忠军')#request.user.username).order_by('DB_ID')
	args = {}
	args.update(csrf(request))
	args['user'] = request.user
	args['objs'] = objs
	return render_to_response('consoleView/account.html',args)

@login_required
def db_search(request,db_name):
	db_name_ch = {
	'patient':"病人基本信息",
	'cancer':"肿瘤基本信息",
	'symptom':"症状与体征",
	'treatment':"治疗情况",
	'test':"辅助检查",
	'followup':"随访情况",
	'questionnaire' : "问卷评分"
	}
	if db_name == 'patient':
		objs =  Patient.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	if db_name == 'cancer':
		objs =  Cancer.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	if db_name == 'symptom':
		objs =  Symptom.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	if db_name == 'treatment':
		objs =  Treatment.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	if db_name == 'test':
		objs =  Test.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	if db_name == 'followup':
		objs =  FollowUp.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	if db_name == 'questionnaire':
		objs =  Questionnaire.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')

	args = {}
	args.update(csrf(request))
	args['user'] = request.user
	args['db_name'] = db_name
	args['db_name_ch'] = db_name_ch[db_name]
	args['objs'] = objs

	return render_to_response('consoleView/db_search.html',args)

@login_required
def general_search(request):
	#get patient list, privacy should be considered
	patients =  Patient.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')

	#other related table fields
	#cancer = Cancer.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
	#symptom = Symptom.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
	#treatement = Treatment.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
	#test = Test.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
	#followup = FollowUp.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
	#questionnaire = Questionnaire.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')

	args = {}
	args.update(csrf(request))
	args['user'] = request.user
	args['patients'] = patients
	#args['cancer'] = cancer
	#args['symptom'] = symptom
	#args['test'] = test
	#args['followup'] = followup
	#args['questionnaire'] = questionnaire

	return render_to_response('consoleView/general_search.html',args)

def detail(request, DB_ID):

	if DB_ID:
		patient = get_object_or_404(Patient, DB_ID=DB_ID)

		args = {}
		args.update(csrf(request))
		args['user'] = request.user
		args['patient'] = patient
		
		return render(request, 'detailView/detail.html', args)
	else:
		HttpResponseRedirect('/dashboard/')


######################registered template filters##########################
@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)

@register.filter
def key(d, key_name):
	try:
		value = d[key_name]
	except:
		from django.conf import settings

		value = settings.TEMPLATE_STRING_IF_INVALID

	return value


