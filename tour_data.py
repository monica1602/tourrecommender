"""
Base de dados de passeios turísticos para recomendação.
"""

TOURS = [
    # === BRASIL ===
    {
        "id": 1,
        "nome": "Cristo Redentor",
        "pais": "Brasil",
        "cidade": "Rio de Janeiro",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 80.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Visita ao icônico Cristo Redentor no topo do Corcovado com vista panorâmica da cidade.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=400"
    },
    {
        "id": 2,
        "nome": "Trilha na Floresta da Tijuca",
        "pais": "Brasil",
        "cidade": "Rio de Janeiro",
        "tipo": "Natureza",
        "duracao_horas": 5,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 10,
        "descricao": "Trilha ecológica pela maior floresta urbana do mundo com cachoeiras.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1516306580123-e6e52b1b7b5f?w=400"
    },
    {
        "id": 3,
        "nome": "Passeio de Barco pela Baía de Guanabara",
        "pais": "Brasil",
        "cidade": "Rio de Janeiro",
        "tipo": "Aventura",
        "duracao_horas": 4,
        "preco": 150.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Navegue pela Baía de Guanabara com vistas do Pão de Açúcar e pontos históricos.",
        "avaliacao": 4.5,
        "imagem": "https://images.unsplash.com/photo-1544989164-31dc3c645987?w=400"
    },
    {
        "id": 4,
        "nome": "Tour Gastronômico em São Paulo",
        "pais": "Brasil",
        "cidade": "São Paulo",
        "tipo": "Gastronomia",
        "duracao_horas": 4,
        "preco": 200.0,
        "gratuito": False,
        "max_pessoas": 12,
        "descricao": "Explore os melhores restaurantes e bares da Vila Madalena e Pinheiros.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400"
    },
    {
        "id": 5,
        "nome": "Museu de Arte de São Paulo (MASP)",
        "pais": "Brasil",
        "cidade": "São Paulo",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 50.0,
        "gratuito": False,
        "max_pessoas": 50,
        "descricao": "Visite o acervo de arte europeia e brasileira no icônico prédio da Avenida Paulista.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1554907984-15263bfd63bd?w=400"
    },
    {
        "id": 6,
        "nome": "Parque Ibirapuera",
        "pais": "Brasil",
        "cidade": "São Paulo",
        "tipo": "Natureza",
        "duracao_horas": 3,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 100,
        "descricao": "Passeio pelo maior parque urbano de São Paulo com lagos, museus e áreas verdes.",
        "avaliacao": 4.5,
        "imagem": "https://images.unsplash.com/photo-1578353022142-09264fd64295?w=400"
    },
    {
        "id": 7,
        "nome": "Cataratas do Iguaçu",
        "pais": "Brasil",
        "cidade": "Foz do Iguaçu",
        "tipo": "Natureza",
        "duracao_horas": 6,
        "preco": 90.0,
        "gratuito": False,
        "max_pessoas": 40,
        "descricao": "Contemple uma das 7 maravilhas naturais do mundo com passarelas sobre as quedas d'água.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1543385426-191664295b58?w=400"
    },
    {
        "id": 8,
        "nome": "Pelourinho - Centro Histórico",
        "pais": "Brasil",
        "cidade": "Salvador",
        "tipo": "Cultural",
        "duracao_horas": 4,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 20,
        "descricao": "Caminhe pelas ruas coloridas do centro histórico de Salvador, Patrimônio da UNESCO.",
        "avaliacao": 4.4,
        "imagem": "https://images.unsplash.com/photo-1551279880-03af85c387e8?w=400"
    },
    # === PORTUGAL ===
    {
        "id": 9,
        "nome": "Torre de Belém",
        "pais": "Portugal",
        "cidade": "Lisboa",
        "tipo": "Cultural",
        "duracao_horas": 2,
        "preco": 10.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Visite a torre fortificada do século XVI, símbolo dos Descobrimentos Portugueses.",
        "avaliacao": 4.5,
        "imagem": "https://images.unsplash.com/photo-1555881400-74d7acaacd8b?w=400"
    },
    {
        "id": 10,
        "nome": "Passeio de Elétrico 28",
        "pais": "Portugal",
        "cidade": "Lisboa",
        "tipo": "Cultural",
        "duracao_horas": 2,
        "preco": 5.0,
        "gratuito": False,
        "max_pessoas": 40,
        "descricao": "Percorra os bairros históricos de Lisboa no famoso elétrico amarelo.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=400"
    },
    {
        "id": 11,
        "nome": "Caves do Vinho do Porto",
        "pais": "Portugal",
        "cidade": "Porto",
        "tipo": "Gastronomia",
        "duracao_horas": 3,
        "preco": 25.0,
        "gratuito": False,
        "max_pessoas": 15,
        "descricao": "Degustação de vinhos nas caves históricas de Vila Nova de Gaia.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=400"
    },
    {
        "id": 12,
        "nome": "Caminhada na Ribeira",
        "pais": "Portugal",
        "cidade": "Porto",
        "tipo": "Natureza",
        "duracao_horas": 2,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 50,
        "descricao": "Passeio à beira do Rio Douro com vista para as pontes e casas coloridas.",
        "avaliacao": 4.5,
        "imagem": "https://images.unsplash.com/photo-1555881400-74d7acaacd8b?w=400"
    },
    # === ITÁLIA ===
    {
        "id": 13,
        "nome": "Coliseu de Roma",
        "pais": "Itália",
        "cidade": "Roma",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 18.0,
        "gratuito": False,
        "max_pessoas": 25,
        "descricao": "Explore o anfiteatro mais famoso do mundo com guia especializado em história romana.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=400"
    },
    {
        "id": 14,
        "nome": "Tour de Gôndola em Veneza",
        "pais": "Itália",
        "cidade": "Veneza",
        "tipo": "Romântico",
        "duracao_horas": 1,
        "preco": 80.0,
        "gratuito": False,
        "max_pessoas": 6,
        "descricao": "Passeio romântico pelos canais de Veneza em gôndola tradicional.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1514890547357-a9ee288728e0?w=400"
    },
    {
        "id": 15,
        "nome": "Degustação de Vinhos na Toscana",
        "pais": "Itália",
        "cidade": "Florença",
        "tipo": "Gastronomia",
        "duracao_horas": 6,
        "preco": 120.0,
        "gratuito": False,
        "max_pessoas": 10,
        "descricao": "Visite vinícolas da região do Chianti com degustação de vinhos e almoço típico.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?w=400"
    },
    # === FRANÇA ===
    {
        "id": 16,
        "nome": "Torre Eiffel",
        "pais": "França",
        "cidade": "Paris",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 26.0,
        "gratuito": False,
        "max_pessoas": 50,
        "descricao": "Suba ao topo da Torre Eiffel e aprecie a vista panorâmica de Paris.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1511739001486-6bfe10ce65f4?w=400"
    },
    {
        "id": 17,
        "nome": "Museu do Louvre",
        "pais": "França",
        "cidade": "Paris",
        "tipo": "Cultural",
        "duracao_horas": 4,
        "preco": 17.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Explore o maior museu de arte do mundo com obras como a Mona Lisa.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=400"
    },
    {
        "id": 18,
        "nome": "Jardins de Versalhes",
        "pais": "França",
        "cidade": "Paris",
        "tipo": "Natureza",
        "duracao_horas": 5,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 100,
        "descricao": "Passeie pelos magníficos jardins do Palácio de Versalhes com fontes e esculturas.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1564399580075-5dfe19c205f0?w=400"
    },
    # === JAPÃO ===
    {
        "id": 19,
        "nome": "Templo Fushimi Inari",
        "pais": "Japão",
        "cidade": "Kyoto",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 50,
        "descricao": "Caminhe pelos milhares de portões torii vermelhos neste santuário milenar.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1478436127897-769e1b3f0f36?w=400"
    },
    {
        "id": 20,
        "nome": "Cruzeiro pelo Rio Sumida",
        "pais": "Japão",
        "cidade": "Tóquio",
        "tipo": "Aventura",
        "duracao_horas": 2,
        "preco": 30.0,
        "gratuito": False,
        "max_pessoas": 40,
        "descricao": "Navegue pelo rio Sumida com vistas da Tokyo Skytree e pontes históricas.",
        "avaliacao": 4.4,
        "imagem": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=400"
    },
    {
        "id": 21,
        "nome": "Aula de Sushi Tradicional",
        "pais": "Japão",
        "cidade": "Tóquio",
        "tipo": "Gastronomia",
        "duracao_horas": 3,
        "preco": 75.0,
        "gratuito": False,
        "max_pessoas": 8,
        "descricao": "Aprenda a preparar sushi autêntico com um mestre sushiman em Tsukiji.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=400"
    },
    # === ESTADOS UNIDOS ===
    {
        "id": 22,
        "nome": "Central Park",
        "pais": "Estados Unidos",
        "cidade": "Nova York",
        "tipo": "Natureza",
        "duracao_horas": 3,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 100,
        "descricao": "Explore o famoso parque urbano de Manhattan com lagos, pontes e jardins.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1534430480872-3498386e7856?w=400"
    },
    {
        "id": 23,
        "nome": "Estátua da Liberdade",
        "pais": "Estados Unidos",
        "cidade": "Nova York",
        "tipo": "Cultural",
        "duracao_horas": 4,
        "preco": 24.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Ferry até a Ilha da Liberdade com acesso ao pedestal e museu.",
        "avaliacao": 4.5,
        "imagem": "https://images.unsplash.com/photo-1503174971373-b1f69850bded?w=400"
    },
    {
        "id": 24,
        "nome": "Grand Canyon - Trilha South Rim",
        "pais": "Estados Unidos",
        "cidade": "Arizona",
        "tipo": "Aventura",
        "duracao_horas": 8,
        "preco": 35.0,
        "gratuito": False,
        "max_pessoas": 15,
        "descricao": "Trilha épica pela borda sul do Grand Canyon com vistas de tirar o fôlego.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1474044159687-1ee9f3a51722?w=400"
    },
    # === ARGENTINA ===
    {
        "id": 25,
        "nome": "Tango em San Telmo",
        "pais": "Argentina",
        "cidade": "Buenos Aires",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 60.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Show de tango autêntico com jantar em uma milonga tradicional de San Telmo.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=400"
    },
    {
        "id": 26,
        "nome": "Glaciar Perito Moreno",
        "pais": "Argentina",
        "cidade": "El Calafate",
        "tipo": "Natureza",
        "duracao_horas": 8,
        "preco": 100.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Contemple o impressionante glaciar com passarelas e mini-trekking opcional.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=400"
    },
    # === ESPANHA ===
    {
        "id": 27,
        "nome": "Sagrada Família",
        "pais": "Espanha",
        "cidade": "Barcelona",
        "tipo": "Cultural",
        "duracao_horas": 2,
        "preco": 26.0,
        "gratuito": False,
        "max_pessoas": 25,
        "descricao": "Visite a obra-prima inacabada de Gaudí, Patrimônio da UNESCO.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1583422409516-2895a77efded?w=400"
    },
    {
        "id": 28,
        "nome": "Caminhada pelo Parque Güell",
        "pais": "Espanha",
        "cidade": "Barcelona",
        "tipo": "Natureza",
        "duracao_horas": 2,
        "preco": 10.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Explore o parque artístico de Gaudí com mosaicos coloridos e vista da cidade.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1564221710304-0b37c8b9d729?w=400"
    },
    # === MÉXICO ===
    {
        "id": 29,
        "nome": "Ruínas de Chichén Itzá",
        "pais": "México",
        "cidade": "Cancún",
        "tipo": "Cultural",
        "duracao_horas": 8,
        "preco": 50.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Visite a pirâmide maia de Kukulcán, uma das Novas Sete Maravilhas do Mundo.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1518638150340-f706e86654de?w=400"
    },
    {
        "id": 30,
        "nome": "Mergulho em Cenotes",
        "pais": "México",
        "cidade": "Cancún",
        "tipo": "Aventura",
        "duracao_horas": 4,
        "preco": 70.0,
        "gratuito": False,
        "max_pessoas": 8,
        "descricao": "Mergulhe nas águas cristalinas dos cenotes sagrados maias.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1504019347908-b45f9b0b8dd5?w=400"
    },
    # === GRÉCIA ===
    {
        "id": 31,
        "nome": "Acrópole de Atenas",
        "pais": "Grécia",
        "cidade": "Atenas",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 20.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Explore o Parthenon e os templos antigos no topo da colina sagrada de Atenas.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1555993539-1732b0258235?w=400"
    },
    {
        "id": 32,
        "nome": "Pôr do Sol em Santorini",
        "pais": "Grécia",
        "cidade": "Santorini",
        "tipo": "Romântico",
        "duracao_horas": 3,
        "preco": 45.0,
        "gratuito": False,
        "max_pessoas": 12,
        "descricao": "Cruzeiro ao pôr do sol com vinho e vista das casas brancas de Oia.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400"
    },
    # === TAILÂNDIA ===
    {
        "id": 33,
        "nome": "Templos de Bangkok",
        "pais": "Tailândia",
        "cidade": "Bangkok",
        "tipo": "Cultural",
        "duracao_horas": 5,
        "preco": 15.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Tour pelos templos dourados Wat Pho, Wat Arun e Grand Palace.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1528181304800-259b08848526?w=400"
    },
    {
        "id": 34,
        "nome": "Mercado Flutuante",
        "pais": "Tailândia",
        "cidade": "Bangkok",
        "tipo": "Gastronomia",
        "duracao_horas": 4,
        "preco": 25.0,
        "gratuito": False,
        "max_pessoas": 10,
        "descricao": "Navegue pelos mercados flutuantes provando comida de rua tailandesa.",
        "avaliacao": 4.5,
        "imagem": "https://images.unsplash.com/photo-1506665531195-3566af2b4dfa?w=400"
    },
    {
        "id": 35,
        "nome": "Ilhas Phi Phi de Lancha",
        "pais": "Tailândia",
        "cidade": "Phuket",
        "tipo": "Aventura",
        "duracao_horas": 8,
        "preco": 85.0,
        "gratuito": False,
        "max_pessoas": 15,
        "descricao": "Passeio de lancha por praias paradisíacas com snorkeling em águas cristalinas.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1504214208698-ea1916a2195a?w=400"
    },
    {
        "id": 36,
        "nome": "Praia de Railay - Escalada",
        "pais": "Tailândia",
        "cidade": "Krabi",
        "tipo": "Aventura",
        "duracao_horas": 6,
        "preco": 55.0,
        "gratuito": False,
        "max_pessoas": 8,
        "descricao": "Escalada em falésias calcárias com vista para praias paradisíacas.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?w=400"
    },
    # === EGITO ===
    {
        "id": 37,
        "nome": "Pirâmides de Gizé",
        "pais": "Egito",
        "cidade": "Cairo",
        "tipo": "Cultural",
        "duracao_horas": 5,
        "preco": 40.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Visite as Grandes Pirâmides e a Esfinge com guia egiptólogo.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?w=400"
    },
    {
        "id": 38,
        "nome": "Cruzeiro pelo Rio Nilo",
        "pais": "Egito",
        "cidade": "Luxor",
        "tipo": "Aventura",
        "duracao_horas": 6,
        "preco": 95.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Navegue pelo Nilo visitando templos faraônicos ao longo do caminho.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1568322445389-f64b0f61f457?w=400"
    },
    # === TURQUIA ===
    {
        "id": 39,
        "nome": "Voo de Balão na Capadócia",
        "pais": "Turquia",
        "cidade": "Capadócia",
        "tipo": "Aventura",
        "duracao_horas": 2,
        "preco": 180.0,
        "gratuito": False,
        "max_pessoas": 16,
        "descricao": "Sobrevoe as formações rochosas ao nascer do sol em balão de ar quente.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1526048598645-62b31f82b8f5?w=400"
    },
    {
        "id": 40,
        "nome": "Hagia Sophia e Mesquita Azul",
        "pais": "Turquia",
        "cidade": "Istambul",
        "tipo": "Cultural",
        "duracao_horas": 4,
        "preco": 30.0,
        "gratuito": False,
        "max_pessoas": 25,
        "descricao": "Tour pelos monumentos mais icônicos de Istambul com guia histórico.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1541432901042-2d8bd64b4a9b?w=400"
    },
    {
        "id": 41,
        "nome": "Grand Bazaar - Tour Gastronômico",
        "pais": "Turquia",
        "cidade": "Istambul",
        "tipo": "Gastronomia",
        "duracao_horas": 3,
        "preco": 45.0,
        "gratuito": False,
        "max_pessoas": 10,
        "descricao": "Prove especiarias, doces turcos e kebabs no maior mercado coberto do mundo.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?w=400"
    },
    # === AUSTRÁLIA ===
    {
        "id": 42,
        "nome": "Grande Barreira de Coral",
        "pais": "Austrália",
        "cidade": "Cairns",
        "tipo": "Aventura",
        "duracao_horas": 8,
        "preco": 200.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Mergulho e snorkeling no maior recife de coral do mundo.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1546026423-cc4642628d2b?w=400"
    },
    {
        "id": 43,
        "nome": "Ópera de Sydney - Tour Guiado",
        "pais": "Austrália",
        "cidade": "Sydney",
        "tipo": "Cultural",
        "duracao_horas": 2,
        "preco": 35.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Tour pelos bastidores do icônico Sydney Opera House.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1524293581917-878a6d017c71?w=400"
    },
    {
        "id": 44,
        "nome": "Blue Mountains",
        "pais": "Austrália",
        "cidade": "Sydney",
        "tipo": "Natureza",
        "duracao_horas": 8,
        "preco": 90.0,
        "gratuito": False,
        "max_pessoas": 15,
        "descricao": "Trilhas por florestas de eucalipto com vistas das Three Sisters.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=400"
    },
    # === PERU ===
    {
        "id": 45,
        "nome": "Machu Picchu",
        "pais": "Peru",
        "cidade": "Cusco",
        "tipo": "Cultural",
        "duracao_horas": 10,
        "preco": 70.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Visite a cidade perdida dos Incas, Patrimônio da Humanidade.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1526392060635-9d6019884377?w=400"
    },
    {
        "id": 46,
        "nome": "Vale Sagrado dos Incas",
        "pais": "Peru",
        "cidade": "Cusco",
        "tipo": "Natureza",
        "duracao_horas": 8,
        "preco": 45.0,
        "gratuito": False,
        "max_pessoas": 15,
        "descricao": "Explore ruínas, mercados indígenas e paisagens andinas espetaculares.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1580619305218-8423a7ef79b4?w=400"
    },
    {
        "id": 47,
        "nome": "Tour Gastronômico em Lima",
        "pais": "Peru",
        "cidade": "Lima",
        "tipo": "Gastronomia",
        "duracao_horas": 4,
        "preco": 80.0,
        "gratuito": False,
        "max_pessoas": 10,
        "descricao": "Prove ceviches e pratos peruanos nos melhores restaurantes de Miraflores.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1535399831218-d5bd36d1a6b3?w=400"
    },
    # === MARROCOS ===
    {
        "id": 48,
        "nome": "Medina de Marrakech",
        "pais": "Marrocos",
        "cidade": "Marrakech",
        "tipo": "Cultural",
        "duracao_horas": 4,
        "preco": 20.0,
        "gratuito": False,
        "max_pessoas": 12,
        "descricao": "Explore os souks, palácios e a praça Jemaa el-Fna com guia local.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1539020140153-e479b8c22e70?w=400"
    },
    {
        "id": 49,
        "nome": "Deserto do Saara - Noite em Acampamento",
        "pais": "Marrocos",
        "cidade": "Merzouga",
        "tipo": "Aventura",
        "duracao_horas": 24,
        "preco": 150.0,
        "gratuito": False,
        "max_pessoas": 10,
        "descricao": "Passeio de camelo pelas dunas com pernoite em tenda berber sob as estrelas.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1489749798305-4fea3ae63d43?w=400"
    },
    # === COLÔMBIA ===
    {
        "id": 50,
        "nome": "Cidade Murada de Cartagena",
        "pais": "Colômbia",
        "cidade": "Cartagena",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 30,
        "descricao": "Caminhe pelas ruas coloridas e históricas da cidade murada colonial.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1583997052103-b4a1cb974ce5?w=400"
    },
    {
        "id": 51,
        "nome": "Islas del Rosario - Snorkeling",
        "pais": "Colômbia",
        "cidade": "Cartagena",
        "tipo": "Aventura",
        "duracao_horas": 7,
        "preco": 60.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Passeio de barco a ilhas caribenhas com snorkeling e almoço na praia.",
        "avaliacao": 4.5,
        "imagem": "https://images.unsplash.com/photo-1534862786-46fd0e855d88?w=400"
    },
    # === ALEMANHA ===
    {
        "id": 52,
        "nome": "Castelo de Neuschwanstein",
        "pais": "Alemanha",
        "cidade": "Munique",
        "tipo": "Cultural",
        "duracao_horas": 6,
        "preco": 55.0,
        "gratuito": False,
        "max_pessoas": 25,
        "descricao": "Visite o castelo que inspirou a Disney em meio aos Alpes bávaros.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1534313314376-a72289b6181e?w=400"
    },
    {
        "id": 53,
        "nome": "Tour de Cervejarias",
        "pais": "Alemanha",
        "cidade": "Munique",
        "tipo": "Gastronomia",
        "duracao_horas": 4,
        "preco": 50.0,
        "gratuito": False,
        "max_pessoas": 15,
        "descricao": "Degustação em cervejarias tradicionais bávaras com pretzels e salsichas.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1558642452-9d2a7deb7f62?w=400"
    },
    {
        "id": 54,
        "nome": "Muro de Berlim - Tour Histórico",
        "pais": "Alemanha",
        "cidade": "Berlim",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 30,
        "descricao": "Passeio pela East Side Gallery e Checkpoint Charlie com história da Guerra Fria.",
        "avaliacao": 4.5,
        "imagem": "https://images.unsplash.com/photo-1560969184-10fe8719e047?w=400"
    },
    # === CHILE ===
    {
        "id": 55,
        "nome": "Deserto do Atacama - Gêisers del Tatio",
        "pais": "Chile",
        "cidade": "San Pedro de Atacama",
        "tipo": "Natureza",
        "duracao_horas": 6,
        "preco": 60.0,
        "gratuito": False,
        "max_pessoas": 15,
        "descricao": "Gêisers ao amanhecer a 4.300m de altitude com banho em piscinas termais.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1509861012372-628426e01cfe?w=400"
    },
    {
        "id": 56,
        "nome": "Valle de la Luna",
        "pais": "Chile",
        "cidade": "San Pedro de Atacama",
        "tipo": "Natureza",
        "duracao_horas": 4,
        "preco": 30.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Paisagens lunares com formações de sal e pôr do sol espetacular.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1526392060635-9d6019884377?w=400"
    },
    # === NOVA ZELÂNDIA ===
    {
        "id": 57,
        "nome": "Hobbiton - Terra Média",
        "pais": "Nova Zelândia",
        "cidade": "Matamata",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 75.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Visite o set de filmagem de O Senhor dos Anéis com tocas hobbit reais.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1507699622108-4be3abd695ad?w=400"
    },
    {
        "id": 58,
        "nome": "Bungee Jump em Queenstown",
        "pais": "Nova Zelândia",
        "cidade": "Queenstown",
        "tipo": "Aventura",
        "duracao_horas": 2,
        "preco": 160.0,
        "gratuito": False,
        "max_pessoas": 4,
        "descricao": "Salto de bungee na capital mundial da aventura com vista para os Alpes.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=400"
    },
    {
        "id": 59,
        "nome": "Milford Sound - Cruzeiro",
        "pais": "Nova Zelândia",
        "cidade": "Queenstown",
        "tipo": "Natureza",
        "duracao_horas": 10,
        "preco": 130.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Cruzeiro por fiordes dramáticos com cachoeiras, golfinhos e focas.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1469521669194-babb45599def?w=400"
    },
    # === BRASIL (mais opções) ===
    {
        "id": 60,
        "nome": "Fernando de Noronha - Mergulho",
        "pais": "Brasil",
        "cidade": "Fernando de Noronha",
        "tipo": "Aventura",
        "duracao_horas": 4,
        "preco": 250.0,
        "gratuito": False,
        "max_pessoas": 6,
        "descricao": "Mergulho com cilindro em águas cristalinas com tartarugas e golfinhos.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=400"
    },
    {
        "id": 61,
        "nome": "Chapada Diamantina - Trilha",
        "pais": "Brasil",
        "cidade": "Lençóis",
        "tipo": "Natureza",
        "duracao_horas": 8,
        "preco": 120.0,
        "gratuito": False,
        "max_pessoas": 10,
        "descricao": "Trilha até a Cachoeira da Fumaça com paisagens de tirar o fôlego.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1518639192441-8fce0a366e2e?w=400"
    },
    {
        "id": 62,
        "nome": "Jantar Romântico em Gramado",
        "pais": "Brasil",
        "cidade": "Gramado",
        "tipo": "Romântico",
        "duracao_horas": 3,
        "preco": 180.0,
        "gratuito": False,
        "max_pessoas": 2,
        "descricao": "Jantar a luz de velas com fondue e vinhos em restaurante com lareira.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=400"
    },
    {
        "id": 63,
        "nome": "Lençóis Maranhenses",
        "pais": "Brasil",
        "cidade": "Barreirinhas",
        "tipo": "Natureza",
        "duracao_horas": 6,
        "preco": 95.0,
        "gratuito": False,
        "max_pessoas": 12,
        "descricao": "Passeio de 4x4 pelas dunas brancas com lagoas de água doce cristalina.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1518639192441-8fce0a366e2e?w=400"
    },
    # === ÍNDIA ===
    {
        "id": 64,
        "nome": "Taj Mahal ao Nascer do Sol",
        "pais": "Índia",
        "cidade": "Agra",
        "tipo": "Cultural",
        "duracao_horas": 4,
        "preco": 25.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Visite o monumento ao amor eterno com a luz dourada do amanhecer.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=400"
    },
    {
        "id": 65,
        "nome": "Passeio de Riquixá em Jaipur",
        "pais": "Índia",
        "cidade": "Jaipur",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 10.0,
        "gratuito": False,
        "max_pessoas": 4,
        "descricao": "Explore a Cidade Rosa em riquixá visitando palácios e mercados coloridos.",
        "avaliacao": 4.5,
        "imagem": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=400"
    },
    {
        "id": 66,
        "nome": "Aula de Culinária Indiana",
        "pais": "Índia",
        "cidade": "Nova Delhi",
        "tipo": "Gastronomia",
        "duracao_horas": 4,
        "preco": 35.0,
        "gratuito": False,
        "max_pessoas": 8,
        "descricao": "Aprenda a preparar curry, naan e chai com uma família local.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1505253758473-96b7015fcd40?w=400"
    },
    # === CANADÁ ===
    {
        "id": 67,
        "nome": "Cataratas do Niágara - Barco",
        "pais": "Canadá",
        "cidade": "Toronto",
        "tipo": "Aventura",
        "duracao_horas": 4,
        "preco": 45.0,
        "gratuito": False,
        "max_pessoas": 50,
        "descricao": "Passeio de barco até a base das cataratas mais famosas da América do Norte.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1489447068241-b3490214e879?w=400"
    },
    {
        "id": 68,
        "nome": "Aurora Boreal em Yellowknife",
        "pais": "Canadá",
        "cidade": "Yellowknife",
        "tipo": "Natureza",
        "duracao_horas": 5,
        "preco": 120.0,
        "gratuito": False,
        "max_pessoas": 12,
        "descricao": "Observe a aurora boreal no melhor ponto da América do Norte.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1483347756197-71ef80e95f73?w=400"
    },
    {
        "id": 69,
        "nome": "Parque Nacional Banff - Trilha",
        "pais": "Canadá",
        "cidade": "Banff",
        "tipo": "Natureza",
        "duracao_horas": 7,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 10,
        "descricao": "Trilha pelo Lake Louise com montanhas rochosas e lagos turquesa.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1503614472-8c93d56e92ce?w=400"
    },
    # === CROÁCIA ===
    {
        "id": 70,
        "nome": "Muralhas de Dubrovnik",
        "pais": "Croácia",
        "cidade": "Dubrovnik",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 30.0,
        "gratuito": False,
        "max_pessoas": 25,
        "descricao": "Caminhe pelas muralhas medievais com vista para o mar Adriático.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1555990793-da11153b2473?w=400"
    },
    {
        "id": 71,
        "nome": "Lagos de Plitvice",
        "pais": "Croácia",
        "cidade": "Plitvice",
        "tipo": "Natureza",
        "duracao_horas": 6,
        "preco": 25.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Passarelas sobre lagos esmeralda e cachoeiras em floresta pristina.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1504870712952-3f5164305c02?w=400"
    },
    # === ISLÂNDIA ===
    {
        "id": 72,
        "nome": "Círculo Dourado",
        "pais": "Islândia",
        "cidade": "Reykjavik",
        "tipo": "Natureza",
        "duracao_horas": 8,
        "preco": 80.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Gêisers, cachoeiras e placas tectônicas no circuito mais famoso da Islândia.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1504829857797-ddff29c27927?w=400"
    },
    {
        "id": 73,
        "nome": "Lagoa Azul (Blue Lagoon)",
        "pais": "Islândia",
        "cidade": "Reykjavik",
        "tipo": "Romântico",
        "duracao_horas": 4,
        "preco": 70.0,
        "gratuito": False,
        "max_pessoas": 50,
        "descricao": "Banho em águas termais azul-leitosas cercadas por campos de lava.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1515238152791-8216bfdf89a7?w=400"
    },
    {
        "id": 74,
        "nome": "Caverna de Gelo no Vatnajökull",
        "pais": "Islândia",
        "cidade": "Reykjavik",
        "tipo": "Aventura",
        "duracao_horas": 5,
        "preco": 150.0,
        "gratuito": False,
        "max_pessoas": 8,
        "descricao": "Explore cavernas de gelo azul cristalino dentro do maior glaciar europeu.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1520769669658-f07657f5a307?w=400"
    },
    # === VIETNÃ ===
    {
        "id": 75,
        "nome": "Baía de Ha Long - Cruzeiro",
        "pais": "Vietnã",
        "cidade": "Hanói",
        "tipo": "Natureza",
        "duracao_horas": 8,
        "preco": 65.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Cruzeiro por ilhas calcárias e cavernas na baía mais bonita do Sudeste Asiático.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1528127269322-539152a5b4d2?w=400"
    },
    {
        "id": 76,
        "nome": "Street Food Tour em Ho Chi Minh",
        "pais": "Vietnã",
        "cidade": "Ho Chi Minh",
        "tipo": "Gastronomia",
        "duracao_horas": 4,
        "preco": 20.0,
        "gratuito": False,
        "max_pessoas": 10,
        "descricao": "Prove phở, bánh mì e café vietnamita em barracas locais de moto.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1583417319070-4a69db38a482?w=400"
    },
    # === COREIA DO SUL ===
    {
        "id": 77,
        "nome": "Palácio Gyeongbokgung",
        "pais": "Coreia do Sul",
        "cidade": "Seul",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 5.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Visite o palácio real da dinastia Joseon com hanbok tradicional.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1534274988757-a28bf1a57c17?w=400"
    },
    {
        "id": 78,
        "nome": "K-Food Tour em Myeongdong",
        "pais": "Coreia do Sul",
        "cidade": "Seul",
        "tipo": "Gastronomia",
        "duracao_horas": 3,
        "preco": 40.0,
        "gratuito": False,
        "max_pessoas": 8,
        "descricao": "Prove tteokbokki, Korean BBQ e hotteok nas ruas mais movimentadas de Seul.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=400"
    },
    # === CUBA ===
    {
        "id": 79,
        "nome": "Havana Velha em Carro Clássico",
        "pais": "Cuba",
        "cidade": "Havana",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 40.0,
        "gratuito": False,
        "max_pessoas": 4,
        "descricao": "Passeio em carro americano dos anos 50 pelas ruas coloridas de Havana.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1500759285222-a95626b934cb?w=400"
    },
    {
        "id": 80,
        "nome": "Aula de Salsa e Mojito",
        "pais": "Cuba",
        "cidade": "Havana",
        "tipo": "Cultural",
        "duracao_horas": 2,
        "preco": 25.0,
        "gratuito": False,
        "max_pessoas": 12,
        "descricao": "Aprenda a dançar salsa e prepare mojitos com músicos cubanos ao vivo.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1545128485-c400e7702796?w=400"
    },
    # === NORUEGA ===
    {
        "id": 81,
        "nome": "Fiordes Noruegueses - Cruzeiro",
        "pais": "Noruega",
        "cidade": "Bergen",
        "tipo": "Natureza",
        "duracao_horas": 7,
        "preco": 110.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Navegue pelos fiordes dramáticos com cachoeiras e vilarejos pitorescos.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1507272931001-fc06c17e4f43?w=400"
    },
    {
        "id": 82,
        "nome": "Trilha Trolltunga",
        "pais": "Noruega",
        "cidade": "Odda",
        "tipo": "Aventura",
        "duracao_horas": 12,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 6,
        "descricao": "Trilha desafiadora até a língua de rocha suspensa sobre o fiorde.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1520769669658-f07657f5a307?w=400"
    },
    # === ÁFRICA DO SUL ===
    {
        "id": 83,
        "nome": "Safari no Kruger Park",
        "pais": "África do Sul",
        "cidade": "Joanesburgo",
        "tipo": "Natureza",
        "duracao_horas": 10,
        "preco": 180.0,
        "gratuito": False,
        "max_pessoas": 8,
        "descricao": "Safari fotográfico em busca dos Big Five em veículo 4x4 aberto.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1516426122078-c23e76319801?w=400"
    },
    {
        "id": 84,
        "nome": "Table Mountain",
        "pais": "África do Sul",
        "cidade": "Cidade do Cabo",
        "tipo": "Natureza",
        "duracao_horas": 4,
        "preco": 20.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Suba de teleférico ou trilha até o topo com vista 360° da cidade e oceano.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1580060839134-75a5edca2e99?w=400"
    },
    {
        "id": 85,
        "nome": "Degustação de Vinhos em Stellenbosch",
        "pais": "África do Sul",
        "cidade": "Cidade do Cabo",
        "tipo": "Gastronomia",
        "duracao_horas": 5,
        "preco": 65.0,
        "gratuito": False,
        "max_pessoas": 12,
        "descricao": "Tour por vinícolas premiadas na região vinícola mais bonita da África.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?w=400"
    },
    # === IRLANDA ===
    {
        "id": 86,
        "nome": "Falésias de Moher",
        "pais": "Irlanda",
        "cidade": "Dublin",
        "tipo": "Natureza",
        "duracao_horas": 10,
        "preco": 55.0,
        "gratuito": False,
        "max_pessoas": 25,
        "descricao": "Falésias de 200m sobre o Atlântico com paisagens verdes dramáticas.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1509005084666-3cbc75184cbb?w=400"
    },
    {
        "id": 87,
        "nome": "Tour de Pubs com Música Ao Vivo",
        "pais": "Irlanda",
        "cidade": "Dublin",
        "tipo": "Gastronomia",
        "duracao_horas": 4,
        "preco": 30.0,
        "gratuito": False,
        "max_pessoas": 15,
        "descricao": "Visite pubs tradicionais com música irlandesa ao vivo e degustação de whiskey.",
        "avaliacao": 4.5,
        "imagem": "https://images.unsplash.com/photo-1543007630-9710e4a00a20?w=400"
    },
    # === TANZÂNIA ===
    {
        "id": 88,
        "nome": "Safari no Serengeti",
        "pais": "Tanzânia",
        "cidade": "Arusha",
        "tipo": "Natureza",
        "duracao_horas": 12,
        "preco": 300.0,
        "gratuito": False,
        "max_pessoas": 6,
        "descricao": "Safari pela savana africana durante a Grande Migração de gnus.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=400"
    },
    {
        "id": 89,
        "nome": "Zanzibar - Praias de Areia Branca",
        "pais": "Tanzânia",
        "cidade": "Zanzibar",
        "tipo": "Romântico",
        "duracao_horas": 8,
        "preco": 50.0,
        "gratuito": False,
        "max_pessoas": 10,
        "descricao": "Dia em praias paradisíacas com snorkeling e almoço de frutos do mar.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1501179691627-eeaa65ea017c?w=400"
    },
    # === JORDÂNIA ===
    {
        "id": 90,
        "nome": "Petra - Cidade Rosa",
        "pais": "Jordânia",
        "cidade": "Petra",
        "tipo": "Cultural",
        "duracao_horas": 8,
        "preco": 70.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Explore a cidade esculpida em rocha rosa, uma das Novas Maravilhas do Mundo.",
        "avaliacao": 4.9,
        "imagem": "https://images.unsplash.com/photo-1579606032821-4e6161c81571?w=400"
    },
    {
        "id": 91,
        "nome": "Flutuação no Mar Morto",
        "pais": "Jordânia",
        "cidade": "Amã",
        "tipo": "Natureza",
        "duracao_horas": 3,
        "preco": 25.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Flutue nas águas ultra-salgadas do ponto mais baixo da Terra com lama terapêutica.",
        "avaliacao": 4.5,
        "imagem": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=400"
    },
    # === PORTUGAL (mais opções) ===
    {
        "id": 92,
        "nome": "Passeio de Barco no Algarve",
        "pais": "Portugal",
        "cidade": "Faro",
        "tipo": "Aventura",
        "duracao_horas": 3,
        "preco": 35.0,
        "gratuito": False,
        "max_pessoas": 15,
        "descricao": "Navegue por grutas e praias secretas nas falésias douradas do Algarve.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=400"
    },
    {
        "id": 93,
        "nome": "Sintra - Palácio da Pena",
        "pais": "Portugal",
        "cidade": "Lisboa",
        "tipo": "Cultural",
        "duracao_horas": 5,
        "preco": 30.0,
        "gratuito": False,
        "max_pessoas": 20,
        "descricao": "Visite o colorido Palácio da Pena e os jardins românticos de Sintra.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1588262209458-16541af15fbd?w=400"
    },
    # === JAPÃO (mais opções) ===
    {
        "id": 94,
        "nome": "Floresta de Bambu de Arashiyama",
        "pais": "Japão",
        "cidade": "Kyoto",
        "tipo": "Natureza",
        "duracao_horas": 2,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 50,
        "descricao": "Caminhe entre bambus gigantes numa das paisagens mais mágicas do Japão.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1545569341-9eb8b30979d9?w=400"
    },
    {
        "id": 95,
        "nome": "Monte Fuji - Trilha até o 5º Posto",
        "pais": "Japão",
        "cidade": "Tóquio",
        "tipo": "Aventura",
        "duracao_horas": 10,
        "preco": 90.0,
        "gratuito": False,
        "max_pessoas": 12,
        "descricao": "Trilha ao vulcão sagrado do Japão com vista do nascer do sol no topo.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1490806843957-31f4c9a91c65?w=400"
    },
    # === ESPANHA (mais opções) ===
    {
        "id": 96,
        "nome": "Flamenco em Sevilha",
        "pais": "Espanha",
        "cidade": "Sevilha",
        "tipo": "Cultural",
        "duracao_horas": 2,
        "preco": 35.0,
        "gratuito": False,
        "max_pessoas": 30,
        "descricao": "Show autêntico de flamenco em tablao tradicional com tapas e vinho.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1551369247-eca8a5f1f9c0?w=400"
    },
    {
        "id": 97,
        "nome": "Caminho de Santiago - Etapa Final",
        "pais": "Espanha",
        "cidade": "Santiago de Compostela",
        "tipo": "Aventura",
        "duracao_horas": 8,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 6,
        "descricao": "Caminhe os últimos 25km do Caminho com chegada à Catedral de Santiago.",
        "avaliacao": 4.8,
        "imagem": "https://images.unsplash.com/photo-1543783207-ec64e4d95325?w=400"
    },
    # === ESTADOS UNIDOS (mais opções) ===
    {
        "id": 98,
        "nome": "Tour pela Golden Gate",
        "pais": "Estados Unidos",
        "cidade": "San Francisco",
        "tipo": "Cultural",
        "duracao_horas": 3,
        "preco": 0.0,
        "gratuito": True,
        "max_pessoas": 50,
        "descricao": "Bike ou caminhada pela ponte Golden Gate com vista da baía e Alcatraz.",
        "avaliacao": 4.6,
        "imagem": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=400"
    },
    {
        "id": 99,
        "nome": "Helicóptero sobre Las Vegas",
        "pais": "Estados Unidos",
        "cidade": "Las Vegas",
        "tipo": "Aventura",
        "duracao_horas": 1,
        "preco": 200.0,
        "gratuito": False,
        "max_pessoas": 6,
        "descricao": "Voo noturno de helicóptero sobre a Strip de Las Vegas iluminada.",
        "avaliacao": 4.7,
        "imagem": "https://images.unsplash.com/photo-1506197603052-3cc9c3a201bd?w=400"
    },
    {
        "id": 100,
        "nome": "Everglades - Airboat Safari",
        "pais": "Estados Unidos",
        "cidade": "Miami",
        "tipo": "Natureza",
        "duracao_horas": 3,
        "preco": 45.0,
        "gratuito": False,
        "max_pessoas": 12,
        "descricao": "Passeio de airboat pelos pântanos com jacarés e aves exóticas.",
        "avaliacao": 4.5,
        "imagem": "https://images.unsplash.com/photo-1500759285222-a95626b934cb?w=400"
    },
]


def get_paises():
    """Retorna lista de países únicos."""
    return sorted(list(set(tour["pais"] for tour in TOURS)))


def get_cidades(pais=None):
    """Retorna lista de cidades, opcionalmente filtradas por país."""
    if pais:
        return sorted(list(set(
            tour["cidade"] for tour in TOURS if tour["pais"] == pais
        )))
    return sorted(list(set(tour["cidade"] for tour in TOURS)))


def get_tipos():
    """Retorna lista de tipos de passeio únicos."""
    return sorted(list(set(tour["tipo"] for tour in TOURS)))


def recomendar_passeios(filtros):
    """
    Filtra e recomenda passeios com base nos critérios do usuário.
    """
    resultados = TOURS.copy()

    if filtros.get("pais"):
        resultados = [t for t in resultados if t["pais"] == filtros["pais"]]

    if filtros.get("cidade"):
        resultados = [t for t in resultados if t["cidade"] == filtros["cidade"]]

    if filtros.get("tipo"):
        resultados = [t for t in resultados if t["tipo"] == filtros["tipo"]]

    if filtros.get("gratuito") is not None:
        if filtros["gratuito"]:
            resultados = [t for t in resultados if t["gratuito"]]

    if filtros.get("preco_max") is not None and filtros["preco_max"] > 0:
        resultados = [t for t in resultados if t["preco"] <= filtros["preco_max"]]

    if filtros.get("duracao_max") is not None and filtros["duracao_max"] > 0:
        resultados = [
            t for t in resultados if t["duracao_horas"] <= filtros["duracao_max"]
        ]

    if filtros.get("pessoas") is not None and filtros["pessoas"] > 0:
        resultados = [
            t for t in resultados if t["max_pessoas"] >= filtros["pessoas"]
        ]

    # Ordenar por avaliação (melhor primeiro)
    resultados.sort(key=lambda x: x["avaliacao"], reverse=True)

    return resultados
