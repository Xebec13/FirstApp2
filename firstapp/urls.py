"""
URL configuration for firstapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from first import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name="index"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('create_user/', views.CreateUserView.as_view(), name='create'),
    path('add_sport/', views.AddSportView.as_view(), name='sport'),
    path('add_hall/', views.AddHallView.as_view(), name='hall'),
    path('add_event/', views.AddEventView.as_view(), name='event'),
    path('show_event/', views.ShowEventView.as_view(), name='show_event'),
    path('join_event/', views.JoinEventView.as_view(), name='join_event'),
    path('edit_event/<int:event_id>/', views.EditEventView.as_view(), name='edit_event'),
    path('delete_event/<int:event_id>/', views.DeleteEventView.as_view(), name='delete_event')
]
