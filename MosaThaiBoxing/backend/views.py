from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Trainer, Price, Merchandise, Feedback, TrainingRegistration, Contact, AboutUs
from .serializers import (
    PostSerializer,
    TrainerSerializer,
    PriceSerializer,
    MerchandiseSerializer,
    FeedbackSerializer,
    TrainingRegistrationSerializer,
    ContactSerializer,
    AboutUsSerializer,
)


def main(request):
    return render(request, 'base.html')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class TrainingRegistrationViewSet(viewsets.ModelViewSet):
    queryset = TrainingRegistration.objects.all()
    serializer_class = TrainingRegistrationSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer