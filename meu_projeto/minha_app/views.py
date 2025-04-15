from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import google.generativeai as genai
import json

# Configura a API
genai.configure(api_key="AIzaSyDUwdv7b_DwFMUexNj2qxsg7Ag2ojoOvK4")

# Cria o modelo uma vez
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Views da aplicação
def home(request):
    return render(request, 'index.html')

def projetos(request):
    return render(request, 'projetos.html')

def integrantes(request):
    return render(request, 'integrantes.html')

def curso(request):
    return render(request, 'curso.html')

def fale_conosco(request):
    return render(request, 'fale_conosco.html')

def solicitacao_projetos(request):
    return render(request, 'solicitacao_projetos.html')


# View do chatbot
@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").strip()

            if not user_message:
                return JsonResponse({'reply': 'Mensagem vazia. Tente perguntar algo!'}, status=400)

            response = model.generate_content(user_message)

            # Verifica se retornou texto
            reply = getattr(response, "text", None)
            if not reply:
                return JsonResponse({'reply': 'Não consegui entender. Tente novamente!'}, status=200)

            return JsonResponse({'reply': reply})

        except Exception as e:
            print("Erro no Gemini:", e)
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método inválido.'}, status=405)
