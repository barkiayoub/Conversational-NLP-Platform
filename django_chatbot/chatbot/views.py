# from django.shortcuts import render
# from django.http import JsonResponse
# import openai

#
# openai.api_key = openai_api_key

# def ask_openai(message):
#     response = openai.Completion.create(
#         model= "gpt-3.5-turbo",
#         prompt = message,
#         max_tokens=150,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
#     # print(response)
#     answer = response.choices[0].text.strip()
#     return


# # Create your views here.
# def chatbot(request):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         response = ask_openai(message)
#         return JsonResponse({'message': message,'response': response})
#     return render(request, 'chatbot.html')


from django.shortcuts import render
from django.http import JsonResponse
from transformers import AutoModelForCausalLM, AutoTokenizer
import os
from huggingface_hub import login

# Load the Mistral model and tokenizer from Hugging Face
# login("")

model_name = "mistralai/Mistral-7B-Instruct-v0.3"  # Replace with the correct model name on Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def ask_mistral(message):
    # Tokenize the input message
    inputs = tokenizer.encode(message, return_tensors="pt")

    # Generate a response
    outputs = model.generate(
        inputs,
        max_length=150,
        temperature=0.7,
        num_return_sequences=1,
        do_sample=True
    )

    # Decode and return the generated text
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_mistral(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')