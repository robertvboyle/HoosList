
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db.models import Q

import urllib, json

from .models import Course, Schedule, User, Profile, Relationship


class IndexView(generic.ListView):
    template_name = 'louslist/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        url = "http://luthers-list.herokuapp.com/api/deptlist/?format=json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        collegeArts = set(["AAS","MSP","AMST","KICH","CREO", "ELA","HIME","NESC","COGS","ANTH","ARAB","ARAD","ARCY","ARTH","ARTR","ARTS","ASL","ASTR","BIOL","CASS","CHEM","CHIN","TURK","CHTR","CLAS","COLA","CPLT","DANC","DRAM","EALC","EAST","ECON","EGMT","ENCW","ENGL","ENWR","ETP","EVSC","FORU","FREN","FRTR","GDS","GERM","GETR","GREE","GSGS","GSSJ","GSVS","HEBR","HIAF","HIEA","HIEU","HILA","HIND","HISA","HIST","HIUS","HSCI","INST","ITAL","ITTR","JAPN","JPTR","JWST","KOR","LASE","LATI","LING","LNGS","MATH","MDST","MESA","MEST","MUSI","PERS","PETR","PHIL","PHYS","PHS","PLAP","PLCP","PLIR","PLPT","POL","PORT","POTR","PPL","PSYC","RELA","RELB","RELC","RELG","RELH","RELI","RELJ","RELS","RUSS","RUTR","SANS","SAST","SATR","SLAV","SLFK","SLTR","SOC","SPAN","SPTR","STAT","TBTN","URDU","USEM","WGS","YIDD"])
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
            'seas' : seas,
            'caas' : caas,
            'edu' :edu,
            'arch': arch,
            'nurs':nurs,
            'comm':comm,
            'batt':batt,
            'rest' : rest,
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


def my_profile(request):
    profile = Profile.objects.get(user=request.user)

    context = {'profile':profile}

    return render(request, 'louslist/myprofile.html', context)

def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)

    qs = Relationship.objects.invitations_received(profile)
    results = list(map(lambda x: x.sender, qs))
    is_empty = False
    if len(results) == 0:
        is_empty=True

    context = {'qs':results, 'is_empty' : is_empty}

    return render(request, 'louslist/my_invites.html', context)
    
def accept_invitation(request):
    if request.method=="POST":
        pk = request.POST.get('profile_pk')
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)

        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        if rel.status == 'send':
            rel.status = 'accepted'
            rel.save()

    return redirect("/my-invites/")

        

        

def reject_invitation(request):
    if request.method=="POST":
        pk = request.POST.get('profile_pk')
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)

        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        rel.delete()
    
    return redirect("/my-invites/")


def invite_profiles_list_view(request):

    user = request.user 

    qs = Profile.objects.get_all_profiles_to_invite(user)

    context = {'qs':qs}

    return render(request, 'louslist/to_invite_list.html', context)

class LoginView(generic.ListView):
    template_name = 'louslist/login.html'

    def get_queryset(self):
        return ''

class ProfileView(generic.ListView):
    template_name = 'louslist/profile.html'

    def get_queryset(self):
        return ''

def ScheduleView(request):
    if(request.method == "POST"):
        userid = request.POST.get('userid')
        courseid = request.POST.get('courseid')
        course = Course.objects.get(course_id=courseid)
        s = Schedule.objects.get(userID=userid)
        s.courses.remove(course)
        s.save()
    try:
        courses = Schedule.objects.get(userID=request.user.id).courses.all()
    except:
        s = Schedule(userID=request.user.id)
        s.save()
        courses = s.courses.all()
    context = {'courses': courses}
    return render(request, 'louslist/schedule.html', context)

def processClass(request):
    if(request.method == "POST"):

        #user = User.objects.get(id=userid)

        # When we make the user model, we will query the user by the context user id, then add the class to the user's list of classes
        userid = request.POST.get('userid')
        form = Course()
        form.title = request.POST.get("title") 
        department = request.POST.get("department")
        form.subject = request.POST.get("subject")
        form.number = request.POST.get("number")
        form.section = request.POST.get("section")
        if "-" in str(request.POST.get("credits")):
            form.credits = int(str(request.POST.get("credits"))[0])
        else:
            form.credits = request.POST.get("credits")
        form.instructor = request.POST.get("instructor") 
        form.days = request.POST.get("days")
        form.time = request.POST.get("time")
        form.location = request.POST.get("location") 
        form.course_id = request.POST.get("courseid")

        try:
            form = Course.objects.get(course_id=form.course_id)
        except:
            form.save()
        
        # arrayTimes = []
        # if form.time != "-" or form.time != "":
        #     timeSplit = form.time.split("  ")
        #     for i in timeSplit:
        #         if i !="":
        #             timesSecond = i.split(" - ")
        #             firstTime = datetime.datetime.strptime(timesSecond[0], "%I:%M %p")
        #             secondTime = datetime.datetime.strptime(timesSecond[1], "%I:%M %p")
        #             arrayTimes.append([firstTime,secondTime])

        # times = []
        # if form.days != "-" or form.days != "":
        #     daysSplit = form.days.split(" ")
        #     for day in range(len(daysSplit)):
        #         for oneDay in range(0,len(daysSplit[day]),2):
        #             curDay = daysSplit[day][oneDay:oneDay+2]
                    
        #             if curDay == "Mo":
        #                 times.append([arrayTimes[day][0].replace(day=2),arrayTimes[day][1].replace(day=2)])
        #             elif curDay == "Tu":
        #                 times.append([arrayTimes[day][0].replace(day=3),arrayTimes[day][1].replace(day=3)])
        #             elif curDay == "We":
        #                 times.append([arrayTimes[day][0].replace(day=4),arrayTimes[day][1].replace(day=4)])
        #             elif curDay == "Th":
        #                 times.append([arrayTimes[day][0].replace(day=5),arrayTimes[day][1].replace(day=5)])
        #             elif curDay == "Fr":
        #                 times.append([arrayTimes[day][0].replace(day=6),arrayTimes[day][1].replace(day=6)])
        #             elif curDay == "Sa":
        #                 times.append([arrayTimes[day][0].replace(day=7),arrayTimes[day][1].replace(day=7)])
        #             else:
        #                 times.append([arrayTimes[day][0].replace(day=1),arrayTimes[day][1].replace(day=1)])   
                        
      
        try:
            schedule = Schedule.objects.get(userID= userid) # If the course already exists, we don't want to add it again
            schedule.save()
            schedule.courses.add(form)    
        except:
            schedule = Schedule(userID= userid)
            schedule.save()
            schedule.courses.add(form)
            # If the course doesn't exist, save it to the database
        
    return HttpResponseRedirect(reverse('louslist:department', kwargs={'department': department}))

def logout_user(request):
    logout(request)
    return redirect("/")


def profiles_list_view(request):

    user = request.user 

    qs = Profile.objects.get_all_profiles(user)

    context = {'qs':qs}

    return render(request, 'louslist/profile_list.html', context)


class ProfileListView(generic.ListView):
    model = Profile
    template_name = 'louslist/profile_list.html'
    context_object_name = 'qs'

    def get_queryset(self):
         qs = Profile.objects.get_all_profiles(self.request.user)
         return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        user = self.request.user
        profile = Profile.objects.get(user=user)
        #context['profile'] = profile

        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)

        rel_receiver = []
        rel_sender = []

        for item in rel_r:
            rel_receiver.append(item.receiver.user)

        for item in rel_s:
            rel_sender.append(item.sender.user)

        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        context['is_empty'] = False
        if len(self.get_queryset()) == 0:
              context['is_empty'] = True
        
        return context

def send_invitation(request):
    if request.method=='POST':
        pk=request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.create(sender=sender,receiver=receiver,status='send')

        return redirect(request.META.get('HTTP_REFERER'))

    return redirect("/")

def remove_from_friends(request):
    if request.method=='POST':
        pk=request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.get(
            (Q(sender=sender) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=sender))
        )
        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))

    return redirect("/")

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

def profilesView(request, userid):
    user = request.user
    user2 = User.objects.get(id=userid)

    if user == user2:
        return redirect('louslist:profile')
    else:
        
        context = {'user2': user2}
        return render(request, 'louslist/profiles.html', context)


def schedulesView(request, userid):
    if(request.method == "POST"):
        user2id = request.POST.get('userid')
        courseid = request.POST.get('courseid')
        course = Course.objects.get(course_id=courseid)
        s = Schedule.objects.get(userID=user2id)
        s.courses.add(course)
        s.save()

    areFriends = False
    user = request.user
    user2 = User.objects.get(id=userid)

    if user2 in user.profile.friends.all():
        areFriends = True
    
    if user == user2:
        return redirect('louslist:schedule')
    try:
        courses = Schedule.objects.get(userID=userid).courses.all()
    except:
        s = Schedule(userID=userid)
        s.save()
        courses = s.courses.all()
    context = {'courses': courses, 'user2': user2, 'friends': areFriends}
    return render(request, 'louslist/friendschedules.html', context)

    

