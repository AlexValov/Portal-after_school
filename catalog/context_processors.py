import datetime


def date(request):
    time = datetime.datetime.now()
    return {'time': time}
