"""
URL configuration for BookShelf_W_13 project.

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
from ksiazki import views

urlpatterns = [
    path('publishers/', views.PublisherListView.as_view(), name='publisher_list'),
    path('add_publishers/', views.AddPublisherView.as_view(), name='publisher_add'),
    path('update_publisher/<int:pk>/', views.UpdatePublisherView.as_view(), name='publisher_update'),
]
