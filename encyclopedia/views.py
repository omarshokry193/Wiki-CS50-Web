from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from . import util
from markdown2 import markdown
import random
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def createEntry(request):
    ef = CreateEntry(request.POST)
    title = request.POST.get('title')
    description = request.POST.get('description')
    context = {
        'ef': ef
    }
    if ef.is_valid():
        util.save_entry(title,description)
        entry = util.get_entry(title)
        return HttpResponseRedirect('wikipedia/' + title)
    else:
        return render(request, 'encyclopedia/create-entry.html', context)
def getEntry(request, entry):
    entry = util.get_entry(entry)
    try:
        entry = markdown(entry)
        return render(request, 'encyclopedia/entrys.html',{'entry':entry})
    except TypeError:
        return render(request, 'encyclopedia/entrys.html',{'entry':entry})
def randomEntry(request):
    entrys = random.choice(util.list_entries())
    return HttpResponseRedirect('/wikipedia/' + entrys)







def searchEntry(request):
    entries= util.list_entries()
    if request.method == "POST":

        results = []
        search = request.POST["search"]
        search = str(search)

        for entry in entries:

                if search == entry:
                    return HttpResponseRedirect('wikipedia/' + entry)

                if search.lower() in entry.lower():
                    results.append(entry)

        if results != []:
            return render(request, "encyclopedia/results.html", {
                'entries': results, 
                }) 
    return render(request, "encyclopedia/index.html", {
    "entries": util.list_entries(),
    })









def editEntry(request,entry):
    entry_fields = util.get_entry(entry)
    content = {
        'content':entry_fields
    }
    ef = EditEntry(content)
    # if form.is_valid():
    #     if entry in entrys:
    #         entry = util.get_entry(entry)
    #         entry = markdown(entry)
    #         return render(request, 'encyclopedia/entrys.html',{'entry':entry})
    #     else:
    #         return render(request, 'encyclopedia/search-error.html',{'entry':entry})
    # else:
    #     return render(request, 'encyclopedia/index.html',context)
    return render(request, 'encyclopedia/edit.html',{'entry':entry_fields})