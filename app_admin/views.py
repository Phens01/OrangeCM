from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from blog.models import Client
from blog.forms import ClientForm

def dashboard(request):
	list_clients = Client.objects.all()
	context = {"list_clients":list_clients}
	return render(request, "db.html", context)


class AddClient(CreateView):
	model = Client
	form_class = ClientForm
	template_name = "add-client.html"
	success_url = "my-clients"

	def form_valid(self, form):
		form.instance.user=self.request.user
		return super().form_valid(form)