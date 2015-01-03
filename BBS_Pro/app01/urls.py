from django.conf.urls import include, url

import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.index),
]
