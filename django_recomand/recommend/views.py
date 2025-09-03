from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "recommend/index.html")

def contact(request):
    return render(request, "recommend/contact.html")
def topics_listing(request):
    return render(request, "recommend/topics-listing.html")
def topics_detail(request):
    return render(request, "recommend/topics-detail.html")