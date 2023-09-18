from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationSerializer,MenuSerializer,ResturantsLikeSerializer,SaveMenuSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from .models import Resturants,Menu
from rest_framework import viewsets
from .serializers import RestuarantsSerializer
from .mypermission import IsAdminUser
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Menu,User,SaveMenu


class menuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    @action(detail=True, methods=['POST'])
    def increment_likes(self, request, pk=None):
        menu = self.get_object()
        menu.likes += 1
        menu.save()
        serializer = self.get_serializer(menu)
        return Response(serializer.data)
    

class resturantView(viewsets.ModelViewSet):
    queryset = Resturants.objects.all()
    serializer_class = ResturantsLikeSerializer
    @action(detail=True, methods=['POST'])
    def increment_likes(self, request, pk=None):
        restaurant = self.get_object()
        restaurant.likes += 1
        restaurant.save()
        serializer = self.get_serializer(restaurant)
        return Response(serializer.data)

 
class MenuView(viewsets.ModelViewSet):
    serializer_class= MenuSerializer
    queryset=Menu.objects.all()
    
     

class addRestuarantsView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes = [IsAdminUser]
    def post(self,request):
        print(request.user,'useruseruseruser')
        seri = RestuarantsSerializer( data=request.data)
        if seri.is_valid():
            seri.save()
            return Response({'msg':'added1111'})
        return Response(seri.errors)

    
# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

class SendPasswordResetEmailView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
  
class RestuarantsApiView(APIView):
    permission_classes=[IsAuthenticated]
    renderer_classes=[UserRenderer]
    def get(self, request, pk=None):
        print(request.user,'llpllpplpl')
        if pk is not None:
          restu = Resturants.objects.get(id=pk)
          seri = RestuarantsSerializer(restu)
          return Response(seri.data)
        restu = Resturants.objects.all()
        seri = RestuarantsSerializer(restu, many=True, context={'request': request})
        return Response(seri.data)

    def put(self, request,pk=None):
        restu = Resturants.objects.get(id=pk)
        seri = RestuarantsSerializer(restu,data=request.data)
        if seri.is_valid(raise_exception=True):
            seri.save()
            return Response({'msg':'restuarants Completely Updated!!'})
        return Response(seri.errors)
      
      
    def patch(self,request,pk=None):
        restu = Resturants.objects.get(id=pk)
        seri = RestuarantsSerializer(restu,data=request.data,partial=True)
        if seri.is_valid(raise_exception=True):
            seri.save()
            return Response({'msg':'restuarants Partially Updated!!'})
        return Response(seri.errors)
    
    def delete(self,request,pk=None):
        restu = Resturants.objects.get(id=pk)
        restu.delete()
        return Response({'msg':'Deleted!!!'})
    

class SaveMenuView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    
    def post(self, request,format=None):
        seri = SaveMenuSerializer(request.user, data=request.data)
        if seri.is_valid(raise_exception=True):
            resturant_name = Resturants.objects.get(resturant_name=seri.validated_data.get('resturant_name'))
            menu_name = Menu.objects.get(menu_name=seri.validated_data.get('menu_name'))
            user_id = User.objects.get(email=request.user.email)
            savemenu= SaveMenu.objects.create(
                user_id=user_id
            )
            savemenu.menu_name.set([menu_name])
            savemenu.resturant_name.set([resturant_name])
            savemenu.save()
            return Response({'message': 'Menu is saved in associated Restaurants' })
        return Response(seri.errors )
    
     