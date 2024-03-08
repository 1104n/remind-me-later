from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Reminder
import json



@require_POST
def create_reminder(request):
    try:
        data = json.loads(request.body)
        reminder = Reminder.objects.create(
            date=data['date'],
            time=data['time'],
            message=data['message'],
            reminder_mode=data['reminder_mode']
        )
        return JsonResponse({'status': 'success', 'id': reminder.id})
    except KeyError:
        return JsonResponse({'status': 'error', 'message': 'Invalid data provided'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
