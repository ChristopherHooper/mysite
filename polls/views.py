from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
import get_Events
from .models import Choice, Question, Category


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
	model = Category
	template_name = 'polls/eventsview.html'
	def get_queryset(self):
		return Question.objects.all
def events(request, first, second, third):
	p = get_object_or_404(Question, first, second, third)
	try:
		first = p.choice_set.get(pk=request.POST['first'])
		second = p.choice_set.get(pk=request.POST['second'])
		third = p.choice_set.get(pk=request.POST['second'])					
	except (KeyError):
		# Redisplay the question voting form.
		return render(request, 'polls/category.html')

	else:
		first.events = get_Events.get_events
		first.save()
		second.events = get_Events.get_events
		second.save()
		third.events = get_Events.get_events
		third.save()
	# Always return an HttpResponseRedirect after successfully dealing
	# with POST data. This prevents data from being posted twice if a
	# user hits the Back button.
	return HttpResponseRedirect(reverse('polls:eventsview', first, second, third))
        
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