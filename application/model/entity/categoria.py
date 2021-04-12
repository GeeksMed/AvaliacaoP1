"""
Uma categoria, que é composta por um título, uma descrição e a URL de uma imagem para ilustração.
"""

class Categoria():
    __titulo: str
    __descricao: str
    __imagem: str

    def __init__(self, titulo: str, descricao: str, imagem: str) -> Categoria:
        self.__titulo = titulo
        self.__descricao = descricao
        self.__imagem = imagem

    def get_titulo(self):
        return self.__titulo

    def get_descricao(self):
        return self.__descricao

    def get_imagem(self):
        return self.__imagem
     
    def set_titulo(self, titulo: str) -> None:
        self.__titulo = titulo

    def set_descricao(self, descricao: str) -> None:
        self.__descricao = descricao 

    def set_imagem(self, imagem: str) -> None:
        self.__imagem = imagem