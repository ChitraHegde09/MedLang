from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, SymptomForm
from .models import Symptom, Phrase, UserActivity

def home(request):
    return render(request, 'core/home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('select_symptoms')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('select_symptoms')
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def select_symptoms(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            selected = form.cleaned_data['symptoms']
            request.session['symptom_ids'] = [s.id for s in selected]
            return redirect('learn')
    else:
        form = SymptomForm()
    return render(request, 'core/symptom_select.html', {'form': form})

@login_required
def learn_view(request):
    symptom_ids = request.session.get('symptom_ids', [])
    phrases = Phrase.objects.filter(symptom__id__in=symptom_ids)
    return render(request, 'core/learn.html', {'phrases': phrases})

@login_required
def dashboard(request):
    activities = UserActivity.objects.filter(user=request.user)
    return render(request, 'core/dashboard.html', {'activities': activities})
