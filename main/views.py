from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import event, participant
from django.contrib import messages
from django.core.mail import send_mail
from EventManager import settings
# from twilio.rest import Client
import datetime


def root(request):
    return redirect('index')


def index(request):
    return render(request, 'index.html')


def eventReg(request):
    if request.method=='POST':
        eventInstance = event(
            eventName = request.POST["e_name"],
            desc = request.POST["e_desc"],
            loc = request.POST["e_location"],
            fromDate = request.POST["e_fdate"],
            fromTime = request.POST["e_ftime"],
            toDate = request.POST["e_tdate"],
            toTime = request.POST["e_ttime"],
            regEndDate = request.POST["e_rdate"],
            regEndTime = request.POST["e_rtime"],   
            hostEmail = request.POST["e_email"],
            hostPswd = request.POST["e_pw"]
            )
        eventInstance.save()
        subject = 'Event Registration Successful'
        msg = 'Thank you for registering your event with us.'\
            + '\n\nEvent Name: ' + request.POST["e_name"]\
            + '\nEvent ID: ' + str(event.objects.get(eventName=request.POST["e_name"]).id)\
            + '\n\nYou can now review the participation in your event through our portal.'\
            + '\n\nEventManager Web App'
        to = request.POST["e_email"]
        print('--------------------------------------------------------------')
        print('Event ID: '+str(event.objects.get(eventName=request.POST["e_name"]).id))
        print('--------------------------------------------------------------')

        # send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
        contents = {
            'qwerty' : 'abc'
        }
        # index(request, contents)
        # return
        return redirect('index')
    else:
        return render(request, 'eventReg.html')




def participantReg(request):
    if request.method == 'POST':
        participantInstance = participant(
            participantName = request.POST["p_name"],
            contact = request.POST["p_contact"],
            email = request.POST["p_email"],
            regType = request.POST["p_type"],
            noOfTickets = request.POST["p_tickets"],
            eventID = request.POST["p_event"]
            )
        if (participant.objects.filter(email=request.POST["p_email"]).exists() and participant.objects.get(email=request.POST["p_email"]).eventID==int(request.POST["p_event"])):
            messages.info(request, 'You have already registered for this event.')
            return redirect('participantReg')
        else:
            participantInstance.save()
            eventInstance = event.objects.get(id=participantInstance.eventID)



            # # ------------------------- code for E-Mail notifications -------------------------

            subject = 'Event Registration Successful'
            msg = 'Thank you ' + participantInstance.participantName + ' for registering your participation with us.'\
                + '\n\nParticipant-ID: ' + str(participantInstance.id)\
                + '\nEvent Name: ' + eventInstance.eventName\
                + '\nLocation: ' + eventInstance.loc\
                + '\nDate(s): ' + str(eventInstance.fromDate) + ' - ' + str(eventInstance.toDate)\
                + '\nTime: ' + str(eventInstance.fromTime) + ' - ' + str(eventInstance.toTime)\
                + '\nParticipation Type: ' + participantInstance.regType\
                + '\nNo. of people: ' + participantInstance.noOfTickets\
                + '\n\n\nTeam EventoZone'
            to = participantInstance.email
            print('--------------------------------------------------------------')
            print('Event ID: '+str(participantInstance.id))
            print('--------------------------------------------------------------')
            # send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])



            # ------------------------- code for Mobile Message notifications -------------------------

            # account_sid = '________'
            # auth_token = '________'
            # client = Client(account_sid, auth_token)
            # client.messages.create(
            #                         from_='________',
            #                         to='+91' + request.POST["p_contact"],
            #                         body='\n\nThank you ' + request.POST["p_name"] + ' for registering your participation with us.'
            #                             + '\n\nParticipant-ID: ' + str(participantInstance.id)
            #                             + '\nEvent Name: ' + eventInstance.eventName
            #                             + '\nLocation: ' + eventInstance.loc
            #                             + '\nDate(s): ' + str(eventInstance.fromDate) + ' - ' + str(eventInstance.toDate)
            #                             + '\nTime: ' + str(eventInstance.fromTime) + ' - ' + str(eventInstance.toTime)
            #                             + '\nParticipation Type: ' + request.POST["p_type"]
            #                             + '\nNo. of people: ' + request.POST["p_tickets"]
            #                             + '\n\n\nEventManager Web App'
            #                         )
            return redirect('index')
    else:
        currDate = datetime.datetime.now().date()
        currTime = datetime.datetime.now().time()
        events = event.objects.all()
        for obj in events:
            if obj.regEndDate > currDate:
                continue
            else:
                if obj.regEndDate==currDate:
                    if obj.regEndTime > currTime:
                        continue
                    else:
                        obj.status = 0
                        toModify = event.objects.get(id=obj.id)
                        toModify.status = 0
                        toModify.save()
                else:
                    obj.status = 0
                    toModify = event.objects.get(id=obj.id)
                    toModify.status = 0
                    toModify.save()

        contents = {
            'events' : events,
            'currDate' : currDate,
            'currTime' : currTime
        }
        return render(request, 'participantReg.html', contents)
    



def eventDash(request):
    if request.method == 'POST':
        id = request.POST["event_id"]
        pw = request.POST["event_pw"]
        if event.objects.filter(id=id).exists():
            if event.objects.get(id=id).hostPswd == pw:
                participants = participant.objects.filter(eventID = id)
                contents = {
                    'participants' : participants,
                    'flag' : 1
                }
                return render(request, 'eventDash.html', contents)
            else:
                messages.info(request, 'Incorrect Password!')
                return render(request, 'eventDash.html')
        else:
            messages.info(request, 'No event is registered with this Event-ID.')
            return render(request, 'eventDash.html')
    else:
        contents = {
            'flag' : 0
        }
        return render(request, 'eventDash.html', contents)