from django.views.generic import TemplateView, CreateView, DeleteView

from .models import Movie
from .forms import CreateMovieForm



class IndexView(CreateView):
    form_class = CreateMovieForm
    template_name = 'home/index.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        return context



class DeleteMovieView(DeleteView):
    model = Movie
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)