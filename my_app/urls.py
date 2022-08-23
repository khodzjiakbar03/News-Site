from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('',IndexPageView.as_view(),name = 'index'),
	path('post_detail/<int:pk>',Post_DetailPageView.as_view(),name='post_detail'),
	path('category/<int:category_id>',categorypageview,name='category'),
	path('post_edit/<int:pk>/',PostUpdateView.as_view(),name='post_edit'),
	path('post_delete/<int:pk>/',PostDeleteView.as_view(),name='post_delete'),
	path('post_new/',PostCreateView.as_view(),name='post_new'),

	] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




# bu pastdagi listview url lar 👇👇👇👇  s

# urlpatterns = [
# 	path('',IndexPageView.as_view(),name = 'index'),
# 	path('post_detail/<int:pk>',Post_DetailPageView.as_view(),name='post_detail'),
# 	path('uzbekistan/',UzbekistanPageView.as_view(),name='uzbekistan'),
# 	path('sport/',SportPageView.as_view(),name='sport'),