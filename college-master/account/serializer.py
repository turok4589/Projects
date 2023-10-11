from .models import User
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth


# register serializers
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name','phone_no','email','password','gym_membership','health']
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
    health = serializers.BooleanField(read_only=True)
    gym_membership = serializers.BooleanField(read_only=True)

   
    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
        tokens_data = {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    # Include 'health' and 'gym_membership' only if they are True
        if user.health:
            tokens_data['health'] = user.health
        if user.gym_membership:
            tokens_data['gym_membership'] = user.gym_membership

        return tokens_data

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens', 'health', 'gym_membership']

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
            # 'health': user.health,
            # 'gym_membership': user.gym_membership
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
