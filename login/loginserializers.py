from rest_framework import serializers
from .models import Login  # Assuming your model is in the same app

class LoginSerializer(serializers.ModelSerializer):
    encoded_pass = serializers.ReadOnlyField()
    yourname = serializers.SerializerMethodField('get_my_field')
    class Meta:
        model = Login
        fields = ('name', 'phonenumber', 'password', 'encoded_pass', 'yourname') 
    
    def get_my_field(self, obj):
        return 'hello yourname is ' + obj.name