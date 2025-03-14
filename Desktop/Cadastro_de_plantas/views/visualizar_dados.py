from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
)

from controller.dados_controller import DadosController


class VisualizarDados(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dados cadastrados")
        self.setGeometry(500, 100, 400, 300)
        layout = QVBoxLayout()

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels(
            ["ID", "Temperatura", "Luminosidade", "Umidade"]
        )

        layout.addWidget(self.tabela)

        botao_atualizar = QPushButton("Atualizar")
        botao_atualizar.clicked.connect(self.carregar_dados)

        layout.addWidget(botao_atualizar)
        self.setLayout(layout)

    def carregar_dados(self):
        self.controller = DadosController()
        dados = self.controller.mostrar_dados()
        self.tabela.setRowCount(len(dados))

        for row, dado in enumerate(dados):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(dado[0])))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(dado[1])))
            self.tabela.setItem(row, 2, QTableWidgetItem(str(dado[2])))
            self.tabela.setItem(row, 3, QTableWidgetItem(str(dado[3])))
