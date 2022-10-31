from django.shortcuts import redirect, render

# Create your views here.


def send_to_main():
    return redirect(main)


def main(request):
    return render(request, 'main.html')
