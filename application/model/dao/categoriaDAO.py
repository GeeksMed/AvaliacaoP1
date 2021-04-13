from application.model.entity.categoria import Categoria

class CategoriaDAO():

    def __init__(self, categoriaLista):
        self.__categoriaLista = categoriaLista

    def get_categoriaLista(self) -> list:
        return self.__categoriaLista
