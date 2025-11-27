# LLM Resumidor Python

Este projeto é um **resumidor automático de textos** desenvolvido em Python utilizando um modelo de linguagem (LLM).  
O user fornece um texto e o sistema retorna:

- Um resumo
- Lista de tópicos principais
- Uma aplicação prática do conteúdo (quando aplicável)

O objetivo do projeto é demonstrar o uso de LLMs para automação de tarefas de leitura, compreensão de texto e resumo de informação.

## 🚀 Funcionalidades

- Recebe textos longos via terminal ou via arquivo `.txt`
- Envia o conteúdo para um modelo de linguagem
- Aí retorna:
  - Resumo em parágrafos curtos
  - Tópicos principais
  - Sugestão de aplicação prática
- Controle de qualidade via prompt engineering
- Integração com API de modelo de linguagem
- Estrutura simples e fácil de adaptar


## 🛠️ Tecnologias utilizadas

- Python 3+
- OpenAI SDK
- API de modelo de linguagem (LLM)
- Virtual Environment (venv)
- Prompt Engineering
- Terminal (CLI)

## 📥 Como executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/Dinastra/llm-resumidor-python.git
cd llm-resumidor-python
```


### 2. Crie e ative o ambiente virtual

**Windows (cmd / Git Bash):**
```bat
python -m venv .venv
.\.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```


### 3. Instale as dependências

```bash
pip install openai
```


### 4. Configure a variável de ambiente da API

Você precisa ter uma chave válida da OpenAI. Ela tem que ser ativa.

**Windows (CMD):**
```bat
set OPENAI_API_KEY=SUA_CHAVE_AQUI
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY="SUA_CHAVE_AQUI"
```


### 5. Execute o projeto

```bash
python resumidor.py
```

Cole o texto quando solicitado e finalize com:

- **Windows:** `Ctrl + Z` + Enter  
- **Linux/Mac:** `Ctrl + D`

O resultado aparecerá no próprio terminal.


## 📂 Estrutura do projeto

```
llm-resumidor-python/
│
├── resumidor.py
├── README.md
└── .venv/
```


## 📌 Observações importantes

- A chave da API **NÃO** deve ser inserida no código.
- Não compartilhe sua chave em repositórios públicos.
- Caso ocorra erro `billing_not_active`, verifique se a conta da API possui créditos ativos. Isso é MUITO importante, pois se não tiver créditos ativos, vai apontar um erro.


## 💡 Motivação

Este projeto foi desenvolvido com foco em aprendizado prático em **Ciência de Dados e Inteligência Artificial**, com o objetivo de entender melhor:

- Integração com LLMs via API
- Funcionamento de prompts
- Estruturação de projetos em Python
- Automação de tarefas cognitivas


## 📈 Próximos passos (pra evoluir o projeto)

- Interface web
- Suporte a arquivos PDF
- Escolha dinâmica de modelos
- Parâmetros de tamanho do resumo
- Exportação para `.txt` ou `.pdf`
- Histórico de resumos


## 👩‍💻 Desenvolvedora (ou seja, euzinha)

Projeto desenvolvido por **Evelyn Melo** mas vocês tmb podem me chamar de **Dinastra**  


## 🤝 Contribuições

Sugestões e melhorias são bem-vindas.  
Sinta-se à vontade para abrir issues e pull requests.

---

Se este projeto te ajudou de alguma forma, deixe uma ⭐!
