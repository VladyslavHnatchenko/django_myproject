import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView

from .models import DreamReal
from .forms import LoginForm


def login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()

    return render(request, "logged_in.html", {"username": username})


class DreamView(ListView):
    queryset = DreamReal.objects.all()
    template_name = "dreamreal.html"


class StaticView(TemplateView):
    template_name = "static.html"


def send_mass_email(request):
    send_mail("Test_New_Message",
              "WOW MAN. This is automated message.",
              "***",  # insert your email
              ["poje@dr-mail.net",  # https://temp-mail.org/en/  # generate fake email
               "***"],  # insert another email
              fail_silently=False)
    return render(request, "email.html")


def send_email(request):
    send_mail("What's up, man!",
              "Hello there. This is automated message.",
              "***",  # insert your email
              ["poje@dr-mail.net"],  # https://temp-mail.org/en/  # generate fake email
              fail_silently=False)
    return render(request, "email.html")


def data_manipulation(request):
    res = ""

    # Filtering data:
    qs = DreamReal.objects.filter(name="paul")
    res += f"Found : {len(qs)} results <br>"

    # Ordering results
    qs = DreamReal.objects.order_by("name")

    for elt in qs:
        res += elt.name + "<br>"

    return HttpResponse(res)


def crud_ops(request):
    # Creating an entry.
    dreamreal = DreamReal(
        website="www.polo.com",
        mail="sorex@polo.com",
        name="sorex",
        phone_number="002376970"
    )
    dreamreal.save()

    # Read ALL entries.
    objects = DreamReal.objects.all()
    res = "Printing all DreamReal entries in the DB: <br>"

    for elt in objects:
        res += elt.name + "<br>"

    # Read a specific entry:
    sorex = DreamReal.objects.get(name="sorex")
    res += "Printing one entry <br>"
    res += sorex.name

    # Delete an entry.
    res += "<br>Deleting an entry<br>"
    sorex.delete()

    # Update data.
    dreamreal = DreamReal(
        website="www.polo.com",
        mail="sorex@polo.com",
        name="sorex",
        phone_number="002376970"
    )

    dreamreal.save()
    res += "Updating entry<br>"

    dreamreal = DreamReal.objects.get(name="sorex")
    dreamreal.name = "thierry"
    dreamreal.save()

    return HttpResponse(res)


def morning(request):
    return render(request, "morning.html", {})


def hello(request):
    today = datetime.datetime.now().date()

    days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return redirect("https://www.djangoproject.com")


def view_article(request, id):
    text = f"Displaying article number: {id}"
    return redirect(view_articles, month="02", year="2045")


def view_articles(request, month, year):
    text = f"Displaying articles of: {month}/{year}"
    return HttpResponse(text)
