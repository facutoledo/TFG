from django.contrib.auth.decorators import login_required
from django.urls import path, reverse_lazy
from .views import BienvenidaView

urlpatterns = [
    path('', login_required(BienvenidaView.as_view()),
         name='bienvenida'),
]