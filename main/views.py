from django.shortcuts import render, redirect
from .models import Stories, StoriesSeries, StoriesCategory, Dataa, telling
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.http import HttpResponse


def single_slug(request, single_slug):
    categories = [c.category_slug for c in StoriesCategory.objects.all()]
    if single_slug in categories:
        matching_series = StoriesSeries.objects.filter(story_category__category_slug=single_slug)
        series_urls = {}
        for m in matching_series.all():
            part_one = Stories.objects.filter(story_series__story_series=m.story_series).earliest("story_published")
            series_urls[m] = part_one.story_slug

        return render(request=request,
                      template_name='main/category.html',
                      context={"story_series": matching_series, "part_ones": series_urls})

    stories = [t.story_slug for t in Stories.objects.all()]
    if single_slug in stories:
        this_story = Stories.objects.get(story_slug=single_slug)
        story_from_series = Stories.objects.filter(story_series__story_series=this_story.story_series).order_by('story_published')
        this_tutorial_idx = list(story_from_series).index(this_story)

        return render(request,
                      "main/story.html",
                      {"story": this_story,
                       "sidebar": story_from_series,
                       "this_story_idx": this_tutorial_idx})

    return HttpResponse(f"{single_slug} is a category")


def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"stories": Stories.objects.all}
                  )


def see_more(request):
    return render(request=request,
                  template_name="main/see_more.html",
                  context={"stories": telling.objects.all}
                  )


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now Logged in as { username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request,
                  "main/register.html",
                  context={"form": form})


def data(request):
    return render(request=request,
                  template_name="main/analy.html",
                  context={"data": Dataa.objects.all()})



def logout_request(request):
    logout(request)
    messages.info(request, "You have logged out")
    return redirect("main:homepage")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now Logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Check username and password!")
        else:
            messages.error(request, "Check username and password!")

    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form": form})
