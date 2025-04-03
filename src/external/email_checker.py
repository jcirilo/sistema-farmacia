import re

class EmailCheckerAPI:
  # simula um serviço externo de validação de email

  def check_email(self, email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None
