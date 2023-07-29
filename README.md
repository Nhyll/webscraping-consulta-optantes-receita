## Webscraping para Consulta de Enquadramento Fiscal no site "Consulta Optantes Receita Federal"

Este projeto tem como objetivo realizar webscraping no site "Consulta Optantes Receita Federal" para consultar o enquadramento fiscal de um CNPJ fornecido pelo usuário. O site da Receita Federal possui um captcha que precisa ser resolvido para que a consulta seja realizada com sucesso. Para contornar isso, utilizamos a API do serviço "TwoCaptcha" para quebrar o captcha e obter a página de consulta com o resultado.

### Como funciona

O projeto é desenvolvido em Python e utiliza as bibliotecas "requests" para fazer requisições HTTP, "BeautifulSoup" para analisar o HTML da página e extrair informações, e "twocaptcha" para resolver o captcha.

### Requisitos

- Python 3.x
- Bibliotecas Python: requests, BeautifulSoup e twocaptcha

### Configuração

1. Clone o repositório para o seu computador.
2. Instale as bibliotecas necessárias executando o seguinte comando:

`pip install requests beautifulsoup4 twocaptcha`

3. Crie um arquivo chamado `.config` no diretório raiz do projeto com o seguinte formato:

[CAPTCHA]
API_KEY = sua_chave_api_do_twocaptcha

[COMPANY]
CNPJ = cnpj_para_consulta

Substitua `sua_chave_api_do_twocaptcha` pela sua chave da API do TwoCaptcha e `cnpj_para_consulta` pelo CNPJ que você deseja consultar.

### Executando o projeto

Para executar o webscraping e obter a página de consulta com o resultado, basta rodar o arquivo `main.py`

### Aviso Importante

Este projeto foi criado apenas para fins recreativos e educacionais. Ele não tem qualquer finalidade maliciosa ou de violação de privacidade. O uso deste código em qualquer atividade ilegal ou não ética é estritamente proibido.



