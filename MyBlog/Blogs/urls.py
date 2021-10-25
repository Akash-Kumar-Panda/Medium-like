from django.urls import path
from . import views

app_name = "blogs" 

urlpatterns = [
    path('<int:blog_id>/', views.fetchBlog),
    path('update/<int:blog_id>', views.updateBlog),
    path('update/', views.updateBlog,name = "update"),
    path('delete/<int:blog_id>', views.deleteBlog,),
]

