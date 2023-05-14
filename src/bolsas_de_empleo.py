from src.computrabajo_handler import CompuTrabajoHandler

class BolsaDeEmpleo:
    def __init__(self) -> None:
        pass

class CompuTrabajo(BolsaDeEmpleo):
    def __init__(self) -> None:
        super().__init__()
        self.handler = CompuTrabajoHandler()