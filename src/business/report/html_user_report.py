from business.report.base_user_report import BaseUserReport
from business.model.customer import Customer
from typing import List

class HtmlUserReport(BaseUserReport):

    def _add_title(self):
        self.report += "<html><head><title>Relatório de Acesso</title></head><body>\n"
        self.report += "<h1>Estatísticas de Acesso dos Usuários</h1>\n"

    def _add_summary(self, customers: List[Customer], access_log: dict):
        self.report += f"<p>Total de usuários: {len(customers)}</p>\n"
        total_acessos = sum(access_log.get(cust.get_id(), 0) for cust in customers)
        self.report += f"<p>Total de acessos: {total_acessos}</p>\n"

    def _add_details(self, customers: List[Customer], access_log: dict):
        self.report += "<h2>Detalhes por Usuário</h2><ul>\n"
        for customer in customers:
            user_id = customer.get_id()
            acessos = access_log.get(user_id, 0)
            self.report += f"<li>{customer.get_name()} ({customer.get_email()}): {acessos} acessos</li>\n"
        self.report += "</ul>\n"

    def _finalize(self) -> str:
        self.report += "</body></html>"
        return self.report
