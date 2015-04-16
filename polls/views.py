from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from .models import Choice, Question, Category, Events, Eve
import pprint
from django.core import serializers
import json
import prettyQuery

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
		"""
		Return the last five published questions (not including those set to be
		published in the future).
		"""
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
		
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class CatagoryView(generic.ListView):
	model = Category
	template_name = 'polls/CategoryList.html'
	context_object_name = "category_list"
	
class EventsView(generic.ListView):
	model = Events
	template_name = 'polls/eventsview.html'
	context_object_name = 'events_list'
# 	def get_queryset(self):
# 		return Question.objects.all

class Error(generic.ListView):
	model = Category
	template_name = 'polls/error.html'
	
def events(request):
# 	p = get_object_or_404(Category)
	a = get_object_or_404(Category, CId=request.POST['first'])
	b = get_object_or_404(Category, CId=request.POST['second'])
	c = get_object_or_404(Category, CId=request.POST['third'])
	try:			
		Events.objects.all().delete()
		a = Events(first = prettyQuery.prettyQuery(request.POST['first']), second = prettyQuery.prettyQuery(request.POST['second']), third = prettyQuery.prettyQuery(request.POST['third']))
		a.save()
	except (KeyError):
		# Redisplay the question voting form.
		return render(request, 'polls/error.html')
		#return HttpResponseRedirect(reverse('polls:results', args=(first,)))
#	else:
	# Always return an HttpResponseRedirect after successfully dealing
	# with POST data. This prevents data from being posted twice if a
	# user hits the Back button.
# 	return HttpResponseRedirect(reverse('polls:eventsview', args=(first,)))
	return HttpResponseRedirect(reverse('polls:eventsview', args=()))
        
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))