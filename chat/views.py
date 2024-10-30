from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import openai
from django.shortcuts import render
from .models import ChatLog
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_view(request):
    ai_response = None  
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        if user_message:  
            ai_response = get_ai_response(user_message)
            ChatLog.objects.create(user_message=user_message, ai_response=ai_response)

    return render(request, 'chat/chat.html', {'ai_response': ai_response})

def get_ai_response(message):
    prompt = f"あなたは転職エージェントです。以下の自己PRを添削してください：\n\n{message}\n\n添削結果:"
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def log_view(request):
    logs = ChatLog.objects.all().order_by('timestamp')
    return render(request, 'chat/log.html', {'logs': logs})

def reset_log_view(request):
    ChatLog.objects.all().delete()
    return redirect('deletion_complete')

def deletion_complete_view(request):
    return render(request, 'chat/deletion_complete.html')