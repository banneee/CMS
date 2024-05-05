from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Grade, Transaction
from django.contrib.auth import logout


@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('/')

    return render(request, 'main/profile.html', {'profile': profile})

@login_required
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        profile.save()
        return redirect('profile')

    return render(request, 'main/profile.html', {'profile': profile})

@login_required
def grades_view(request):
    grades = Grade.objects.filter(user=request.user)
    return render(request, 'main/grades.html', {'grades': grades})

@login_required
def transactions_view(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'main/transactions.html', {'transactions': transactions})
