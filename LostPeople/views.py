import arrow as arrow
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime

from .models import Missed , Comments
from Products.models import Product

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout,authenticate
import cognitive_face as CF

from django.contrib.auth.decorators import login_required
#from . import forms

def ShowMissed(request):
    misseds = Missed.objects.all().order_by('date');
    return render(request, 'LostPeople/ShowMissed.html', { 'misseds': misseds })

def Child(request):
    misseds = Missed.objects.all().order_by('age');
    child = []
    for x in misseds :
        Age = x.age
        if Age<=20:
            child.append(x)
    return render(request, 'LostPeople/Child.html', { 'child': child })

def Adult(request):
    misseds = Missed.objects.all().order_by('age');
    adult = []
    for x in misseds :
        Age = x.age
        if Age>20:
            adult.append(x)
    return render(request, 'LostPeople/Adult.html', { 'adult': adult })

def ShowWating(request):
    watings = Missed.objects.all();
    #watings = Missed.objects.get(Accept=False).Accept
    return render(request, 'LostPeople/ShowWating.html', { 'watings': watings })

def missed_detail(request, id):
    # return HttpResponse(slug)
    missed = Missed.objects.get(id=id)
    comments = Comments.objects.filter(idCard=id)
    return render(request, 'LostPeople/detiles.html', { 'missed': missed, 'comments':comments })

#@login_required(login_url="/accounts/login/")
def missed_create(request):
    if request.method == 'POST':
        missed = Missed()
        missed.name = request.POST['nameM']
        print( missed.name)
        missed.location = request.POST['location']
        missed.age = request.POST['Age']
        missed.Name_Founder = request.POST['NameFR']
        missed.Phone_Founder = request.POST['phone']
        missed.Img = request.FILES['IMG']
        # save article to db
        img = request.FILES['IMG']
        #check = SearchByImGAuto(request,img)
        base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
        CF.BaseUrl.set(base_url)
        key = '17f9a54e963a4ff8806be407739f928c'  # Replace with a valid Subscription Key here.
        CF.Key.set(key)
        SearchedImg = CF.face.detect(img)
        # Assume the first face is the one we want to compare
        if SearchedImg is not None:
            SearchIMG = SearchedImg[0]['faceId']
            print("SearchedImg:" + SearchIMG)
            misseds = Missed.objects.all().order_by('date')
            ID = -1
            for temp in misseds:
                face = CF.face.detect(temp.Img)
                if face is not None:
                    DataIMG = face[0]['faceId']
                    print("Data Img:" + DataIMG)
                    similarity = CF.face.verify(SearchIMG, DataIMG)
                    if similarity['isIdentical'] == True:
                        print('matching success ')
                        ID = temp.id
                        break
                    # faces[face] = temp.id
            if ID != -1:
                print('it is in data base')
                messages.warning(request, 'The image is exist in Database , this is info for your missed!')
                return redirect('LostPeople:detail', id=ID)
            else:
                print('not found')
                missed.save()
                messages.success(request, 'Add is success , Hope to  fined your missed!')
                return redirect('home')
    return render(request, 'LostPeople/CreatMissed.html', )

def accept(request,id2):
    missed = Missed.objects.get(id=id2)
    missed.Accept = True
    missed.save()

    return redirect('LostPeople:wait')
    #render(request,'LostPeople/ShowWating.html',{'watings': watings})
'''def Search(request):
    Name = request.GET.get('s')
    age1 = request.GET.get('age')
    
    if age1 is "1-10":
        fillterd = Missed.objects.all().filter(Missed.age is range(1,10))
    elif age1 is "11-20":
        fillterd = Missed.objects.all().filter(Missed.age is range(11,20))
        #age in range(11, 20)
    else:
        fillterd = Missed.objects.all()
    missed = fillterd.filter(name=Name)

    return render(request,'LostPeople/ShowResults.html',{'S': Name , 'missed':missed , 'fillterd':fillterd})
    #return render(request,'LostPeople/ShowResults.html',{'S': Name , 'age':age })
'''


def Search(request):
    Name = request.GET.get('SearchedName')
    age1 = request.GET.get('age')
    dateS = request.GET.get('bday')
    print('date : ',dateS,' age : ' , age1 , 'name : ',Name)
    print('date search : ',dateS,' now : ',datetime.now().date())
    #temp = Missed.objects.filter(date__range=[date,datetime.now().date()])

    if dateS=='None' or dateS=='':
        print('no dateeeee')
        temp = Missed.objects.all()
    else:
        print('not none')
        Date = arrow.get(dateS)
        if Date.date()>=datetime.now().date():
            print('no dateeeee')
            temp = Missed.objects.all()
        else:
            print('datttte')
            temp = Missed.objects.filter(date__range=[Date.date(),datetime.now().date()])
    arr = []
    Farr=[]
    for x in temp :
        ageF = x.age
        NameData = x.name
        print('Name data ' , NameData)
        print(ageF)
        if age1=='ten':
            if ageF > 1 and ageF < 10 and(NameData==Name or Name=='' or Name=='None'):
                arr.append(x)
                print('1000000000000000000')
        elif age1=='twin' :
            if ageF > 11 and ageF < 20 and (NameData==Name or Name==''or Name=='None'):
                arr.append(x)
                print('20000000000000000000')
        elif age1=='Up20':
            if ageF > 20 and (NameData==Name or Name==''or Name=='None') :
                print('Up20')
                arr.append(x)
        else:
            if  (NameData==Name or Name==''or Name=='None') :
                arr.append(x)
                print(ageF)
                print('all')
    print(len(arr))
    return render(request, 'LostPeople/ShowResults.html', {'Name': Name,'age1':age1,'arr':arr,'Farr':Farr})


def GetSection(request):
    misseds = Missed.objects.all().order_by('age');
    reverse = Missed.objects.all().order_by('age').reverse();
    products = Product.objects.all();
    child=[]
    Adult=[]
    p=[]
    '''for x in misseds :
        Age = x.age
        if Age<=20:
            child.append(x)
        else:
            Adult.append(x)'''
    for i in range(0,3):
        if i<misseds.count():
            Age = misseds[i].age
            if Age<=20:
                child.append(misseds[i])
            else:
                continue
        else:
            break


    for i in range(0,3):
        if i<reverse.count():
            Age = reverse[i].age
            if Age>20:
                Adult.append(reverse[i])
            else:
                break
        else:
            break

    for i in range(0,3):
        if i<products.count():
            p.append(products[i])
        else:
            break


    '''child.append(misseds[0])
    child.append(misseds[1])
    child.append(misseds[2])

    misseds.order_by('age').reverse()
    Adult.append(misseds[0])
    Adult.append(misseds[1])
    Adult.append(misseds[2])

    products = Product.objects.all()
    p.append(products[0])
    p.append(products[1])
    #p.append(products[2])'''
    return render(request, 'LostPeople/Section.html', { 'child': child , 'Adult':Adult , 'Products':p})


def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         username = request.POST['username']
         password1 = request.POST['password1']
         password2 = request.POST['password2']
         if username!='' and username[0].isdigit():
             return render(request, 'signup.html', {'form': form})

         form.username =username
         form.password1=password1
         form.password2=password2

         if form.is_valid():
             user = form.save(commit=False)
             #  log the user in
             username = form.cleaned_data['username']
             password = form.cleaned_data['password1']
             user.set_password(password)
             user.save()
             user = authenticate(username=username, password=password)
             login(request, user)
             return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', { 'form': form })


'''def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
               return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', { 'form': form })'''

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html',)

def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('home')

def api(request):
    base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(base_url)
    key = '17f9a54e963a4ff8806be407739f928c'  # Replace with a valid Subscription Key here.
    CF.Key.set(key)
    '''img_url = 'G:\coding\Django\GP2\pics/pic1.jpg'
    SearchedImg = CF.face.detect(img_url)'''
    img = request.FILES['IMG']
    SearchedImg = CF.face.detect(img)         # Detect faces in an image
    # Assume the first face is the one we want to compare
    if SearchedImg is not None:
        SearchIMG = SearchedImg[0]['faceId']
        print ("SearchedImg:" + SearchIMG)
        misseds = Missed.objects.all().order_by('date')
        #faces = {}
        ID = -1
        for temp in misseds :         # Detect faces in a comparison image
            face = CF.face.detect(temp.Img)
            if face is not None:
                DataIMG = face[0]['faceId']
                print("Data Img:" + DataIMG)
                similarity = CF.face.verify(SearchIMG,DataIMG)
                if similarity['isIdentical'] == True:
                    print('matching success ')
                    ID = temp.id
                    break
                #faces[face] = temp.id
        if ID!=-1:
            return redirect('LostPeople:detail', id=ID)
        else:
            print('not found')
            return redirect('home')

'''def SearchByImGAuto(request,IMG):
    base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(base_url)
    key = '5b650e36cdd241d484b84ed4560664bc'  # Replace with a valid Subscription Key here.
    CF.Key.set(key)

    img = IMG
    SearchedImg = CF.face.detect(img)

    # Assume the first face is the one we want to compare
    if SearchedImg is not None:
        SearchIMG = SearchedImg[0]['faceId']
        print ("SearchedImg:" + SearchIMG)

        misseds = Missed.objects.all().order_by('date')
        ID = -1
        for temp in misseds :
            face = CF.face.detect(temp.Img)
            if face is not None:
                DataIMG = face[0]['faceId']
                print("Data Img:" + DataIMG)
                similarity = CF.face.verify(SearchIMG,DataIMG)
                if similarity['isIdentical'] == True:
                    print('matching success ')
                    ID = temp.id
                    break
                #faces[face] = temp.id
        if ID!=-1:
            print('it is in data base')
            return redirect('LostPeople:detail', id=ID)
        else:
            print('not found')
            return False '''


@login_required(login_url="/login/")
def Make_comment(request,id3):
    comment = Comments()
    comment.idCard = id3
    comment.Auther = request.user
    comment.comment = request.POST['Comment']
    comment.save()
    return redirect('LostPeople:detail', id=id3)


def DeleteData(request,id4):
    card = Missed.objects.get(id=id4)
    age = card.age
    card.delete()
    if age <20:
        return redirect('LostPeople:child')
    else:
        return redirect('LostPeople:adult')

def DeleteWating(request,id4):
    card = Missed.objects.get(id=id4)
    card.delete()
    return redirect('LostPeople:wait')

