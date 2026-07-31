# 🌍 TourGuide - Recomendação de Passeios Turísticos

Sistema inteligente de recomendação de passeios turísticos com filtros personalizados para encontrar a experiência ideal para sua próxima viagem.

🔗 **Acesse o site:** [https://tourrecommender.onrender.com](https://tourrecommender.onrender.com)

---

## 📋 Sobre o Projeto

O TourGuide é uma aplicação web que ajuda viajantes a descobrir passeios turísticos com base em suas preferências. O usuário pode filtrar por país, cidade, tipo de passeio, orçamento, duração e tamanho do grupo, recebendo recomendações ordenadas por avaliação.

---

## ✨ Funcionalidades

- 🌎 **Filtro por País** — 32 países disponíveis
- 🏙️ **Filtro por Cidade** — 71 cidades (atualiza dinamicamente ao selecionar o país)
- 🎯 **Tipo de Passeio** — Cultural, Natureza, Aventura, Gastronomia, Romântico
- 💰 **Preço Máximo** — Defina seu orçamento ou busque apenas passeios gratuitos
- ⏱️ **Duração Máxima** — Filtre por tempo disponível (em horas)
- 👥 **Quantidade de Pessoas** — Encontre passeios adequados ao tamanho do grupo
- ⭐ **Ordenação por Avaliação** — Resultados ordenados dos melhores avaliados
- 📱 **Design Responsivo** — Funciona em desktop, tablet e celular

---

## 🗺️ Países Disponíveis

| | | | |
|---|---|---|---|
| África do Sul | Alemanha | Argentina | Austrália |
| Brasil | Canadá | Chile | Colômbia |
| Coreia do Sul | Croácia | Cuba | Egito |
| Espanha | Estados Unidos | França | Grécia |
| Índia | Irlanda | Islândia | Itália |
| Japão | Jordânia | Marrocos | México |
| Noruega | Nova Zelândia | Peru | Portugal |
| Tailândia | Tanzânia | Turquia | Vietnã |

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| **Python 3.11** | Linguagem principal do backend |
| **Flask** | Framework web |
| **Gunicorn** | Servidor WSGI para produção |
| **HTML5** | Estrutura do frontend |
| **CSS3** | Estilização com design moderno |
| **JavaScript (Vanilla)** | Interatividade e chamadas à API |
| **Render** | Hospedagem e deploy |

---

## 📁 Estrutura do Projeto

```
tourrecommender/
├── app.py              # Backend Flask com rotas da API
├── tour_data.py        # Base de dados com 100 passeios
├── requirements.txt    # Dependências Python
├── render.yaml         # Configuração de deploy no Render
├── Procfile            # Comando de inicialização
├── .gitignore          # Arquivos ignorados pelo Git
└── static/
    ├── index.html      # Página principal
    ├── styles.css      # Estilos CSS
    └── app.js          # Lógica do frontend
```

---

## 🚀 Como Rodar Localmente

```bash
# Clonar o repositório
git clone https://github.com/monica1602/tourrecommender.git
cd tourrecommender

# Instalar dependências
pip install -r requirements.txt

# Iniciar o servidor
python app.py
```

Acesse **http://localhost:5000** no navegador.

---

## 🔌 API Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Página principal |
| GET | `/api/paises` | Lista de países disponíveis |
| GET | `/api/cidades?pais=Brasil` | Cidades filtradas por país |
| GET | `/api/tipos` | Tipos de passeio disponíveis |
| POST | `/api/recomendar` | Recomendação com filtros (JSON) |

### Exemplo de requisição POST `/api/recomendar`:

```json
{
  "pais": "Brasil",
  "cidade": "",
  "tipo": "Natureza",
  "gratuito": false,
  "preco_max": 100,
  "duracao_max": 6,
  "pessoas": 2
}
```

---

## 📊 Dados

- **100 passeios** cadastrados
- **32 países** representados
- **71 cidades** diferentes
- **5 categorias** de passeio
- Preços de **gratuito** até **R$ 300**
- Durações de **1h** até **24h**

---

## 🌐 Deploy

O site está hospedado no Render com deploy automático a partir do branch `main`.

🔗 **URL:** [https://tourrecommender.onrender.com](https://tourrecommender.onrender.com)

> ⚠️ No plano gratuito do Render, o serviço pode levar alguns segundos para "acordar" após inatividade.

---

## 📝 Licença

Este projeto é de uso livre para fins educacionais e pessoais.

---

Feito com ❤️ por [monica1602](https://github.com/monica1602)
