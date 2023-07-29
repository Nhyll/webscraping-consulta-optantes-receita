# Importando as bibliotecas necessárias
from twocaptcha import TwoCaptcha
import requests
from bs4 import BeautifulSoup
import configparser

# Lendo as configurações do arquivo .config
config = configparser.ConfigParser()
config.read('.config')

# Obtendo a chave da API do serviço de resolução de captcha e o CNPJ da empresa a ser consultada
API_KEY = config.get('CAPTCHA', 'API_KEY')
CNPJ = config.get('COMPANY', 'CNPJ')

# URLs para consulta e o endpoint para submeter o formulário com os dados
URL = "https://consopt.www8.receita.fazenda.gov.br/consultaoptantes"
NEW_URL = "https://consopt.www8.receita.fazenda.gov.br/consultaoptantes/Home/ConsultarCnpj?vc={}"

# Iniciando uma sessão para manter cookies e outras informações
session = requests.Session()

# Configurando o serviço de resolução de captcha (TwoCaptcha) com a chave da API
SOLVER = TwoCaptcha(API_KEY)

# Fazendo uma requisição GET para a página de consulta para obter os cookies
ret = session.get(URL)

# Verificando se a requisição foi bem-sucedida (status_code 200)
if ret.status_code == 200:
    cookie_value = ret.headers.get('Set-Cookie')
    if not cookie_value:
        print("Nenhum cookie encontrado na resposta.")
        exit()
else:
    print(f"Falha na requisição. Código de status: {ret.status_code}")
    exit()

# Analisando a página com BeautifulSoup para extrair o valor do token de verificação
soup = BeautifulSoup(ret.content, 'html.parser')
input_element = soup.find('input', {'name': '__RequestVerificationToken'})

if input_element:
    request_verification_token = input_element['value']
else:
    print("Elemento não encontrado.")
    exit()

# Resolvendo o captcha usando o serviço de resolução de captcha (TwoCaptcha)
captcha_solution = SOLVER.hcaptcha(sitekey='96a07261-d2ef-4959-a17b-6ae56f256b3f', url=URL)

# Dados do formulário para submeter a consulta do CNPJ
form_data = {
    "Cnpj": CNPJ,
    "__RequestVerificationToken": request_verification_token,
    "h-captcha-response": captcha_solution['code']
}

# Cabeçalhos HTTP com os cookies e informações do usuário (agente)
headers = {
    "Cookie": cookie_value,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}

# Enviando uma requisição POST com os dados do formulário e os cabeçalhos
resp = session.post(URL, data=form_data, headers=headers)

# Salvando a página de resposta em um arquivo HTML
with open("pagina_receita.html", "wb") as file:
    file.write(resp.content)

# Informando que a página foi salva com sucesso
print("Página salva com sucesso!")