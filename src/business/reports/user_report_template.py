from abc import ABC, abstractmethod
from business.control.user_control import UserControl

class UserReportTemplate(ABC):
  # template method para geração de relatórios de usuários
  def __init__(self):
    self.user_control = UserControl()

  # define o fluxo da geração do relatório
  def generate_report(self) -> str:
    users_data = self.fetch_users_data()
    statistics = self.calculate_statistics(users_data)
    report_content = self.format_report(users_data, statistics)
    return report_content

  # obtém os dados dos usuários
  def fetch_users_data(self) -> dict:
    return self.user_control.listAll()

  # calcula estatísticas básicas
  def calculate_statistics(self, users_data: dict) -> dict:
    total_users = len(users_data)
    return {"total_users": total_users}

  # @abstractmethod
  # método abstrato que deve ser implementado pelas subclasses
  # def format_report(self, users_data: dict, statistics: dict) -> str:
  #  pass
