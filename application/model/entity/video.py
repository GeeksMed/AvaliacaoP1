"""
Cada vídeo que é apresentado nas telas é composto pela URL do vídeo, a URL da imagem de
apresentação, por um título, uma breve descrição, quantidade de visualizações, quantidade de
curtidas e a data de publicação. Cada vídeo também está vinculado a uma categoria, que é
composta por um título, uma descrição e a URL de uma imagem para ilustração.
"""

class Video():
    __url: str
    __imagem: str
    __titulo: str
    __descricao: str
    __qt_visualizacao: int
    __qt_curtidas: int
    __data_publicacao: str

    def __init__(self, url: str, imagem: str, titulo: str, descricao: str, qt_visualizacao: int, qt_curtidas: int, data_publicacao: str):
        self.__url = url
        self.__imagem = imagem
        self.__titulo = titulo
        self.__descricao = descricao
        self.__qt_visualizacao = qt_visualizacao
        self.__qt_curtidas = qt_curtidas
        self.__data_publicacao = data_publicacao

    def get_url(self):
        return self.__url
    
    def get_imagem(self):
        return self.__imagem
        
    def get_titulo(self):
        return self.__titulo

    def get_descricao(self):
        return self.__descricao

    def get_qt_visualizacao(self):
        return self.__qt_visualizacao

    def get_qt_curtidas(self):
        return self.__qt_curtidas

    def get_data_publicacao(self):
        return self.__data_publicacao
    
    def set_url(self, url: str):
        self.__url = url
    
    def set_imagem(self, imagem: str):
        self.__imagem = imagem
        
    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def set_descricao(self, descricao: str):
        self.__descricao = descricao 

    def set_qt_visualizacao(self, qt_visualizacao: str):
        self.__qt_visualizacao = qt_visualizacao

    def set_qt_curtidas(self, qt_curtidas: str):
        self.__qt_curtidas = qt_curtidas

    def set_data_publicacao(self, data_publicacao: str):
        self.__data_publicacao = data_publicacao