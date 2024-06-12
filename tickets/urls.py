from django.urls import path
from .views import home
from .views import Create, ListPosts, PostDetail
#from .views import CustomLoginView

urlpatterns = [
    path('', home, name="home"),
    path('create', Create.as_view(), name="create"),
    path('list', ListPosts.as_view(), name= "list"),
    path('detail/<int:pk>', PostDetail.as_view(), name="detail")
]

