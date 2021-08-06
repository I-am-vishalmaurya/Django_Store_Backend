from django.shortcuts import render
from django.db.models import Value, F, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from store.models import Product, Customer
from tags.models import TaggedItems

# Create your views here.

def sayhello(request):
    query_set = TaggedItems.objects.get_tags_for(Product, 1)
    return render(request, 'index.html', {'name': 'Vishal Maurya', 'result': list((query_set))})
