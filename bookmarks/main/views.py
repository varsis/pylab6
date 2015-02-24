from django.shortcuts import render,render_to_response,redirect
from django.template import RequestContext

from main.models import Link,Tag


# Create your views here.

def index(request):
    #Request the context of the request.
    #the context contains information such as the client's machine details, for exmaple.
    context = RequestContext(request)

    #get all links
    links = Link.objects.all()

    return render_to_response('main/index.html', {'links': links}, context)

def tags(request):
    context = RequestContext(request)

    #get all tags
    tags = Tag.objects.all()

    return render_to_response('main/tags.html', {'tags': tags}, context)

def tag(request,tag_name):
    context = RequestContext(request)
    the_tag = Tag.objects.get(name=tag_name)
    links = the_tag.link_set.all()
    return render_to_response('main/index.html', {'links': links,'tag_name':'#' + tag_name }, context)

def add_link(request):
    context = RequestContext(request)
    if request.method == 'POST':
        url = request.POST.get("url","")
        input_tags = request.POST.get("tags","")
        input_tags = input_tags.split(' ')
        title = request.POST.get("title","")
        Link(title=title)

        add_tags = []
        for tag in input_tags:
            try:
                found = Tag.objects.get(name=tag)
                add_tags.append(found)
            except:
                add_tags.append(Tag(name=tag))
            Link(tags=add_tags,title=title,url=url)

    return redirect(index)


