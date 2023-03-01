from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from main.forms import ContactRequestForm
from main.models import ContactRequest


def page_home(request):
    context = {
        'title': 'Retro',
    }

    return render(request, 'main/index.html', context)


def page_about(request):
    context = {
        'title': 'About Us',
    }

    return render(request, 'main/about.html', context)


def page_services(request):
    context = {
        'title': 'Services',
    }

    return render(request, 'main/services.html', context)


def page_portfolio(request):
    context = {
        'title': 'Portfolio',
    }

    return render(request, 'main/portfolio.html', context)


def page_right_sidebar(request):
    context = {
        'title': 'Right Sidebar',
    }

    return render(request, 'main/sidebar-right.html', context)


def page_contact(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message was sent successfully!')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        messages.error(request, 'Something went wrong, please check form data')
    else:
        form = ContactRequestForm()

    context = {
        'title': 'Contact',
        'form': form,
    }

    return render(request, 'main/contact.html', context)
