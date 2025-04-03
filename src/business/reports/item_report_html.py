from .item_report_template import ItemReportTemplate

class ItemHTMLReport(ItemReportTemplate):
    def format_report(self, items_data: dict, statistics: dict) -> str:
        report = "<html><body>"
        report += "<h1>Relatório de Itens</h1>"
        report += f"<p>Total de Itens: {statistics['total_items']}</p>"
        report += "<table border='1'><tr><th>ID</th><th>Nome</th><th>Estoque</th></tr>"
        
        for item in items_data:
            report += f"<tr><td>{item.get_id()}</td><td>{item.get_name()}</td><td>{item.get_stock()}</td></tr>"
        
        report += "</table></body></html>"
        return report
