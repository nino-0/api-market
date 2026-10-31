from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Defina a lista de URLs (origens) que têm permissão para acessar sua API
origins = [
    "http://localhost:5173",  # URL padrão do seu Vite/React
    "http://127.0.0.1:5173",  # Alternativa comum para o localhost do Vite
]

# Configure o middleware do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Permite requisições das URLs da lista acima
    allow_credentials=True,           # Permite o envio de cookies e cabeçalhos de autenticação
    allow_methods=["*"],              # Permite todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],              # Permite todos os cabeçalhos (Headers)
)


@app.get("/products")
async def getProducts():
    return {"products":products}

@app.post("/purchase")
async def purchase():
    return {"msg":"done"}




products = [
    {
        "id": 1,
        "name": "Doce de Caju",
        "price": 15.90,
        "description": "Doce tradicional de caju em calda, caseiro e com sabor marcante.",
        "estoque_num": 25,
        "img_url": "img1.jpg",
    },
    {
        "id": 2,
        "name": "Doce de Banana",
        "price": 12.50,
        "description": "Doce de banana pastoso, feito com bananas selecionadas e sem adição de conservantes artificiais.",
        "estoque_num": 30,
        "img_url": "img2.jpg",
    },
    {
        "id": 3,
        "name": "Doce de Leite",
        "price": 18.00,
        "description": "Doce de leite cremoso tradicional, derrete na boca.",
        "estoque_num": 40,
        "img_url": "img3.jpg",
    },
    {
        "id": 4,
        "name": "Torta Trufada",
        "price": 45.00,
        "description": "Fatia de torta trufada de chocolate com recheio cremoso e cobertura de ganache.",
        "estoque_num": 10,
        "img_url": "img4.jpg",
    },
    {
        "id": 5,
        "name": "Salada de Frutas",
        "price": 10.00,
        "description": "Mix de frutas frescas da estação cortadas, acompanhadas de suco natural de laranja.",
        "estoque_num": 15,
        "img_url": "img5.jpg",
    },
    {
        "id": 6,
        "name": "Bolo de Pote",
        "price": 9.90,
        "description": "Bolo de pote sabor prestígio, com massa fofinha e muito recheio.",
        "estoque_num": 20,
        "img_url": "img6.jpg",
    },
    {
        "id": 7,
        "name": "Geladinho Gourmet",
        "price": 6.00,
        "description": "Geladinho gourmet de Ninho com Nutella, cremoso e refrescante.",
        "estoque_num": 50,
        "img_url": "img7.jpg",
    },
]