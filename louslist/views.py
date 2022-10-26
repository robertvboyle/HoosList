from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

import urllib, json


class IndexView(generic.ListView):
    template_name = 'louslist/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        url = "http://luthers-list.herokuapp.com/api/deptlist/?format=json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        collegeArts = set(["AAS","AMST","CREO", "NESC","COGS","ANTH","ARAB","ARAD","ARCY","ARTH","ARTR","ARTS","ASL","ASTR","BIOL","CASS","CHEM","CHIN","TURK","CHTR","CLAS","COLA","CPLT","DANC","DRAM","EALC","EAST","ECON","EGMT","ENCW","ENGL","ENWR","ETP","EVSC","FORU","FREN","FRTR","GDS","GERM","GETR","GREE","GSGS","GSSJ","GSVS","HEBR","HIAF","HIEA","HIEU","HILA","HIND","HISA","HIST","HIUS","HSCI","INST","ITAL","ITTR","JAPN","JPTR","JWST","KOR","LASE","LATI","LING","LNGS","MATH","MDST","MESA","MEST","MUSI","PERS","PETR","PHIL","PHYS","PHS","PLAP","PLCP","PLIR","PLPT","POL","PORT","POTR","PPL","PSYC","RELA","RELB","RELC","RELG","RELH","RELI","RELJ","RELS","RUSS","RUTR","SANS","SAST","SATR","SLAV","SLFK","SLTR","SOC","SPAN","SPTR","STAT","TBTN","URDU","USEM","WGS","YIDD"])
        engineering = set(["CS","APMA","CE","BME","CHE","CPE","ECE","MSE","MAE","STS","SYS"])
        education = set(["EDHS","EDLF","EDIS","KINE","KLPA"])
        architecture = set(["ALAR","ARAH","ARCH","ARH","LAR","PLAC","PLAN","SARC"])
        nursing = set(["GCNL","GNUR","NUCO","NUIP","NURS"])
        commmerce = set(["COMM","GCOM", "ACCT"])
        batten = set(["LPPA","LPPL","LPPP","LPPS"])

        caas =[]
        seas=[]
        edu =[]
        arch =[]
        nurs =[]
        comm =[]
        batt =[]
        rest = []

        for i in data:
            if i['subject'] in collegeArts:
                caas.append(i['subject'])
            elif i['subject'] in engineering:
                seas.append(i['subject'])
            elif i['subject'] in education:
                edu.append(i['subject'])
            elif i['subject'] in architecture:
                arch.append(i['subject'])
            elif i['subject'] in nursing:
                nurs.append(i['subject'])
            elif i['subject'] in commmerce:
                comm.append(i['subject'])
            elif i['subject'] in batten:
                batt.append(i['subject'])
            else:
                rest.append(i['subject'])
                
        context= {
            'data' : data,
        }

        return context

    def get_queryset(self):
        return ''


class DepartmentView(generic.ListView):
    template_name = 'louslist/department.html'

    def get_context_data(self, **kwargs):
        dept = self.kwargs.get('department')
        context = super(DepartmentView, self).get_context_data(**kwargs)
        url = "http://luthers-list.herokuapp.com/api/dept/%s/?format=json" % (dept)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        context= {
            'data' : data,
        }

        return context

    def get_queryset(self):
        return ''



    

class LoginView(generic.ListView):
    template_name = 'louslist/login.html'

    def get_queryset(self):
        return ''

