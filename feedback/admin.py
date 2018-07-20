from django.contrib import admin
from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'phone', 'email', 'text', "form_type", 'created')
    # list_display_links = ('url', 'name')
    list_filter = ("form_type", )

    exclude = ('subject', 'urlhash', 'useragent')


admin.site.register(Feedback, FeedbackAdmin)
