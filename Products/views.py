from django.shortcuts import render, redirect
from .models import Product , BookMarks , Charity
from django.contrib.auth.decorators import login_required
#from . import forms
import xlrd

def ShowProducts(request):
    products = Product.objects.all();
    return render(request, '../templates/Products/ShowProducts.html', { 'products': products })

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, '../templates/Products/detiles.html', { 'product': product })

def product_create(request):
    if request.method == 'POST':
        product = Product()
        product.nameP = request.POST['ProductName']
        product.Img = request.FILES['IMG']
        product.Store_Name = request.POST['NameStore']
        product.Store_location = request.POST['location']
        product.price = request.POST['price']
        # save article to db
        product.save()
        return redirect('Products:listP')
    return render(request, '../templates/Products/CreatProduct.html', )

@login_required(login_url="/login/")
def BookMark(request,id2):
    print('id product', id2)
    #fav = request.GET.get('fav')
    bookmark = BookMarks()
    bookmark.idUser = request.user.id
    bookmark.idProduct =  id2
    bookmark.Fav = 'on'
    myfav = BookMarks.objects.filter(idUser=request.user.id,idProduct=id2)
    if len(myfav)==0:
        bookmark.save()
        return redirect('Products:Myfav')
    else:
        return redirect('Products:listP')


@login_required(login_url="/login/")
def MyBookmark(request):
    userID = request.user.id
    myBookmarks = BookMarks.objects.all().filter(idUser=userID)
    Products = []
    for temp in myBookmarks:
        product = Product.objects.get(id=temp.idProduct)
        Products.append(product)
    return render(request, '../templates/Products/MyBookmark.html', { 'myBookmarks': myBookmarks , 'Products': Products })


def DeleteProduct(request,id3):
    product = Product.objects.get(id=id3)
    product.delete()
    return redirect('Products:listP')

def DeleteCharity(request,id4):
    charity = Charity.objects.get(id=id4)
    charity.delete()
    return redirect('Products:listC')

def generateCharity(request):
    workbook = xlrd.open_workbook('Data.xlsx')
    worksheet = workbook.sheet_by_name('Sheet1')
    # Value of 1st row and 1st column
    # worksheet.cell(0, 0).value
    lenRow = worksheet.nrows
    for i in range(1,lenRow) :
        charity = Charity()
        print('name: ',worksheet.cell(i,0))
        charity.name = worksheet.cell(i,0).value
        print('address: ', worksheet.cell(i, 1))
        charity.address = worksheet.cell(i,1).value
        print('Phone_nubmer: ', worksheet.cell(i, 2))
        charity.Phone_nubmer = worksheet.cell(i,2).value
        # save article to db
        charity.save()
    return redirect('Products:listC')

def ShowCharity(request):
    charities = Charity.objects.all();
    return render(request, '../templates/Products/ShowCharity.html', { 'charities': charities })

def createCharity(request):
    if request.method == 'POST':
        charity = Charity()
        charity.name = request.POST['CharityName']
        charity.address = request.POST['address']
        charity.Phone_nubmer = request.POST['Phone_nubmer']
        # save article to db
        charity.save()
        return redirect('Products:listC')
    return render(request, '../templates/Products/CreatCharity.html', )
