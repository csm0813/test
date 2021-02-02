import django

def index(request):
    return django.Http.HttpResponse("index.html")


def login(request):
    return django.Http.HttpResponse("login.html")

def register(request):
    return django.Http.HttpResponse("res.html")


if __name__ == "__main__":
    main()


