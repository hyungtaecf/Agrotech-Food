# PROJECT VIEWS.PY
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'index.html'

class PostDetail(TemplateView):
    template_name = 'post_detail.html'

class MessageSent(TemplateView):
    template_name = 'message_sent.html'
