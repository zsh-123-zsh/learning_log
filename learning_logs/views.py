from django.shortcuts import render
from .models import Topic
# Create your views here.
def index(request):
    return render(request,'learning_logs/index.shtml')
def topics(request):
    topics=Topic.objects.order_by('date_added')
    comtext={'topics':topics}
    return render(request,'learning_logs/topics.shtml',comtext)