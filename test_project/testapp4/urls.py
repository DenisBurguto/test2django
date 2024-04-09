from django.urls import path
from .views import user_form, many_fields_form, add_user, upload_image

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('form/', many_fields_form, name='form'),
    path('user/', add_user, name='add_user'),
    path('upload/', upload_image, name='upload_image'),
]
