import json
import os
import unicodedata
from difflib import get_close_matches
 
ARQUIVO_FAQ = "faq.json"
 
# Remove acentos e coloca tudo em minúsculo
def normalizar(texto):
    texto = unicodedata.normalize('NFD', texto)
    texto_sem_acento = ''.join(
        c for c in texto if unicodedata.category(c) != 'Mn'
    )
    return texto_sem_acento.lower()
 
# Carrega a base de dados se o arquivo existir
def carregar_faq():
    if os.path.exists(ARQUIVO_FAQ):
        with open(ARQUIVO_FAQ, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
 
# Salva a base de dados
def salvar_faq(faq):
    with open(ARQUIVO_FAQ, "w", encoding="utf-8") as f:
        json.dump(faq, f, ensure_ascii=False, indent=2)
 
# Busca a melhor resposta com base em palavras-chave coincidentes
def encontrar_resposta(pergunta, faq):
    palavras_usuario = normalizar(pergunta).split()
    melhores = []
 
    for item in faq:
        palavras_chave = [normalizar(p.strip()) for p in item.get("palavras_chave", [])]
        coincidencias = sum(1 for p in palavras_chave if p in palavras_usuario)
 
        if coincidencias > 0:
            melhores.append((coincidencias, item["resposta"], item["pergunta"]))
 
    if melhores:
        melhores.sort(reverse=True, key=lambda x: x[0])
        melhor = melhores[0]
        print(f"\n Melhor correspondência com: {melhor[2]}")
        return melhor[1]
 
    # Busca por pergunta parecida com difflib, como apoio extra
    perguntas = [item["pergunta"] for item in faq]
    similares = get_close_matches(pergunta, perguntas, n=1, cutoff=0.6)
    if similares:
        for item in faq:
            if item["pergunta"] == similares[0]:
                print(f"\n Pergunta parecida encontrada: {item['pergunta']}")
                return item["resposta"]
 
    return None
 
# Loop principal
def main():
    faq = carregar_faq()
    print(" Sistema de Perguntas e Respostas (digite 'sair' para encerrar)\n")
 
    while True:
        pergunta = input("Nos informe a sua dúvida: ").strip()
        if normalizar(pergunta) == "sair":
            break
 
        resposta = encontrar_resposta(pergunta, faq)
 
        if resposta:
            print(" Resposta:", resposta)
        else:
            print(" Essa pergunta ainda não tem resposta.")
            if input("Deseja adicionar uma resposta agora? (s/n) > ").strip().lower() == "s":
                nova_resposta = input("Digite a resposta > ")
                chaves = input("Digite palavras-chave separadas por vírgula > ")
                palavras = [normalizar(p.strip()) for p in chaves.split(",")]
 
                faq.append({
                    "pergunta": pergunta,
                    "resposta": nova_resposta,
                    "palavras_chave": palavras
                })
                salvar_faq(faq)
                print(" Resposta salva com sucesso!\n")
 
if __name__ == "__main__":
    main()