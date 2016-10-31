from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    title = "MarkupEasy"
    template = loader.get_template('editor/index.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))
