from django.shortcuts import render


def indexone(request):
    return render(request,"home.html")

def logins(request):
    return render(request,"logins.html")
def data(request):
    return render(request,"data.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        Name= fname+" "+lname
        dataone = {"username" :username, "Name":Name }
    return render(request,"signup.html")
