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
    path('categories/', views.CategoryListView.as_view(), name='categories_list'),
    path('add_category/', views.AddCategoryView.as_view(), name='category_add'),
    path('update_category/<int:pk>/', views.UpdateCategoryView.as_view(), name='category_update'),
    path('add_author/', views.AddAuthorView.as_view(), name='add_author'),
    path('author_list/', views.AddAuthorView.as_view(), name='author_list'),
    path('update_author/<int:pk>/', views.UpdateAuthorView.as_view(), name='author_update'),
    path('add_book/', views.AddBookView.as_view(), name='book_add'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('detail_book/<int:pk>/', views.DetailBookView.as_view(), name='book_detail'),
    path('edit_comment/<int:pk>/', views.EditCommentView.as_view(), name='edit_comment'),
]
