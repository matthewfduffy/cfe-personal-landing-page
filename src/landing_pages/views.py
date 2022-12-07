# from django.http import HttpResponse
from django.shortcuts import render
from .forms import LandingPageForm

# def home_page(*args, **kwargs):
#     return HttpResponse("<h1>Hello World</h1>")

def home_page(request, *args, **kwargs):
    title = "Welcome Home"
    form = LandingPageForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = LandingPageForm() # clears form after successful submission
        # print(form.cleaned_data.get("email"))

    context = {
        "title": title.format,
        "form": form
    }
    return render(request, "landing_pages/home.html", context)