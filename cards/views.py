from django.views.generic import ListView , CreateView, UpdateView
from cards.models import Card
from django.urls import reverse_lazy 
from django.shortcuts import get_object_or_404, redirect
from cards.forms import CardCheckForm
import random
# Create your views here.


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box")
    template_name = "cards/card_list.html" # we can skip this


class CardCreateView (CreateView):
    model = Card
    fields = ["question","answer","box"]
    success_url = reverse_lazy("create-card")


class CardEditView (UpdateView):
    model = Card
    fields = ["question","answer","box"]
    success_url = reverse_lazy("card-list")
 

class BoxView(ListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        quetyset = Card.objects.filter(box=self.kwargs["box_num"])
        return quetyset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            solved = form.cleaned_data["solved"]
            card.move(solved)
        return redirect(request.META.get("HTTP_REFERER"))