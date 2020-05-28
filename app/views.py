from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from app.forms import SignUpForm
from app.models import Profile
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
        the homepage rendered after fetch
        Spring API.

    """
    r = requests.get("https://tqsapitests.herokuapp.com/car/")
    if r.status_code != 200:
        return HttpResponseNotFound()

    json = r.json()

    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
        'database': json
    }
    if request.user.is_authenticated:
        isTyped = tokenizer.checkUserType(request)
        if not isTyped:
            isOk = tokenizer.getType(request)
            if not isOk:
                return HttpResponseNotFound()

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
            authenticate(username=username, password=raw_password)
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


def successRegister(request):
    return render(request, 'successregister.html')


def getItem(request, carId):
    """
    Get information for a particular item.
    Args:
        request: actual request.
        carId: car id to display
        information

    Returns:
        the information for a
        specific car id.
    """
    if request.method == 'GET':
        r = requests.get("https://tqsapitests.herokuapp.com/car/" + str(carId))
        if r.status_code != 200:
            return FileNotFoundError()
        json = r.json()

        r = requests.get("https://tqsapitests.herokuapp.com/profile/",
                         headers={'Authorization': 'Bearer ' + tokenizer.genToken(json['ownerMail'])})
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
    """
    Allow users to search for brand,
    model and year.
    Args:
        request: actual request.

    Returns:
        a rendered view with the
        search results.
    """
    if request.method == 'GET':
        content = request.GET['search']
        tipo = request.GET['pesquisa']
        isOk = False
        if tipo == "brand":
            r = requests.get(
                "https://tqsapitests.herokuapp.com/car/brand/" + content)
            if r.status_code != 200:
                return FileNotFoundError()
            isOk = True
        if tipo == "model":
            r = requests.get(
                "https://tqsapitests.herokuapp.com/car/model/" + content)
            if r.status_code != 200:
                return FileNotFoundError()
            isOk = True
        if tipo == "year":
            r = requests.get(
                "https://tqsapitests.herokuapp.com/car/year/" + content)
            if r.status_code != 200:
                return FileNotFoundError()
            isOk = True
        if isOk:
            json = r.json()
            tparams = {
                'database': json,
                'year': datetime.now().year,
            }
            return render(request, 'index.html', tparams)
        else:
            return render(request, 'index.html', {'database': [], 'year': datetime.now().year})
    else:
        return redirect('home')


def getProfile(request, edit):
    """
    Get user profile information.
    Args:
        request: actual request.

    Returns:
        a view with all user
        profile information.
    """
    if request.user.is_authenticated:
        r = requests.get("https://tqsapitests.herokuapp.com/profile/",
                         headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})
        if r.status_code != 200:
            return redirect('home')

        json = r.json()
        tparams = {
            'row': json,
            'year': datetime.now().year,
        }
        if edit == "edit":
            return render(request, 'editProfile.html', tparams)
        else:
            return render(request, 'profile.html', tparams)
    else:
        return redirect('login')


def updateProfile(request):
    """
    Update profile information.
    Args:
        request: actual request.

    Returns:
        the profile edited or an
        error message.
    """
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
                'name': request.POST['name'],
                'mail': request.user.email,
                'address': request.POST['morada'],
                'zipCode': request.POST['zipcode'],
                'city': request.POST['city'],
                'nif': request.POST['nif'],
                'photo': image
            }

            r = requests.put("https://tqsapitests.herokuapp.com/profile/", json=content,
                             headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})

            if r.status_code != 200:
                messages.error(
                    request, "Não foi possível atualizar o seu perfil.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

            messages.info(request, "Perfil atualizado com sucesso.")
            return redirect('profile', edit="view")
        else:
            return HttpResponseForbidden()
    else:
        return redirect('login')


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
            car = requests.get(
                "https://tqsapitests.herokuapp.com/car/" + str(i))
            cars.append(car.json())

        tparams = {
            'database': cars,
            'year': datetime.now().year,
        }
        return render(request, 'favourite.html', tparams)
    else:
        return redirect('login')


def deleteFavourite(request, favID):
    """
    Delete a item from favourite list.
    Args:
        request:actual request.
        favID: favourite (item) id.

    Returns:
        the list of the favourite items.
    """
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
