from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import Message
from chat.serializers import MessageSerializer, UserSerializer # Our Serializer Classes

#Users View
@csrf_exempt
def user_list(request, pk=None):
    """
    List all required message, or create a new message.
    """
    if request.method == 'GET':
        if pk:
            users = User.objects.filter(id=pk) #Select only that particular user
        else:
            users = Users.objects.all()      #Else get all user list
        serializer = UserSerializer(users, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(Serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

#Message View
@csrf_exempt

def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(Sender_id=sender, receiver_id=receiver)
        serializer = MessageSerializer(message, many=True, context={'request': request}
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data =JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# Create your views here.
