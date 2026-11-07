# 🌐 Coleta de Dados da Web com Python

> Projeto desenvolvido para praticar técnicas de **Web Scraping** e **Extração de Dados** utilizando Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Requests](https://img.shields.io/badge/Requests-HTTP-success)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-green)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple)

---

# 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte dos meus estudos em **Python para Ciência e Análise de Dados**.

O objetivo é aprender diferentes técnicas de coleta de informações disponíveis na internet utilizando bibliotecas amplamente empregadas no mercado.

Durante o desenvolvimento são exploradas duas abordagens principais:

- 🌐 Requisições HTTP utilizando **Requests**
- 🍲 Leitura e interpretação do HTML com **BeautifulSoup**
- 📊 Extração automática de tabelas utilizando **Pandas**

Como fonte de dados, foi utilizada a página da Wikipédia contendo a lista das maiores empresas do mundo por receita.

---

# 🎯 Objetivos

- ✔️ Realizar requisições HTTP
- ✔️ Entender a estrutura de páginas HTML
- ✔️ Navegar pela árvore HTML utilizando BeautifulSoup
- ✔️ Extrair tabelas diretamente com Pandas
- ✔️ Manipular dados estruturados
- ✔️ Desenvolver conhecimentos em Web Scraping

---

# 🛠 Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| 🐍 Python | Linguagem principal |
| 🌐 Requests | Requisições HTTP |
| 🍲 BeautifulSoup4 | Análise e navegação do HTML |
| 🐼 Pandas | Extração e manipulação de tabelas |

---

# 📂 Estrutura do Projeto

```text
📁 Web-Scraping-Python
│
├── coleta_dados.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Como Executar

### Clone o repositório

```bash
git clone https://github.com/jeffersonDot/NOME-DO-REPOSITORIO.git
```

### Entre na pasta

```bash
cd NOME-DO-REPOSITORIO
```

### Instale as dependências

```bash
pip install requests beautifulsoup4 pandas lxml
```

### Execute

```bash
python coleta_dados.py
```

---

# 📊 O que o projeto faz?

### 🔹 Requests

Realiza uma requisição HTTP para obter o conteúdo da página da Wikipédia.

```python
response = requests.get(url)
```

---

### 🔹 BeautifulSoup

Converte o HTML em uma estrutura navegável, permitindo localizar elementos específicos da página.

```python
soup = BeautifulSoup(response.text, "html.parser")
```

---

### 🔹 Pandas

Extrai automaticamente todas as tabelas presentes na página.

```python
tabelas = pandas.read_html(url)
```

Em seguida, é exibida a primeira tabela contendo as maiores empresas do mundo por receita.

---

# 📈 Exemplo de Dados Obtidos

| Rank | Empresa | Receita |
|------:|----------|---------:|
| 1 | Walmart | US$ 681 bilhões |
| 2 | Amazon | US$ 638 bilhões |
| 3 | State Grid | US$ 545 bilhões |
| 4 | Saudi Aramco | US$ 495 bilhões |
| 5 | Sinopec | US$ 429 bilhões |

---

# 🚀 Aprendizados

Ao desenvolver este projeto pratiquei conceitos importantes como:

- 🌍 Web Scraping
- 🔎 Estrutura HTML
- 📡 Requisições HTTP
- 🧹 Extração de dados
- 📊 DataFrames
- 🐼 Manipulação de dados com Pandas
- 💻 Boas práticas em Python

---

# 📚 Fonte dos Dados

Os dados utilizados neste projeto foram obtidos da página pública da Wikipédia:

🔗 https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue

---

# 🔮 Próximas Melhorias

- ✅ Extrair apenas colunas específicas
- 📈 Criar gráficos com Matplotlib
- 💾 Exportar para CSV e Excel
- 🗃️ Salvar em banco de dados
- 🔄 Automatizar a atualização dos dados
- 🌐 Coletar informações de outras páginas

---

# 👨‍💻 Autor

### Jefferson Santos

🎓 Tecnólogo em Análise e Desenvolvimento de Sistemas

📊 Estudante de Ciência de Dados, Python, Excel e Power BI.

🔗 GitHub: **https://github.com/jeffersonDot**

---

⭐ Este projeto faz parte da minha jornada de aprendizado em Python e Ciência de Dados. Toda sugestão ou feedback é bem-vindo!
