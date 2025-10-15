def criar_prova_fisica():
    """
    Função principal que executa o algoritmo da prova de física virtual.
    """
    
    # --- 1. Armazenamento de Dados ---
    # Uma lista de dicionários, onde cada dicionário representa uma questão.
    questoes = [
        {
            "conteudo": "Campo e Forças Magnéticas",
            "pergunta": "Uma partícula com carga elétrica positiva entra em uma região de campo magnético uniforme, com velocidade perpendicular às linhas de campo. Qual é a trajetória descrita pela partícula?",
            "opcoes": {
                "A": "Uma linha reta na mesma direção da velocidade inicial.",
                "B": "Uma trajetória circular uniforme.",
                "C": "Uma parábola.",
                "D": "A partícula para imediatamente."
            },
            "resposta_correta": "B"
        },
        {
            "conteudo": "Indução e Onda Eletromagnética",
            "pergunta": "De acordo com a Lei de Faraday-Lenz, a corrente elétrica induzida em uma espira condutora surge para:",
            "opcoes": {
                "A": "Maximizar o fluxo magnético através da espira.",
                "B": "Aumentar a velocidade da variação do fluxo magnético.",
                "C": "Gerar um campo magnético que se opõe à variação do fluxo magnético que a originou.",
                "D": "Anular completamente o campo magnético externo."
            },
            "resposta_correta": "C"
        },
        {
            "conteudo": "Circuitos Elétricos",
            "pergunta": "Em um circuito com três resistores de 10 Ω (ohms) cada, associados em série, e ligados a uma fonte de tensão de 60 V (volts), qual é a corrente elétrica total que percorre o circuito?",
            "opcoes": {
                "A": "6 A (ampères)",
                "B": "3 A (ampères)",
                "C": "2 A (ampères)",
                "D": "0.5 A (ampères)"
            },
            "resposta_correta": "C"
        }
    ]

    # --- 2. Coletar Informação do Usuário ---
    nome_usuario = input("Olá! Por favor, digite seu nome para começar: ")
    print(f"\nBem-vindo(a), {nome_usuario}! A prova de Física será iniciada.")
    print("----------------------------------------------------------")

    # --- 3. Executar a Prova ---
    pontuacao = 0
    conteudos_a_revisar = []

    # O laço 'for' percorre cada questão na lista
    for i, questao in enumerate(questoes):
        print(f"\nQuestão {i + 1}: ({questao['conteudo']})")
        print(questao['pergunta'])
        
        # Exibe as opções de forma organizada
        for alternativa, texto_opcao in questao['opcoes'].items():
            print(f"{alternativa}) {texto_opcao}")

        # Laço 'while' para validar a resposta do usuário
        while True:
            resposta_usuario = input("Digite sua resposta (A, B, C ou D): ").upper()
            if resposta_usuario in ["A", "B", "C", "D"]:
                break
            else:
                print("Opção inválida! Por favor, digite A, B, C ou D.")
        
        # Verifica se a resposta está correta
        if resposta_usuario == questao['resposta_correta']:
            print("Resposta correta!")
            pontuacao += 1
        else:
            print(f"Resposta incorreta. A resposta certa era a alternativa {questao['resposta_correta']}.")
            # Registra o conteúdo que o usuário errou
            conteudos_a_revisar.append(questao['conteudo'])
        
        print("----------------------------------------------------------")

    # --- 4. Calcular e Exibir Resultados ---
    total_de_questoes = len(questoes)
    nota_final = (pontuacao / total_de_questoes) * 10.0

    print(f"\nProva finalizada, {nome_usuario}!")
    print(f"Sua nota final foi: {nota_final:.1f} de 10.0")

    # --- 5. Gerar Feedback Personalizado ---
    if nota_final == 10.0:
        print("Parabéns! Você demonstrou excelente domínio em todos os conteúdos da prova.")
    else:
        # Usa um set para remover conteúdos duplicados, caso houvesse mais questões do mesmo tópico
        conteudos_unicos = set(conteudos_a_revisar)
        feedback = "\nCom base em seus erros, sugerimos que você revise os seguintes tópicos:\n"
        for conteudo in conteudos_unicos:
            feedback += f"- {conteudo}\n"
        print(feedback)


# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    criar_prova_fisica()
