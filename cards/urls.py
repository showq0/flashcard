from django.urls import path
from django.views.generic import TemplateView
from cards.views import CardListView, CardCreateView, CardEditView,BoxView

urlpatterns = [
    path('card-list',CardListView.as_view(), name= "card-list" ),
    path('create-card',CardCreateView.as_view(), name= "create-card" ),
    path('edit-card/<int:pk>',CardEditView.as_view(), name= "edit-card" ),
    path('box/<int:box_num>',BoxView.as_view(), name= "box-view" ),



]
