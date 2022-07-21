from django.shortcuts import render
from django.http import Http404
from . import util
from django.http import HttpResponse, HttpResponseNotFound
import random
def home(request):
    return render(request, "encyclopedia/home.html", {
        "entries": util.list_entries()
    })

def detail(request, title):
    entry = util.get_entry(title)
    if entry:
        return render(request, "encyclopedia/detail.html", {
            "entry": entry
        })
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