from rest_framework import serializers
from .models import AbsUser

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsUser
        fields = ['first_name', 'last_name', 'password', 'email']
        
    def validate(self, data):
        """
        Validate the user data.

        Args:
            data (dict): Data to be validated.
        
        Raises:
            serializers.ValidationError: If any validation fails.
        
        Returns:
            dict: Validated data.
        """
        errors_list = []
        
        if 'email' in data:
            email = data['email']
            if AbsUser.objects.filter(email=email).exists():
                errors_list.append("Este e-mail já está em uso.")
        if 'password' in data:
            password = data['password']
            if len(password) < 8:
                errors_list.append("A senha deve ter pelo menos 8 caracteres.")
            if not any(char.isdigit() for char in password):
                errors_list.append("A senha deve conter pelo menos um número.")
            if not any(char.isupper() for char in password):
                errors_list.append("A senha deve conter pelo menos uma letra maiúscula.")
        if 'first_name' in data and 'last_name' in data:
            first_name = data['first_name']
            last_name = data['last_name']
            if len(first_name.strip()) > 50 or len(first_name.strip()) < 3:
                errors_list.append("O nome não pode estar vazio.")
            if len(last_name.strip()) > 50 or len(last_name.strip()) < 3:
                errors_list.append("O sobrenome não pode estar vazio.")
        
        if errors_list:
            raise serializers.ValidationError(errors_list)
        
        return data
    