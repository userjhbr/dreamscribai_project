from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'dreams/index.html')

def interpret_dream(request):
    if request.method == 'POST':
        data = {
            'dream_text': request.POST.get('dream_text', ''),
            'health_status': request.POST.get('health_status', ''),
            'relationships': {
                'relationship_status': request.POST.get('relationship_status', '')
            },
            'feelings': {
                'during_dream': request.POST.get('feelings_during', ''),
                'after_waking': request.POST.get('feelings_after', '')
            },
            'dream_context': request.POST.get('dream_context', ''),
            'dream_frequency': request.POST.get('dream_frequency', ''),
            'culture_and_beliefs': request.POST.get('culture_and_beliefs', ''),
            'psychological_state': {
                'state': request.POST.get('psychological_state', '')
            }
        }

        response = requests.post('http://localhost:5000/interpret_dream', json=data)
        result = response.json().get('result', 'Erro ao interpretar o sonho.')

        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
