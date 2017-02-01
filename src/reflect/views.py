from django.shortcuts import render,get_object_or_404
from reflect.forms import ReflectionForm, ReplyForm
from django.shortcuts import redirect
from .models import Reflection, Reply
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.core.urlresolvers import reverse


def home(request):
	title = "交大線上意見回饋表單"
	success = True
	if request.POST:
		success = True
		email = request.POST['email']
		name = request.POST['name']
		category = request.POST['category']
		suggestion = request.POST['suggestion']
		content = request.POST['content']
		Reflection.objects.create(
			category=category,
			name = name,
			email = email,
			content = content,
			advice=suggestion,
			state=0,
			)
		return redirect('/success/')
	return render(request, "home.html",locals())

def success(request):
	return render(request,"success.html")

class ReflectionDetailView(DetailView):
	queryset = Reflection.objects.all()
	model = Reflection
	template_name = "detail.html"

	def get_context_data(self, **kwargs):
		form = ReplyForm
		reflection = Reflection.objects.get(id=self.kwargs.get('pk'))
		context = {
				"timestamp" : getattr(reflection, 'timestamp'),
				"name" : getattr(reflection, 'name'),
				"email" : getattr(reflection, 'email'),
				"category" : getattr(reflection, 'category'),
				"advice" : getattr(reflection, 'advice'),
				"content" : getattr(reflection, 'content'),
				"state" : getattr(reflection, 'state'),
				"form" : form,
				"replies" : Reply.objects.filter(reflection=Reflection.objects.get(id=self.kwargs.get('pk'))),
		}
		return context

	def post(self, request, *args, **kwargs):
		return self.get(request, *args, **kwargs)

	def dispatch(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			reflection = Reflection.objects.get(id=self.kwargs.get('pk'))

			#First Visted Handling
			if getattr(reflection, 'state') == 0:
				Reply.objects.create(
						user="系統自動產生",
						content = "已收到意見",
						reflection = reflection,
					)
				setattr(reflection, 'state', '1')	#state=1 read
				reflection.save()
      		
			#Form is submitted
			form = ReplyForm(self.request.POST or None)	
			if request.POST:
				if form.is_valid():
					success = True
					user = request.POST['user']
					content = request.POST['content']
					reflection = Reflection.objects.get(id=self.kwargs.get('pk'))
					Reply.objects.create(
						user=user,
						content = content,
						reflection = reflection,
					)
					
				return super(ReflectionDetailView, self).dispatch(request, *args, **kwargs)
		else:
			return redirect('auth_login')
		return super(ReflectionDetailView, self).dispatch(request, *args, **kwargs)


	# def render_to_response(self, context):
	# 	if self.request.user.is_authenticated:
	# 		form = ReplyForm
			

class ReflectionListView(ListView):
	queryset = Reflection.objects.all()
	template_name = "stunion.html"

	def get_context(self):
		queryset = Reflection.objects.all()
		context={
				"queryset" : queryset,
			}

	def render_to_response(self, context):
		if self.request.user.is_authenticated:
			return super(ReflectionListView, self).render_to_response(context)
		else:
			return redirect('auth_login')
    

class ReflectDeleteView(DeleteView):
    model = Reflection
    template_name = "delete_confirm.html"
    success_url = reverse_lazy('list')

    def render_to_response(self, context):
    	if self.request.user.is_authenticated:
    		return super(ReflectDeleteView, self).render_to_response(context)
    	else:
    		return redirect('auth_login')