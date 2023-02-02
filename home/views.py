from django.shortcuts import render
from django.views.generic import View

from .models import *

# Create your views here.
class BaseView(View):
    views = {}
    views['categories'] = Category.object.all()


class HomeView(View):
    def get(self, request):
        self.views['categories']= Category.object.all()
        self.views['subcategories']= SubCategory.object.all()
        self.views['sliders']= Slider.object.all()
        self.views['ads']= Ad.object.all()
        self.views['brands']= Brand.object.all()
        self.views['reviews']= Review.object.all()
        self.views['news_product']= Product.object.filter(labels='new')
        self.views['hot_product']= Product.object.filter(labels='hot')
        self.views['sale_product']= Product.object.filter(labels='sale')


        return render(request, 'index.html', self.views)

