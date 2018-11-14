from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import sys

reg_text = "현재까지 등록된 키워드 [ 김수현, 전형진] "

def keyboard(request):

    return JsonResponse({
        #'type': 'buttons',
        #'buttons': ['전형진', '김수현']

        'message': {
            'text': reg_text
        }

    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    print(datacontent)

    if datacontent == '전형진':
        res_text = "개멋짐니다"

        return JsonResponse({
            'message': {
                'text': res_text
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['전형진', '김수현']
            }
        })

    elif datacontent == '김수현':
        res_text = "세젤예입니다."

        return JsonResponse({
            'message': {
                'text': res_text
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['전형진', '김수현']
            }
        })

    else :
        return JsonResponse({
            'message': {
                'text': reg_text
            }
        })


