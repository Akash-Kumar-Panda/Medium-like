from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path("<int:com_id>",views.update_comment),
    path("",views.update_comment,name="add"),
    path("delete/<int:comment_id>",views.delete_comment),
]
