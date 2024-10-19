from django.shortcuts import render
import markdown
from . import util
import secrets

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    file = util.get_entry(title)
    if file is None:
        return render(request, "encyclopedia/error.html")
    html = markdown.markdown(file)
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "content": html
    })

def search(request): 
    value = request.GET.get('q', '')
    file = util.get_entry(value)
    if file is not None:
        html = markdown.markdown(file)
        return render(request, "encyclopedia/title.html", {
            "title": value,
            "content": html
        })
    else:
        search_result = []
        for entry in util.list_entries():
            if value.upper() in entry.upper():
                search_result.append(entry)
        return render(request, "encyclopedia/index.html", {
            "entries": search_result,
            "search": True
        })
    
def create_new_page(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        edit = request.POST.get("edit", "")
        if (util.get_entry(title) is None or edit == "True"):
            util.save_entry(title, content)
            return render(request, f"encyclopedia/title.html", {
                "title": title,
                "content": markdown.markdown(util.get_entry(title))
            })
        else:
            return render(request, f"encyclopedia/form.html", {
                "exist": True
            })
    else:
        return render(request, "encyclopedia/form.html")
    
def edit(request, title):
    page = util.get_entry(title)
    if page is None:
        return render(request, "encyclopedia/error.html")
    else:
        content = util.get_entry(title)
        return render(request, "encyclopedia/form.html", {
            "title": title,
            "content": content,
            "edit": True
        })
    
def random(request):
    random = secrets.choice(util.list_entries())
    return render(request, "encyclopedia/title.html", {
        "title": random,
        "content": markdown.markdown(util.get_entry(random))
    })


