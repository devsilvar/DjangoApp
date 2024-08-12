from django.shortcuts import render
from crudapp import forms
from crudapp.models import UserData

# Create your views here.
def indexPage(req):
    context = "yusuf aiyegbajeje"
    return render(req , 'crudapp/index.html' , {'name': context})

def userListPage(req):
    userLists = UserData.objects.order_by('name')
    user_records = {'records': userLists}
    return render(req , 'crudapp/userList.html' , context=user_records)

def addUser(req):
    form = forms.crudForm()

    if req.method == "POST":
        form = forms.crudForm(req.POST)
        print('submmited')


        if form.is_valid():
            print('submission successful')
            name = req.POST.get('name')
            email = req.POST.get('email')
            phone_number = req.POST.get('phone_number')
            password = req.POST.get('password')

            new_instace = UserData(name=name,email=email,phone_number=phone_number,password=password)
            new_instace.save()
            return indexPage(req)
        else:
            print(NameError)
        

        return render(req , 'crudapp/index.html' , {'message':'model sucesfully saved'})


# def addUser(req):
#     form = forms.crudForm()

#     if req.method == "POST":
#         form = forms.crudForm(req.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             return indexPage(req)
#         else:
#             print('invalid Form')


#         return render(req , 'crudapp/index.html' , {'message':'model sucesfully saved'})

    


    return render(req , 'crudapp/adduser.html' , {'form': form} )



