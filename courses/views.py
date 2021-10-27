from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from courses.models import Course

# Create your views here.
class CoursesView(ListView):
    model = Course
    template_name = 'courses/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context
  
  
class CreateCourseView(CreateView):
  model = Course
  fields = ['name','semester']






