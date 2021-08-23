from django.shortcuts import render, redirect

from . import util

from django.http import HttpResponse
import markdown2
import secrets




#looks up entries
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
# need to look up this title
def result(request, title):
    if util.get_entry(title) == None:
        return render(request,"encyclopedia/error.html")
    else:
        html_content = markdown2.markdown(util.get_entry(title))
        return render(request,"encyclopedia/title.html", {
        "title": html_content, "query": title
        })


def search(request):
    if request.method == 'POST':
        title = request.POST['q']
        sub = [i.capitalize() for i in util.list_entries() if title in i.lower()]
        if util.get_entry(title) == None:
            return render(request, "encyclopedia/searchresult.html", {
            "entries": sub})
        else:
            return render(request,"encyclopedia/title.html", {
            "title": util.get_entry(title)})
        
def newpage(request):
    
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title) == None:
            util.save_entry(title, content)
            return render(request,"encyclopedia/title.html", {
            "content": util.get_entry(title),"title":title})
        else:
            return render(request,"encyclopedia/error.html")
    else: 
       return render(request,"encyclopedia/newpage.html")


def editpage(request):
    if request.method == "GET":
        title = request.GET["title"]
        content = util.get_entry(title)
        return render(request,"encyclopedia/editpage.html",{
            "content": content, "title":title})
    elif request.method =="POST":
        content = request.POST['editcontent']
        title = request.POST['title']
        util.save_entry(title, content)
        return redirect('title', title=title)


def random(request):
    entries = util.list_entries()
    title = secrets.choice(entries)
    return redirect('title', title=title)