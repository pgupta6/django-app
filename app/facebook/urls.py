"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from facebook import views



router = DefaultRouter()
# router.register('user', views.UserViewSet)
# router.register('post', views.PostViewSet)
# router.register('comment', views.CommentViewSet)
# router.register('postToComment', views.PostToCommentViewSet)
#router.register('Item', views.ItemViewSet)
router.register('ItemCSV', views.ItemCSVViewSet)


app_name = 'facebook'

urlpatterns = [
    path('', include(router.urls)),
    #path('api/data', views.parse_item, name='parse_data')
]
