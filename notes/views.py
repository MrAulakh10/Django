from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import Http404, HttpResponse,HttpResponseRedirect
from .models import Notes
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    form_class=NotesForm
    success_url = '/smart/notes'

class NotesCreateView(CreateView):
    model = Notes
    form_class=NotesForm
    success_url = '/smart/notes'


    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(ListView,LoginRequiredMixin):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    login_url='/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    try :
        model=Notes
        context_object_name="note"
        template_name='notes/notes_detail.html'
    except Exception as e:
        print(e)
    

# def detail(request,pk):
#     try:
#         note=Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request,'notes/notes_detail.html',{'notes':note})