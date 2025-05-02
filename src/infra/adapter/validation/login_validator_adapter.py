from .interfaces import ILoginValidator
from typing import Tuple

class LoginValidatorAdapter(ILoginValidator):
    def validate(self, login: str) -> Tuple[bool, str]:
        """
        Valida o login de acordo com as regras:
        - Máximo 12 caracteres
        - Não pode ser vazio
        - Não pode ter números
        
        Retorna:
            Tuple[bool, str]: (True, "") se válido, (False, mensagem_erro) se inválido
        """
        if not login:
            return False, "Login não pode ser vazio"
            
        if len(login) > 12:
            return False, "Login deve ter no máximo 12 caracteres"
            
        if any(c.isdigit() for c in login):
            return False, "Login não pode conter números"
            
        return True, ""