from django.shortcuts import render
from virus_form.forms import DeathForm
from virus_form.models import States
from virus_form.operations import data_update, total


def home(request):
    """Home file that will handle all home requests """
    obj_dict = States.objects.all()
    if request.method == 'POST':
        form = DeathForm(request.POST)
        if form.is_valid():
            state = form.cleaned_data['states']
            death_count = (form.cleaned_data.get('death_count'))
            data_update(state, death_count)

    form = DeathForm()
    context = {
        'form': form,
        'obj_dict': obj_dict
    }
    return render(request, 'virus_form/home.html', context)


def about(request):
    """ displaying all victim count"""
    obj_dict = States.objects.all()
    total_sum = total()
    return render(request, 'virus_form/about.html', {'obj_dict': obj_dict, 'total': total_sum})
# Create your views here.
