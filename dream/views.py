from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Participant
from .forms import ParticipantForm


# Create your views here.
def index(request):
  participants= Participant.objects.all()
  return render(request, 'dream/index.html',{'participants':participants} )
    



def view_participant(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = ParticipantForm(request.POST)
    if form.is_valid():
       form.save()
       print(form)
       return redirect('add')  
  else:
       form = ParticipantForm()
  return render(request, 'dream/add.html', {'form': form})


def edit(request, id):
    participant = get_object_or_404(Participant, pk=id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ParticipantForm(instance=participant)
        
    return render(request, 'dream/edit.html', {'form': form})



def delete(request, id):
  participant = Participant.objects.get(pk=id)
  if request.method == 'POST':
    participant.delete()
    return redirect ('/')
  return render(request, 'delete.html', {'participant': participant})
