from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.utils import timezone

from .models import Animal, Species


class AnimalPopulationView(View):

    def get(self, request):
        return HttpResponse()


class AnimalView(View):

    def get(self, request):
        return JsonResponse({})

    def post(self, request):
        return JsonResponse({})


class HungryAnimalsView(View):

    def get(self, request):
        return HttpResponse()


class FeedAnimalView(View):

    def post(self, request):
        return HttpResponse()
