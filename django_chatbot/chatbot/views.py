from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'hi this is a response'
        return JsonResponse({'message': message,'response': response})
    return render(request, 'chatbot.html')
