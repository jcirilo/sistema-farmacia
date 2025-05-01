import re

class EmailCheckerAPI:
  # simula um serviço externo de validação de email

  def check_email(self, email: str) -> bool:
    pattern = r"^(?!.*\.\.)(?!.*\.$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.fullmatch(pattern, email) is not None
