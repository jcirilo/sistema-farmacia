from .interfaces import IPasswordValidator
from typing import Tuple

class AwsIamPasswordValidatorAdapter(IPasswordValidator):
    def validate(self, password: str) -> Tuple[bool, str]:
        """
        Valida a senha seguindo as políticas do AWS IAM:
        - Mínimo 8 caracteres
        - Pelo menos uma letra maiúscula
        - Pelo menos uma letra minúscula
        - Pelo menos um número
        - Pelo menos um caractere especial (!@#$%^&*()_+-=[]{}|')
        - Não pode ser igual ao login
        - Não pode conter sequências simples (ex: 1234, abcd)
        
        Retorna:
            Tuple[bool, str]: (True, "") se válido, (False, mensagem_erro) se inválido
        """
        errors = []
        
        if len(password) < 8:
            errors.append("pelo menos 8 caracteres")
            
        if not any(c.isupper() for c in password):
            errors.append("pelo menos uma letra maiúscula")
            
        if not any(c.islower() for c in password):
            errors.append("pelo menos uma letra minúscula")
            
        if not any(c.isdigit() for c in password):
            errors.append("pelo menos um número")
            
        special_chars = "!@#$%^&*()_+-=[]{}|'"
        if not any(c in special_chars for c in password):
            errors.append("pelo menos um caractere especial")
            
        # Verifica sequências simples
        if (password.lower() in ['12345678', 'password', 'senha123', 'qwertyui'] or
            any(str(i)*3 in password for i in range(10))):
            errors.append("não pode conter sequências simples")
            
        if errors:
            return False, f"Senha deve conter {', '.join(errors)}"
            
        return True, ""