from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('faces-of-war', views.FacesOfWar, name='faces_of_war'),

    path('<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('faces-of-war/<int:pk>', views.FacesOfWarDetailView.as_view(), name='face_detail'),

    path('add-face', views.AddFacePage, name='add_face'),
    path('edit-face/<int:id>', views.EditFace),
    path('delete-face/<int:id>', views.DeleteFace),

    path('add-article', views.AddArticlePage, name='add_article'),
    path('edit-article/<int:id>', views.EditArticle),
    path('delete-article/<int:id>', views.DeleteArticle),

    path('add-quote', views.AddQuotePage, name='add_quote'),
    path('quotes', views.Quotes, name='quotes'),

    path('logout', views.Logout, name='logout'),
]

handler404 = "main.views.page_not_found_view"