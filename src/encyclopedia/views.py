from django.shortcuts import render, redirect, reverse
from django.http import Http404
from . import util
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import random
from django.contrib import messages

def home(request):
    return render(request, "encyclopedia/home.html", { "entries": util.list_entries() })

def detail(request, title):
    entry = util.get_entry(title)
    context= {"entry": entry, 'title':title}
    if entry:
        return render(request, "encyclopedia/detail.html", context)
    else:
        return HttpResponseNotFound("<h1>requested page was not found</h1>")


def search(request):
    results = []

    if request.method == "GET":

        query = request.GET.get('q')

        if query == '':
            query = 'None'

        entries = util.list_entries()

        for entry in entries:
            if query.lower() == entry.lower():
                results.append(entry)
                return detail(request,entry)
            elif query.lower() in entry.lower():
                results.append(entry)


    return render(request, "encyclopedia/search.html", {'query': query, 'results': results})

def rand(request):
    entries = util.list_entries()

    entry = random.choice(entries)

    return detail(request, entry)

def create(request):

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        entries = util.list_entries()
        context = {}
        for entry in entries:
            if title.lower() == entry.lower():
                messages.warning(request, "This entry already exist")
                context = {'title':title, 'content':content}
                return render(request, "encyclopedia/create.html", context)
                # to redirect to the same page
                #return HttpResponseRedirect(request.path_info)

        util.save_entry(title, content)
        messages.success(request, 'Your entry has been add successfully !')
        return redirect('encyclopedia:detail', title)

    return render(request, "encyclopedia/create.html")


def edit(request, title):
    content = util.get_entry(title)

    if request.method == "POST":
        content= request.POST.get('content')
        util.save_entry(title, content)
        messages.success(request, 'Your entry has been edited successfully !')
        return redirect('encyclopedia:detail', title)

    context= {'title':title, 'content':content}
    return render(request, "encyclopedia/edit.html", context)