"""
Uma categoria, que é composta por um título, uma descrição e a URL de uma imagem para ilustração.
"""

class Categoria():
    __id = int
    __titulo: str
    __descricao: str
    __imagem: str

    def __init__(self, id: int, titulo: str, descricao: str, imagem: str):
        self.__id = id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__imagem = imagem
        self.__video_lista = []
    
    def __init__(self, id: int, titulo: str, descricao: str, imagem: str, videos_lista: list):
        self.__id = id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__imagem = imagem
        self.__video_lista = videos_lista

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_descricao(self):
        return self.__descricao

    def get_imagem(self):
        return self.__imagem

    def get_videos_lista(self):
        return self.__video_lista
     
    def set_id(self, id: int):
        self.__id = id

    def set_titulo(self, titulo: str) -> None:
        self.__titulo = titulo

    def set_descricao(self, descricao: str) -> None:
        self.__descricao = descricao 

    def set_imagem(self, imagem: str) -> None:
        self.__imagem = imagem

    def set_videos_lista(self, videos_lista: list):
        self.__video_lista = video_lista