from django.conf.urls import  url

import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.index),
    url(r'^detail/(\d+)/$',views.bbs_detail),
    
]
