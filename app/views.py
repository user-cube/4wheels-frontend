from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from app.forms import SignUpForm
import requests
from datetime import datetime
from base64 import b64encode
from app.tools.tokenizer import Tokenizer
from dotenv import load_dotenv
import os
import logging

tokenizer = Tokenizer()
logger = logging.getLogger(__name__)

load_dotenv()
API = os.getenv('API')
API2 = os.getenv('API2')
API3 = os.getenv('API3')
API4 = os.getenv('API4')

def home(request, carPage=0):
    """
    Get homepage view.
    Args:
        request: actual request.

    Returns:
        the homepage rendered after fetch
        Spring API.

    """

    if request.user.is_authenticated:
        isTyped = tokenizer.checkUserType(request)
        if not isTyped:
            isOk = tokenizer.getType(request)
            if not isOk:
                return HttpResponseNotFound()

    if carPage != 0:
        carPage = carPage - 1
    r = requests.get(API4 + "car/?page=" + str(carPage) + "&limit=6")
    if r.status_code != 200:
        print(r.status_code)
        return HttpResponseNotFound()

    json = r.json()

    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
        'database': json['data'],
        ''
        'carPage' : carPage,
        'prev': carPage,
        'next': carPage + 2,
        'last': json['totalpages'],
        'real' : carPage + 1,
        'typeOfPage' : 'cars'
    }
    return render(request, 'index.html', tparams)


def login(request):
    """
    Return login page.
    Args:
        request: actual request.

    Returns:
        rendered login page.
    """
    return render(request, 'login.html', {'year': datetime.now().year, })


def signup(request):
    """
    Allow users to sign up
    using django register
    and API Call.
    Args:
        request: actual request.

    Returns:
        sign up page.
    """
    if request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        try:
            image = request.FILES['picture'].file.read()
            b64pic = b64encode(image)
            image = b64pic.decode("utf-8")
        except Exception as e:
            image = None
            print(e)

        msg = {
            'username': request.POST['email'],
            'password': request.POST['password1']
        }
        r = requests.post(API +
                          "register", json=msg)
        if r.status_code != 200:
            print(r.status_code)
            messages.error(request, "Impossível criar conta.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        msg = {
            'name': request.POST['first_name'] + " " + request.POST['last_name'],
            'address': request.POST['morada'],
            'zipCode': request.POST['zipcode'],
            'city': request.POST['city'],
            'nif': int(request.POST['nif']),
            'type': int(request.POST['typeOfUser']),
            'photo': image,
            'mail': request.POST['email'],
            'contact': int(request.POST['contact']),
            'id': 0
        }

        r = requests.post(API + "profile/", json=msg,
                          headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.POST['email'])})
        if r.status_code != 200:
            print(r.status_code)
            messages.error(request, "Impossível criar conta.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signUp.html', {'form': form, 'year': datetime.now().year})


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
        r = requests.get(API2 + "car/" + str(carId))
        if r.status_code != 200:
            print("Car " + str(r.status_code))
            return HttpResponseNotFound()
        json = r.json()
        r = requests.get(API + "profile/",
                         headers={'Authorization': 'Bearer ' + tokenizer.genToken(json['ownerMail'])})
        if r.status_code != 200:
            print("Profile " + str(r.status_code))
            return HttpResponseNotFound()
        seller = r.json()
        isFav = False
        if request.user.is_authenticated:
            r = requests.get(API + "favourite/",
                             headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})
            if r.status_code != 200:
                print("Favourite " + str(r.status_code))
                return HttpResponseNotFound()

            try:
                favs = r.json()
                for i in favs:
                    if i['car'] == carId:
                        isFav = True
            except Exception as e:
                print(e)
                isFav = False

        tparams = {
            'row': json,
            'seller': seller,
            'year': datetime.now().year,
            'isFav': isFav
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
                API2 + "car/brand/" + content)
            if r.status_code != 200:
                return HttpResponseNotFound()
            isOk = True
        if tipo == "model":
            r = requests.get(
                API2 + "car/model/" + content)
            if r.status_code != 200:
                return HttpResponseNotFound()
            isOk = True
        if tipo == "year":
            r = requests.get(
                API2 + "car/year/" + content)
            if r.status_code != 200:
                return HttpResponseNotFound()
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


@login_required
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
        r = requests.get(API + "profile/",
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


@login_required
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

            r = requests.put(API + "profile/", json=content,
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


@login_required
def getFavourites(request):
    """
    Return all favorites by a user.
    Args:
        request: the request.

    Returns:
        A view with all favorites for a user.
    """
    if request.method == "GET":
        if 'user_type' in request.session.keys():
            if request.session.get('user_type') == 0:
                r = requests.get(API + "favourite/",
                                 headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})
                if r.status_code != 200:
                    return HttpResponseNotFound()

                try:
                    json = r.json()
                except Exception as e:
                    logger.info(str(e))
                    return render(request, 'favourite.html', {'database': []})

                ids = []
                for i in json:
                    ids.append(i['car'])

                cars = []
                for i in ids:
                    car = requests.get(API2 + "car/" + str(i))
                    if car.status_code == 200:
                        print(car.text)
                        cars.append(car.json())
                        print(cars)

                tparams = {
                    'database': cars,
                    'year': datetime.now().year,
                }
                return render(request, 'favourite.html', tparams)
            else:
                return HttpResponseForbidden()
        else:
            return redirect('login')
    else:
        return HttpResponseBadRequest()


@login_required
def deleteFavourite(request, favID):
    """
    Delete a item from favourite list.
    Args:
        request:actual request.
        favID: favourite (item) id.

    Returns:
        the list of the favourite items.
    """
    if 'user_type' in request.session.keys():
        if request.session.get('user_type') == 0:
            r = requests.delete(API + "favourite/" + str(favID),
                                headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})

            if r.status_code != 200:
                messages.error(request, "Não foi possível apagar o favorito.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

            messages.info(request, "Favorito removido com sucesso.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return HttpResponseForbidden()
    else:
        return redirect('login')


@login_required
def addFavourites(request, favID):
    """
    Add a car to favourites.
    Args:
        request: actual request.
        favID: car id to store.

    Returns:
        car id detail page.
    """
    if 'user_type' in request.session.keys():
        if request.session.get('user_type') == 0:
            r = requests.post(API + "favourite/" + str(favID),
                              headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})
            if r.status_code != 200:
                messages.error(request, "Erro ao adicionar favorito")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return HttpResponseForbidden()

    else:
        return redirect('login')


@login_required
def sellerPanel(request, typeOfPanel, page):
    """
    Get seller panel.
    Args:
        request: actual request.
        typeOfPanel: type of panel to
        be rendered

    Returns:
        the panel rendered.
    """
    if request.method == "GET":
        if 'user_type' in request.session.keys():
            if request.session.get('user_type') == 1:
                page = page -1
                r = requests.get(API4 + "car/vendor?page=" + str(page) + "&limit=6",
                                 headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})
                if r.status_code != 200:
                    logger.info("sellerPanel() - API CODE: " + str(r.status_code))
                    return HttpResponseNotFound()

                json = r.json()
                lista = []
                if typeOfPanel == "selling":
                    for i in json:
                        if i['carState'] == "selling":
                            lista.append(i)
                else:
                    for i in json:
                        if i['carState'] == "sold":
                            lista.append(i)

                tparams = {
                    'year': datetime.now().year,
                    'database': lista,
                    'typeOfPanel': typeOfPanel,
                    'carPage': page,
                    'prev': page,
                    'next': page + 2,
                }
                return render(request, 'sellerPanel.html', tparams)
            else:
                return HttpResponseForbidden()
        else:
            return redirect('login')
    else:
        return HttpResponseBadRequest()


@login_required
def deleteCarFromSale(request, carID):
    """
    Delete a car from sale.
    Args:
        request: actual request.
        carID: car id to be deleted.

    Returns:
        the seller panel with a
        message.
    """
    if 'user_type' in request.session.keys():
        if request.session.get('user_type') == 1:
            r = requests.delete(API2 + "car/" + str(carID),
                                headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})

            if r.status_code != 200:
                logger.info("deleteCarFromSale() - API CODE: " + str(r.status_code))
                messages.error(request, "Erro ao apagar item.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

            messages.info(request, "Item apagado com sucesso.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return HttpResponseForbidden()
    else:
        return redirect('login')


@login_required
def editCar(request, carID):
    """
    Allow user to edit a car.
    Args:
        request: actual request.
        carID: car id to edit.

    Returns:
        a rendered page to
        edit a car.
    """
    if 'user_type' in request.session.keys():
        if request.session.get('user_type') == 1:
            r = requests.get(API2 + "car/" + str(carID))
            if r.status_code != 200:
                logger.info("editCar() - API CODE: " + str(r.status_code))
                messages.error(request, "Erro ao editar item.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

            return render(request, 'editCar.html', {'row': r.json(), 'year': datetime.now().year})
        else:
            return HttpResponseForbidden()
    else:
        return redirect('login')


@login_required
def saveEdit(request):
    """
    Save a car edited.
    Args:
        request: actual request.

    Returns:
        the car edited by the user.
    """
    if request.method == "POST":
        if 'user_type' in request.session.keys():
            if request.session.get('user_type') == 1:
                try:
                    image = request.FILES['picture'].file.read()
                    b64pic = b64encode(image)
                    image = b64pic.decode("utf-8")

                except Exception as e:
                    image = request.POST['photo']
                    print(e)

                content = {
                    'brand': request.POST['brand'],
                    'model': request.POST['model'],
                    'month': request.POST['month'],
                    'year': request.POST['year'],
                    'description': request.POST['description'],
                    'typeOfFuel': request.POST['typeOfFuel'],
                    'kilometers': request.POST['kilometers'],
                    'price': request.POST['price'],
                    'id': request.POST['carID'],
                    'ownerMail': request.user.email,
                    'photo': image
                }

                r = requests.put(API2 + "car/" + str(request.POST['carID']), json=content,
                                 headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})

                if r.status_code != 200:
                    logger.info("saveEdit() - API CODE: " + str(r.status_code))
                    messages.error(
                        request, "Não foi possível atualizar as informações do carro")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

                messages.info(request, "Informações atualizadas com sucesso")
                return redirect('sellerpanel', typeOfPanel="selling")
            else:
                return HttpResponseForbidden()
        else:
            return redirect('login')
    else:
        return HttpResponseBadRequest()


@login_required
def addCar(request):
    """
    Add a car to database.
    Args:
        request: actual request.

    Returns:
        a page to add a car
        into the database.
    """
    if 'user_type' in request.session.keys():
        if request.session.get('user_type') == 1:
            return render(request, 'addCar.html')
        else:
            return HttpResponseForbidden()
    else:
        return redirect('login')


@login_required
def saveCar(request):
    """
    Sent edited information
    into the Spring API.
    Args:
        request: actual request.

    Returns:
        the page after save car
        information.
    """
    if request.method == "POST":
        if 'user_type' in request.session.keys():
            if request.session.get('user_type') == 1:
                try:
                    image = request.FILES['picture'].file.read()
                    b64pic = b64encode(image)
                    image = b64pic.decode("utf-8")
                except Exception as e:
                    logger.info("saveCar() : Error with image uploading" + str(e))
                    messages.error(
                        request, "Não foi possível criar um carro")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

                content = {
                    "car": {
                        'brand': request.POST['brand'],
                        'model': request.POST['model'],
                        'month': request.POST['month'],
                        'year': request.POST['year'],
                        'description': request.POST['description'],
                        'typeOfFuel': request.POST['typeOfFuel'],
                        'kilometers': request.POST['kilometers'],
                        'price': request.POST['price'],
                        'ownerMail': request.user.email,
                        'photo': image,
                        'carState': "selling"
                    }
                }

                r = requests.post(API2 + "car/", json=content,
                                  headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})

                if r.status_code != 200:
                    logger.info("saveCar() - API CODE: " + str(r.status_code))
                    messages.error(
                        request, "Não foi possível adicionar o carro")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

                messages.info(request, "Carro adicionado com sucesso")
                return redirect('sellerpanel', typeOfPanel="selling", page=1)
            else:
                return HttpResponseForbidden()
        else:
            return redirect('login')
    else:
        return redirect('login')


@login_required
def sellCarFromSale(request, carID):
    """
    Mark a car as sold.
    Args:
        request: actual request.
        carID: car to mark as sold.

    Returns:
        a list with all cars from
        user.
    """
    if 'user_type' in request.session.keys():
        if request.session.get('user_type') == 1:
            r = requests.put(API2 + "car/sold/" + str(carID),
                             headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})

            if r.status_code != 200:
                messages.error(request, "Erro ao adicionar como vendido.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

            messages.info(request, "Alteração do estado para vendido.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return HttpResponseForbidden()
    else:
        return redirect('login')

@login_required
def listAllUsers(request, typeUser, pageID):
    if 'user_type' in request.session.keys():
        if request.session.get('user_type') == 2:
            pageID = pageID - 1

            if typeUser == "vendors":
                r = requests.get(API3 + "users/vendors?page=" + str(pageID) + "&limit=12",  headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})

                if r.status_code != 200:
                    logger.info("listAllUsers(): API CODE - " +  str(r.status_code))
                    messages.error(request, "Something went wrong.")
                    return HttpResponseBadRequest()

                json = r.json()
            elif typeUser == "buyers":
                r = requests.get(API3 + "users/buyers?page=" + str(pageID)  + "&limit=12", headers={'Authorization': 'Bearer ' + tokenizer.genToken(request.user.email)})

                if r.status_code != 200:
                    logger.info("listAllUsers(): API CODE - " + str(r.status_code))
                    messages.error(request, "Something went wrong.")
                    return HttpResponseBadRequest()

                json = r.json()

            else:
                return HttpResponseBadRequest()

            tparams = {
                'database': json['data'],
                'typeOfList' : typeUser,
                'prev' : pageID,
                'next' : pageID + 2,
                'pageID' : pageID,
                'real' : pageID + 1,
                'last' : json['totalpages'],
                'year': datetime.now().year,
            }

            return render(request, 'listAllUsers.html', tparams)
        else:
            return HttpResponseForbidden()
    else:
        return redirect('login')