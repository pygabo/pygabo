from django.urls import path
from .views import PersonListView,PersonCreateView,PersonDeleteView,PersonUpdateView


urlpatterns = [
    path('', PersonListView.as_view(), name='index'),
    path('create_person/', PersonCreateView.as_view(template_name='persons/create.html'), name='create_person' ),
    path('person_delete/<int:pk>/delete', PersonDeleteView.as_view(),name='delete_person'),
    path('person_delete/<int:pk>',PersonUpdateView.as_view(template_name='persons/create.html'),name='update_person'),

]

