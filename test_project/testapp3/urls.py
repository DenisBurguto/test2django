from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello_class/', views.HelloView.as_view(), name='helloclass'),
    path('posts/<int:year>/', views.year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', views.MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('my/<str:name>', views.my_view, name='my'),
    path('', views.TemplIf.as_view(), name='if'),
    path('for/', views.view_for, name='for'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('author/<int:author_id>/',views.author_posts, name='author_posts'),
    path('post/<int:post_id>/', views.post_full, name='post_full'),
]
