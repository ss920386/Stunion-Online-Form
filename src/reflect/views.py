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
			advice=suggestion
			)
		return redirect('/success/')
	return render(request, "home.html",locals())

def success(request):
	return render(request,"success.html")
	
# def stunion(request):
# 	if request.user.is_authenticated:
# 		queryset = Reflection.objects.all()
# 		context={
# 			"queryset" : queryset,
# 		}
# 		return render(request, "stunion.html",context)
# 	else:
# 		return redirect('auth_login')

class ReflectionDetailView(DetailView):
	queryset = Reflection.objects.all()
	model = Reflection
	template_name = "detail.html"

	def get_context_data(self, **kwargs):
		form = ReplyForm
		context = {
				"timestamp" : Reflection.objects.values_list('timestamp', flat=True).get(id=self.kwargs.get('pk')),
				"name" : Reflection.objects.values_list('name', flat=True).get(id=self.kwargs.get('pk')),
				"email" : Reflection.objects.values_list('email', flat=True).get(id=self.kwargs.get('pk')),
				"category" : Reflection.objects.values_list('category', flat=True).get(id=self.kwargs.get('pk')),
				"advice" : Reflection.objects.values_list('advice', flat=True).get(id=self.kwargs.get('pk')),
				"content" : Reflection.objects.values_list('content', flat=True).get(id=self.kwargs.get('pk')),
				
				"form" : form,

				"replies" : Reply.objects.all()
		}
		return context

	def post(self, request, *args, **kwargs):
		return self.get(request, *args, **kwargs)

	def dispatch(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			form = ReplyForm(self.request.POST or None)	
			if request.POST:
				if form.is_valid():
					success = True
					user = request.POST['user']
					content = request.POST['content']
					Reply.objects.create(
						user=user,
						content = content,
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