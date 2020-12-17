from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product,Voter

from datetime import datetime
from django.utils import timezone
# Create your views here.

def home(request):
    products = Product.objects
    return render(request, 'products/home.html', {'products': products})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url'] and request.POST['body'] and request.FILES['image'] and request.FILES['icon']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']

            url = request.POST['url']
            if 'HTTPS://' not in url.upper() or 'HTTP://' not in url.upper():
                product.url = 'https://' + url
            else:
                product.url = url

            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            # product.pub_date = datetime.now()
            product.pub_date = timezone.datetime.now()

            product.hunter = request.user
            product.save()

            return redirect('/products/' + str(product.id))

        else:
            return render(request, 'products/create.html', {'error': 'You must fill all fields'})


    else:
        return render(request, 'products/create.html')


def details(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/details.html', {'details': product})

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        votante = Voter()

        lista_vot = [x for x in Voter.objects.filter(publish = product_id)]
        print(lista_vot)

        votante.voters = request.user
        product = get_object_or_404(Product, pk=product_id)
        votante.publish = product
        product.votes_total += 1
        votante.save()
        product.save()
        return redirect('/products/' + str(product.id))