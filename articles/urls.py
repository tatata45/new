from django.urls import re_path
from . import views


urlpatterns = [
    re_path(
        r'',
        views.get_post ,#get_post_puppies
        name='get_post'
    ),
    re_path(
        r'^/(?P<pk>[0-9]+)$',
        views.get_delete_update_acticle,
        name='get_delete_update_acticle'
    )
]