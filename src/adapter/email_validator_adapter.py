from external.email_checker import EmailCheckerAPI

class EmailValidatorAdapter:
  def __init__(self):
    self.external_service = EmailCheckerAPI()

  def is_valid(self, email: str) -> bool:
    return self.external_service.check_email(email)
