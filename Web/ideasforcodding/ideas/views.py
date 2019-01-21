from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Idea

def index(request):
    return render(request, 'ideas/index.html')

def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)


class IdeaListView(ListView):
    model = Idea


class IdeaDetailView(DetailView):
    model = Idea


class IdeaRandomView(View):
    def get(self, request):
        import random
        idea = random.choice(list(Idea.objects.all()))
        return render(request, 'ideas/idea_random.html', {'idea': idea})


"""
class AddIdea(View):
    def get(self, request):
        form = AddIdeaForm()
        return render(request, 'ideas/add_idea_panel.html', {'form': form})

    def post(self, request):
        form = AddIdeaForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'ideas/add_idea_panel.html', context)
        else:
            return render(request, 'ideas/error.html', { 'error': form.errors })
"""