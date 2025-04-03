from abc import ABC, abstractmethod
from business.control.item_control import ItemControl  

class ItemReportTemplate(ABC):
    def __init__(self):
        self.item_control = ItemControl() 

    # fluxo principal para gerar o relatório
    def generate_report(self) -> str:
        items_data = self.fetch_items_data()
        statistics = self.calculate_statistics(items_data)
        report_content = self.format_report(items_data, statistics)
        return report_content
    
    # obtém os dados dos itens
    def fetch_items_data(self) -> dict:
        return self.item_control.listAll()  
    
    # calcula estatísticas básicas dos itens
    def calculate_statistics(self, items_data: dict) -> dict:
        total_items = len(items_data)
        return {"total_items": total_items}
    
    # método abstrato para formatação do relatório
    @abstractmethod
    def format_report(self, items_data: dict, statistics: dict) -> str:
        pass
