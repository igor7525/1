from django.conf.urls import url

from feedback.views import FeedbackView

urlpatterns = [
        url(r'^ajax(?P<url>.*)$', FeedbackView.as_view(), name='feedback'),
    ]