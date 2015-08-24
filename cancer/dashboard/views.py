# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template.defaulttags import register

from django.contrib.auth.decorators import login_required

from .models import Patient, Cancer, Symptom, Treatment, Test, FollowUp, Questionnaire

import csv

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
def db_download(request,db_name):
	if request.POST:
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=download.csv'
		writer = csv.writer(response)
		indexes = request.POST.getlist('indexes[]')

		if db_name == 'patient':
			all_objs = Patient.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			writer.writerow([
				'姓名',
				'病历号',
				'性别',
				'出生年月',
				'身份证号',
				'地区',
				'随访电话',
				'去世日期',
				'关系',
				'电话',
				'Email',
				'微信',
				'在随访中'
			])
			for obj in objs:
				writer.writerow([
					obj.name.encode('utf-8'),
					obj.EMR_id,
					obj.sex.encode('utf-8'),
					obj.DOB,
					obj.social_id,
					obj.location.encode('utf-8'),
					obj.phone,
					obj.DOD,
					(obj.get_relative_display() or '').encode('utf-8'),
					obj.relative_phone,
					obj.relative_email,
					obj.relative_wechat,
					(obj.get_relative_in_contact_display() or '').encode('utf-8')
				])
		if db_name == 'cancer':
			all_objs =  Cancer.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			writer.writerow([
				'姓名',
				'病历号',
				'入院日期',
				'出院日期',
				'住院科室',
				'术前诊断',
				'最终诊断',
				'诊断依据',
				'肿瘤性质',
				'肿瘤分类',
				'肿瘤复发',
				'脊柱病灶数目',
				'肿瘤部位',
				'脊柱外骨累及',
				'原发灶外重要脏器累及',
				'重要脏器累及可控制',
				'备注'
			])
			for obj in objs:
				writer.writerow([
					obj.name.encode('utf-8'),
					obj.EMR_id,
					obj.admission_date,
					obj.discharge_date,
					(obj.get_department_display() or '').encode('utf-8'),
					obj.pre_diagnosis.encode('utf-8'),
					obj.diagnosis.encode('utf-8'),
					(obj.get_diagnosis_basis_display() or '').encode('utf-8'),
					(obj.get_cancer_property_display() or '').encode('utf-8'),
					(obj.get_cancer_type_display() or '').encode('utf-8'),
					(obj.get_recurrence_display() or '').encode('utf-8'),
					(obj.get_focus_display() or '').encode('utf-8'),
					(obj.get_location_display() or '').encode('utf-8'),
					(obj.get_infection_spinal_display() or '').encode('utf-8'),
					(obj.get_infection_organ_display() or '').encode('utf-8'),
					(obj.get_infection_organ_controllable_display() or '').encode('utf-8'),
					obj.comment.encode('utf-8')
				])
		if db_name == 'symptom':
			all_objs =  Symptom.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			writer.writerow([
				'姓名',
				'病历号',
				'入院日期',
				'疼痛VAS（轻中重）t为不清',
				'夜间痛',
				'疼痛需卧床缓解',
				'根性疼痛',
				'肢体麻木无力',
				'体表包块',
				'小便异常',
				'病程时间（月）',
				'最重病变水平以远肌力',
				'最重病变水平以远感觉'
			])
			for obj in objs:
				writer.writerow([
					obj.name.encode('utf-8'),
					obj.EMR_id,
					obj.admission_date,
					obj.pain_VAS,
					(obj.get_night_pain_display() or '').encode('utf-8'),
					(obj.get_stay_in_bed_display() or '').encode('utf-8'),
					(obj.get_root_pain_display() or '').encode('utf-8'),
					(obj.get_numb_display() or '').encode('utf-8'),
					(obj.get_enclosed_mass_display() or '').encode('utf-8'),
					(obj.get_abnormal_urine_display() or '').encode('utf-8'),
					obj.duration,
					(obj.get_muscle_display() or '').encode('utf-8'),
					(obj.get_feel_display() or '').encode('utf-8'),
				])
		if db_name == 'treatment':
			all_objs =  Treatment.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			writer.writerow([
				'姓名',
				'病历号',
				'手术日期',
				'术者',
				'手术入路',
				'手术部位',
				'手术方式',
				'肿瘤包膜破损情况',
				'为保证边界牺牲的组织',
				'术中骨水泥强化',
				'术中射频消融',
				'手术总时间（min）',
				'出血量（ml）',
				'异体血（ml）',
				'术中并发症',
				'术中备注',
				'术后并发症',
				'动脉栓塞（方式',
				'动脉栓塞（动脉名称）',
				'经皮骨水泥加强（节段）',
				'经皮骨水泥加强（部位）',
				'支具支持治疗（支具类型）',
				'支具支持治疗（开始年月）',
				'放疗（总剂量 Gy）',
				'放疗（疗程）',
				'放疗（开始日期）',
				'化疗（方案）',
				'化疗（开始日期）',
				'其他治疗（药物）',
				'其他治疗（开始日期）',
				'其他治疗（结束日期）',
				'其他描述'
			])
			for obj in objs:
				writer.writerow([
					obj.name.encode('utf-8'),
					obj.EMR_id,
					obj.surgery_date,
					obj.surgeon.encode('utf-8'),
					(obj.get_approach_display() or '').encode('utf-8'),
					(obj.get_location_display() or '').encode('utf-8'),
					(obj.get_method_display() or '').encode('utf-8'),
					(obj.envelope_damage or '').encode('utf-8'),
					obj.sacrifice.encode('utf-8'),
					obj.bone_cement,
					obj.radiofrequency,
					obj.total_time,
					obj.bleeding_vol,
					obj.allogeneic_blood,
					obj.surgery_complication.encode('utf-8'),
					obj.surgery_comment.encode('utf-8'),
					(obj.get_post_complication_display() or '').encode('utf-8'),
					obj.arterial_embolization_method.encode('utf-8'),
					obj.arterial_embolization_name.encode('utf-8'),
					obj.bone_cement_num.encode('utf-8'),
					(obj.get_bone_cement_location_display() or '').encode('utf-8'),
					(obj.get_support_therapy_type_display() or '').encode('utf-8'),
					obj.support_therapy_start_date.encode('utf-8'),
					obj.radiotherapy_dose.encode('utf-8'),
					obj.radiotherapy_course.encode('utf-8'),
					obj.radiotherapy_start_date.encode('utf-8'),
					obj.chemotherapy_plan.encode('utf-8'),
					obj.chemotherapy_start_date.encode('utf-8'),
					(obj.get_other_treatment_drug_display() or '').encode('utf-8'),
					obj.other_treatment_start_date.encode('utf-8'),
					obj.other_treatment_end_date.encode('utf-8'),
					obj.comment.encode('utf-8')
				])
		if db_name == 'test':
			all_objs =  Test.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			writer.writerow([
				'姓名',
				'病历号',
				'项目日期',
				'项目名称',
				'结果描述',
				'诊断结论',
				'是否术前检查',
				'WBB分期(1-12)',
				'WBB分期(A-F)',
				'CT病变性质',
				'X光顺列',
				'塌陷',
				'后外侧受累',
				'椎动脉受累',
				'Enneking分期',
				'备注'
			])
			for obj in objs:
				writer.writerow([
					obj.name.encode('utf-8'),
					obj.EMR_id,
					obj.project_date,
					obj.project_name,
					obj.result_discription.encode('utf-8'),
					obj.diagosis.encode('utf-8'),
					(obj.get_pre_test_display() or '').encode('utf-8'),
					obj.wbb_1_12.encode('utf-8'),
					obj.wbb_A_F.encode('utf-8'),
					(obj.get_CT_property_display() or '').encode('utf-8'),
					(obj.get_X_ray_display() or '').encode('utf-8'),
					(obj.get_collapse_display() or '').encode('utf-8'),
					(obj.get_lateral_involvement_display() or '').encode('utf-8'),
					obj.vertebral_artery_involvement.encode('utf-8'),
					obj.enneking.encode('utf-8'),
					obj.comment.encode('utf-8')
				])
		if db_name == 'followup':
			all_objs =  FollowUp.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			writer.writerow([
				'姓名',
				'病历号',
				'主诉',
				'复发',
				'转移',
				'内固定松动',
				'内固定断裂',
				'CT融合',
				'随访方式',
				'死亡日期',
				'随访日期',
				'备注'
			])
			for obj in objs:
				writer.writerow([
					obj.name.encode('utf-8'),
					obj.EMR_id,
					obj.major_complain.encode('utf-8'),
					(obj.get_recurrence_display() or '').encode('utf-8'),
					(obj.get_transfer_display() or '').encode('utf-8'),
					(obj.get_fixation_loose_display() or '').encode('utf-8'),
					(obj.get_fixation_break_display() or '').encode('utf-8'),
					(obj.get_CT_fusion_display() or '').encode('utf-8'),
					(obj.get_method_display() or '').encode('utf-8'),
					obj.DOD.encode('utf-8'),
					obj.followup_date.encode('utf-8'),
					obj.comment.encode('utf-8')
				])
		if db_name == 'questionnaire':
			all_objs =  Questionnaire.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			writer.writerow([
				'姓名',
				'病历号',
				'EQ5D-1',
				'EQ5D-2',
				'EQ5D-3',
				'EQ5D-4',
				'EQ5D-5',
				'问卷日期'
			])
			for obj in objs:
				writer.writerow([
					obj.name.encode('utf-8'),
					obj.EMR_id,
					obj.EQ5D_1,
					obj.EQ5D_2,
					obj.EQ5D_3,
					obj.EQ5D_4,
					obj.EQ5D_5,
					obj.date
				])
		return response
	else:
		response = HttpResponse("Not Found")
		response.status_code = 404
		return response


@login_required
def general_search(request):
	#get patient list, privacy should be considered
	patients =  Patient.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')

	#other related table fields
	fields = list()
	#for patient in patients:
		#cancer_cell = []
		#cancers = Cancer.objects.filter(DB_ID__iexact=patient.DB_ID).order_by('DB_ID')
		#for field in cancer._meta.get_all_field_names():
		#	if getattr(cancer,field.name)):
				#try:
					#str_value = str(getattr(cancer,field.name))
					#cancer_cell.append(str_value)
		#		pass
		#symptom = Symptom.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
		#treatement = Treatment.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
		#test = Test.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
		#followup = FollowUp.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
		#questionnaire = Questionnaire.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')

	args = {}
	args.update(csrf(request))
	args['user'] = request.user
	args['patients'] = patients
	#args['cancers'] = cancers
	#args['symptom'] = symptom
	#args['test'] = test
	#args['followup'] = followup
	#args['questionnaire'] = questionnaire

	return render_to_response('consoleView/general_search.html',args)

def detail(request, DB_ID):

	if DB_ID:
		patient = get_object_or_404(Patient, DB_ID=DB_ID)

		#other related table fields
		cancers = Cancer.objects.filter(DB_ID__iexact=DB_ID).order_by('DB_ID')
		symptoms = Symptom.objects.filter(DB_ID__iexact=DB_ID).order_by('DB_ID')
		treatements = Treatment.objects.filter(DB_ID__iexact=DB_ID).order_by('DB_ID')
		tests = Test.objects.filter(DB_ID__iexact=DB_ID).order_by('DB_ID')
		#followups = FollowUp.objects.filter(DB_ID__iexact=DB_ID).order_by('DB_ID')
		#questionnaires = Questionnaire.objects.filter(DB_ID__iexact=DB_ID).order_by('DB_ID')

		args = {}
		args.update(csrf(request))
		args['user'] = request.user
		args['patient'] = patient
		args['cancers'] = cancers
		args['symptoms'] = symptoms
		args['tests'] = tests
		#args['followups'] = followups
		#args['questionnaires'] = questionnaires
		
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


