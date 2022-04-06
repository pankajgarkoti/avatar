
import os
import base64
import string
import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .avatar import randomized_user_avatar

def log(exc):
    f = open('log.txt', 'a')
    f.write(str(exc))
    f.write('\n')
    f.close()
    return

@csrf_exempt
def index(request):
    ascii_letters = string.ascii_letters
    random_string = ''.join(random.choice(ascii_letters) for i in range(16))

    success, file = randomized_user_avatar(random_string)
    if success is True:
        with open(file, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        resp_dict = {
            'status': 'success',
            'message': 'avatar_generated_successfully',
            'image': image_data,
        }
    else:
        resp_dict = {
            'status': 'error',
            'message': 'error_in_avatar_generation',
        }
    os.remove(file)
    return JsonResponse(resp_dict)
