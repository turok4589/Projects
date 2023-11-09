from .models import User
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
from ecommerce.models import Payment


# register serializers
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name','phone_no','email','password','gym_membership','fitness','country','state','city',
                                     'delivery_address','delivery_address_pincode']
        extra_kwargs = {
            'password' :{'write_only':True}  #  to does not return password in api ## postman
        }
    # convert password to hash key
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        if len(password) <6:
            raise serializers.ValidationError("entre strong password")
        instance.save()
        return instance
# login serializers
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()
    fitness = serializers.BooleanField(read_only=True)
    gym_membership = serializers.BooleanField(read_only=True)
    payment_status = serializers.BooleanField(read_only=True)

   
    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
        tokens_data = {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    # Include 'fitness' and 'gym_membership' only if they are True
        if user.fitness:
            tokens_data['fitness'] = user.fitness
        if user.gym_membership:
            tokens_data['gym_membership'] = user.gym_membership
        
        latest_payment = Payment.objects.filter(user=user).last()
        if latest_payment:
            tokens_data['payment_status'] = latest_payment.status
        else:
            tokens_data['payment_status'] = False

        return tokens_data

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens', 'fitness', 'gym_membership','payment_status']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

        return {
            'email': user.email,
            'tokens': user.tokens,
            #'payment_status': Payment.objects.filter(user=user).last().status if user else None,
         
        }

        return super().validate(attrs)


# class UserLoginSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(max_length=255, min_length=3)
#     password = serializers.CharField(max_length=68, min_length=6, write_only=True)
#     tokens = serializers.SerializerMethodField()

#     def get_tokens(self, obj):
#         user = User.objects.get(email=obj['email'])

#         return {
#             'refresh': user.tokens()['refresh'],
#             'access': user.tokens()['access']
#         }

#     class Meta:
#         model = User
#         fields = ['email', 'password', 'tokens']

#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         password = attrs.get('password', '')
#         filtered_user_by_email = User.objects.filter(email=email)
#         user = auth.authenticate(email=email, password=password)

#         if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
#             raise AuthenticationFailed(
#                 detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
#         if not user:
#             raise AuthenticationFailed('Invalid credentials, try again')
#         if not user.is_active:
#             raise AuthenticationFailed('Account disabled, contact admin')

#         return {
#             'email': user.email,
#             'tokens': user.tokens
#         }

#         return super().validate(attrs)




class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
