
from django.urls import path
from . import views
from .const import LIST_CREATE,RETRIEVE_UPDATE_DESTROY
urlpatterns = [
    path('',views.TaskViewSet.as_view(LIST_CREATE)),
    path('<int:id>/',views.TaskViewSet.as_view(RETRIEVE_UPDATE_DESTROY))

]