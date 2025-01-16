from django.shortcuts import render
from django.http import JsonResponse
from langchain import HuggingFaceHub

llm = HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.3",
                     model_kwargs={
                          "max_length": 1000,  # Maximum length of the generated sequence
                          "max_new_tokens": 10000,  # Maximum number of new tokens to generate
                     },
                     huggingfacehub_api_token="replace_with_your_api_key"
                    )

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = llm.invoke(message)
        print(response)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')