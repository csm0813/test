import django

def index(request):
    return django.Http.HttpResponse("index.html")


def login(request):
    return django.Http.HttpResponse("login.html")


if __name__ == "__main__":
    main()


