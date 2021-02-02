import django

def index(request):
    return django.Http.HttpResponse("index.html")


if __name__ == "__main__":
    main()


