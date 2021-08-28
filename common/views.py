from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from common.models import User
from common.serializers import UserSignUpWriteSerializer, UserForm


class UserSignUpAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSignUpWriteSerializer


@api_view(['GET'])
def get_signed_in_user_data(request):
    signed_in_user = request.user
    if signed_in_user:
        user_data = UserSignUpWriteSerializer(signed_in_user).data
        return JsonResponse({'response': user_data})
    return JsonResponse({'error': 'Tokeni juaj ka skaduar ju lutemi te hyni perseri'}, status=401)


@api_view(['POST'])
def update_user(request):
    signed_in_user = request.user
    data = request.data
    email = data.pop('email')
    password = data.pop('password')
    if signed_in_user and signed_in_user.check_password(password):
        formValidation = UserForm(data)
        if formValidation.is_valid() and email == signed_in_user.email:
            User.objects.filter(email=signed_in_user.email).update(**data)
            return JsonResponse({'response': 'Te dhena u perditesuan me sukses'}, status=200)
        return JsonResponse({'error': 'Te dhena jo te plota'}, status=403)

    return JsonResponse({'error': 'Tokeni juaj ka skaduar ju lutemi te hyni perseri'}, status=401)
