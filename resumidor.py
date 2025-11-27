import os
import sys
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "A variável de ambiente OPENAI_API_KEY não está definida. "
        "Defina sua chave da API antes de rodar o script."
    )

client = OpenAI(api_key=API_KEY)

def resumir_texto(texto: str) -> str:
    prompt_sistema = (
        "Você é um assistente que resume textos em português de forma clara e objetiva.\n"
        "Sua resposta deve seguir o formato:\n\n"
        "1) Um resumo em até 5 parágrafos curtos.\n"
        "2) Em seguida, uma lista de 3 a 7 tópicos com os principais pontos do texto.\n"
        "3) Se fizer sentido, inclua uma frase final com possíveis aplicações práticas."
    )

    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": f"Resuma o seguinte texto:\n\n{texto}"}
        ],
        temperature=0.3,
    )

    return resposta.choices[0].message.content.strip()

def ler_texto_da_entrada() -> str:
    if len(sys.argv) > 1:
        caminho = sys.argv[1]
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()
    else:
        print(
            "Cole o texto a ser resumido e depois:\n"
            "- CTRL+D (Linux/Mac)\n"
            "- CTRL+Z e Enter (Windows)\n"
        )
        return sys.stdin.read()

def main():
    texto = ler_texto_da_entrada().strip()

    if not texto:
        print("Nenhum texto fornecido.")
        return

    print("\nGerando resumo...\n")
    resumo = resumir_texto(texto)

    print("===== RESUMO =====\n")
    print(resumo)

if __name__ == "__main__":
    main()