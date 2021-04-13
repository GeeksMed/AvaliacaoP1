from application import app
from flask import Flask, render_template, request, url_for
from application.model.dao.categoriaDAO import CategoriaDAO
from application.model.entity.categoria import Categoria
from application.model.entity.video import Video

videolista = []
videolista.append(Video("/videos/fast1.mp4", "/img/heart.svg", "Fast&Furious 1", "Velocidade e Habilidade", 0, 0, "20/01/2010"))
videolista.append(Video("/videos/fast2.mp4", "/img/heart.svg", "Fast&Furious 2", "Velocidade e Habilidade", 0, 0, "20/01/2012"))
videolista.append(Video("/videos/anime.mp4", "/img/share.svg", "Animes", "Só os melhores", 0, 0, "20/01/2019"))
videolista.append(Video("/videos/deep.mp4", "/img/share.svg", "Deep", "Jonny Deep", 0, 0, "20/01/2017"))

categorialista = []
categorialista.append(Categoria(1, "Ação", "Filmes que te fazem acreditar em velocidade.", "/img/heart.svg", videolista[0:2]))
categorialista.append(Categoria(2, "Anime/Fantasia", "Melhor da vida", "/img/share.svg", videolista[2:4]))
categoriaDAO = CategoriaDAO(categorialista)

@app.route('/')
def index():
    return render_template("index.html", categoria_list = categoriaDAO.get_categoriaLista())

@app.route('/<titulo>')
def video(titulo):
    for video in videolista:
        if video.get_titulo() == titulo:
            return render_template("video.html", video = video)
    return render_template("index.html", categoria_list = categorialista)
