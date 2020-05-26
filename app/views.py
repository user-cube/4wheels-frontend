from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect

# Create your views here.
from app.forms import SignUpForm, EmailForm
from app.models import Items, Profile, Encomenda
import os
from django.db.models import Count, F, Sum
import requests
from datetime import datetime
from base64 import b64encode
from app.tools.tokenizer import Tokenizer

tokenizer = Tokenizer()



def home(request):
    """
    Get homepage view.
    Args:
        request: actual request.

    Returns:
        The homepage rendered after fetch
        Spring API.
    """
    r = requests.get("https://tqsapitests.herokuapp.com/car/")
    if r.status_code != 200:
        return FileNotFoundError()

    json = r.json()

    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
        'database': json
    }
    return render(request, 'index.html', tparams)


def login(request):
    """
    Return login page.
    Args:
        request: actual request.

    Returns:
        Rendered login page.
    """
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profiler = Profile(nome=request.POST['first_name'],
                               user=request.POST['username'],
                               picture='app/static/img/default.jpg',
                               morada=request.POST['morada'],
                               zipcode=request.POST['zipcode'],
                               pais=request.POST['pais'])
            profiler.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signUp.html', {'form': form})


def successregister(request):
    return render(request, 'successregister.html')


def getItem(request, carId):
    if request.method == 'GET':
        r = requests.get("https://tqsapitests.herokuapp.com/car/" + str(carId))
        if r.status_code != 200:
            return FileNotFoundError()
        json = r.json()

        r = requests.get("https://tqsapitests.herokuapp.com/profile/",
                         headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})

        if r.status_code != 200:
            return FileNotFoundError()
        tparams = {
            'row': json,
            'seller': r.json(),
            'year': datetime.now().year,
        }
        return render(request, 'infoItem.html', tparams)
    else:
        return redirect('home')


def search(request):
    if request.method == 'GET':
        pesquisa = request.GET['search']
        tipo = request.GET['pesquisa']
        if tipo == "brand":
            r = requests.get("https://tqsapitests.herokuapp.com/car/brand/" + pesquisa)
            if r.status_code != 200:
                return FileNotFoundError()

            json = r.json()
            tparams = {
                'database': json
            }
        if tipo == "model":
            r = requests.get("https://tqsapitests.herokuapp.com/car/model/" + pesquisa)
            if r.status_code != 200:
                return FileNotFoundError()

            json = r.json()
            tparams = {
                'database': json
            }
        if tipo == "year":
            r = requests.get("https://tqsapitests.herokuapp.com/car/year/" + pesquisa)
            if r.status_code != 200:
                return FileNotFoundError()

            json = r.json()
            tparams = {
                'database': json,
                'year': datetime.now().year,
            }
        return render(request, 'index.html', tparams)
    else:
        return redirect('home')


def getProfile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        r = requests.get("https://tqsapitests.herokuapp.com/profile/",
                         headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})
        json = r.json()
        tparams = {
            'row': json,
            'year': datetime.now().year,
        }
        return render(request, 'profile.html', tparams)


def editProfile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:

        r = requests.get("https://tqsapitests.herokuapp.com/profile/",
                         headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})
        json = r.json()
        tparams = {
            'row': json,
            'user': request.user,
            'year': datetime.now().year,
        }
        return render(request, 'editProfile.html', tparams)


def updateProfile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                image = request.FILES['picture'].file.read()
                b64pic = b64encode(image)
                image = b64pic.decode("utf-8")

            except Exception as e:
                image = request.POST['photo']
                print(e)

            content = {
                'name' : request.POST['name'],
                'mail' : request.POST['email'],
                'morada' : request.POST['address'],
                'zipCode' : request.POST['zipCode'],
                'city' : request.POST['city'],
                'nif' : request.POST['nif'],
                'photo' : image
            }

            r = requests.put("https://tqsapitests.herokuapp.com/profile/", json=content,
                             headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})

            if r.status_code != 200:
                messages.error(request, "Não foi possível atualizar o seu perfil.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

            messages.info(request, "Perfil atualizado com sucesso.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return HttpResponseForbidden()
    else:
        return redirect('login')


def painel(request):
    if request.user.is_authenticated and request.user.is_superuser:
        tparams = {
            'database': Items.objects.all()
        }
        return render(request, 'adminPanel.html', tparams)
    else:
        return redirect('home')


def addProducts(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'addItem.html')
    else:
        return redirect('home')


def processAdd(request):
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:
            adder = Items(titulo=request.POST['titulo'], short=request.POST['short'],
                          descricao=request.POST['descricao'], preco=request.POST['preco'],
                          picture=request.FILES['picture'], quantidade=request.POST['quantidade'])
            adder.save()
            return redirect('adminpanel')
        else:
            return redirect('home')
    else:
        return redirect('home')


def editProducts(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_superuser:
            tparams = {
                'database': Items.objects.filter(id=request.GET['id'])
            }
            return render(request, 'editItem.html', tparams)
        else:
            return redirect('home')
    else:
        return redirect('home')


def processEdit(request):
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:
            items = Items.objects.get(id=request.POST['id'])
            items.short = request.POST['short']
            items.titulo = request.POST['titulo']
            items.descricao = request.POST['descricao']
            items.preco = request.POST['preco']
            if 'picture' in request.FILES:
                items.picture = request.FILES['picture']
            items.quantidade = request.POST['quantidade']
            items.save()
            return redirect('/edititem?id=' + request.POST['id'])
        else:
            return redirect('home')
    else:
        return redirect('home')


def removeProducts(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_superuser:
            Items.objects.get(id=request.GET['id']).delete()
            return redirect('adminpanel')
        else:
            return redirect('home')
    else:
        return redirect('home')


def searchAdmin(request):
    if request.method == 'GET':
        pesquisa = request.GET['search']
        tparams = {
            'database': Items.objects.filter(titulo__contains=pesquisa)
        }
        return render(request, 'searchAdmin.html', tparams)
    else:
        return redirect('home')


def bought(request):
    if request.user.is_authenticated:
        tparams = {
            "database": Encomenda.objects.filter(user=request.user).order_by("-id"),
            "year": datetime.now().year
        }
        return render(request, "salesList.html", tparams)
    else:
        return redirect('login'
                        '')


def boughtAdmin(request):
    if request.user.is_superuser and request.user.is_authenticated:
        tparams = {
            "database": Encomenda.objects.all().order_by("-id"),
            "year": datetime.now().year
        }
        return render(request, "salesListAdmin.html", tparams)
    else:
        return redirect('home')


def boughtSearch(request):
    if request.method == "GET" and 'search' in request.GET:
        if request.user.is_authenticated:
            tparams = {
                "database": Encomenda.objects.filter(user=request.user,
                                                     produtos__titulo__contains=request.GET['search']).order_by("-id"),
                "year": datetime.now().year
            }
            return render(request, "salesList.html", tparams)
        else:
            return redirect('login')
    else:
        return redirect('home')


def boughtSearchAdmin(request):
    if request.method == "GET" and 'search' in request.GET:
        if request.user.is_authenticated and request.user.is_superuser:
            tparams = {
                "database": Encomenda.objects.filter(produtos__titulo__contains=request.GET['search']).order_by("-id"),
                "year": datetime.now().year
            }
            return render(request, "salesList.html", tparams)
        else:
            return redirect('login')
    else:
        return redirect('home')


def buyItem(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            adder = Encomenda(user=request.user, produtos=Items.objects.get(id=request.POST['id']))
            adder.preco = Items.objects.get(id=request.POST['id']).preco
            adder.total = adder.preco * adder.quantidade
            adder.save()

            Items.objects.filter(id=request.POST['id']).update(quantidade=F('quantidade') - 1)

            send_mail(subject='Compra efetuada com sucesso',
                      message='A tua compra já se encontra disponível no painel de itens comprados.\nPodes aceder em: https://xpto-store.herokuapp.com/boughtlist/\nGratos pela tua preferência,\nXPTO Store',
                      from_email=os.getenv('EMAIL'),
                      recipient_list=[request.user.email]
                      )
            messages.info(request, "Compra efetuada com sucesso!")
            return redirect('boughtlist')
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('login')


def sendEmail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            mensagem = form.cleaned_data.get('message')

            if phone != None:
                send_mail(subject='Contacto de ' + name,
                          message=mensagem + "\nEste email foi enviado por: " + email + "\nContacto telefónico: " + str(
                              phone),
                          from_email=os.getenv('EMAIL'),
                          recipient_list=[os.getenv('EMAIL_TO'), os.getenv('EMAIL'), email]
                          )
            else:
                send_mail(subject='Contacto de ' + name,
                          message=mensagem + "\nEste email foi enviado por: " + email,
                          from_email=os.getenv('EMAIL'),
                          recipient_list=[os.getenv('EMAIL_TO'), os.getenv('EMAIL'), email]
                          )

            messages.success(request, 'Email sent')
            return redirect('contact')


def openCharts(request):
    if request.user.is_superuser:
        stock = Items.objects.all()
        lista = [['Items', 'Quantidade']]
        for i in stock:
            lista.append([i.titulo, i.quantidade])
        return render(request, 'charts.html', {'lista': lista})
    else:
        raise PermissionDenied()


def analiseMes(request):
    if request.user.is_superuser:
        x = datetime.now()
        vendas = Encomenda.objects.filter(data__month=x.month, data__year=x.year).values('produtos_id').annotate(
            num=Count('produtos'))
        lista = [['Item', 'Quantidade']]
        for i in vendas:
            nome = Items.objects.filter(id=i['produtos_id'])
            for u in nome:
                lista.append([u.titulo, i['num']])
        return render(request, 'analiseVendas.html', {'lista': lista})
    else:
        raise PermissionDenied()


def analise(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        dinheiro = Encomenda.objects.filter(user=request.user).aggregate(Sum('total'))
        compras = Encomenda.objects.filter(user=request.user).aggregate(Count('id'))

        vendas = Encomenda.objects.filter(user=request.user).values('produtos_id').annotate(
            num=Count('produtos'))
        lista = [['Item', 'Quantidade']]
        for i in vendas:
            nome = Items.objects.filter(id=i['produtos_id'])
            for u in nome:
                lista.append([u.titulo, i['num']])

        tparams = {
            'database': Profile.objects.filter(user=request.user),
            'dinheiro': dinheiro['total__sum'],
            'compras': compras['id__count'],
            'lista': lista
        }
        return render(request, 'estatistica.html', tparams)
    else:
        if request.user.is_superuser:
            raise PermissionDenied()
        else:
            redirect('login')


def evolucaoAdmin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        encomendas = Encomenda.objects.all().values('produtos_id', 'data').annotate(
            num=Count('produtos'))

        lista = []
        for i in encomendas:
            print(i)
            lista.append([i['data'].strftime("%m/%d/%Y"), i['num']])

        return render(request, 'compras.html', {'lista': lista, 'header': 'Compras ao longo do tempo'})
    else:
        raise PermissionDenied()


def getFavourites(request):
    """
    Return all favorites by a user.
    Args:
        request: the request.

    Returns:
        A view with all favorites for a user.

    """
    if request.user.is_authenticated:
        r = requests.get("https://tqsapitests.herokuapp.com/favourite/",
                         headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})
        if r.status_code != 200:
            return FileNotFoundError()

        try:
            json = r.json()
        except Exception as e:
            print(e)
            return render(request, 'favourite.html', {'database': []})

        ids = []
        lista = []
        lista.append(json)
        for i in lista:
            ids.append(i['id'])

        cars = []
        for i in ids:
            car = requests.get("https://tqsapitests.herokuapp.com/car/" + str(i))
            cars.append(car.json())

        tparams = {
            'database': cars,
            'year': datetime.now().year,
        }
        return render(request, 'favourite.html', tparams)
    else:
        return redirect('login')


def deleteFavourite(request, favID):
    if request.user.is_authenticated:
        r = requests.delete("https://tqsapitests.herokuapp.com/favourite/" + str(favID),
                            headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})

        if r.status_code != 200:
            messages.error(request, "Não foi possível apagar o favorito.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        messages.info(request, "Favorito removido com sucesso.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return redirect('login')
