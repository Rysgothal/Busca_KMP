'''
    Funções para Auxiliar o código principal (kmp_princial): kmp_codigo.py

    Criado por: Gabriela Villani Moreira - RA: 181884 || 23/02/2023
    Alteração: Lucas Souza Frade - Ra: 181370         || 02/03/2023
'''

# Gabriela Villani - 23/02/2023 || Função para Buscar Subsequência
def BuscarSubsequencia(pSequencia, pSubsequencia):
    # Lucas Frade - 02/03/2023 || Eliminar posições repetidas
    vPosicao = set()
    vComparacaoBasica = 0
    vComparacaoKMP = 0

    # Busca por subsequências utilizando o método básico de comparação
    for i in range(len(pSequencia) - len(pSubsequencia) + 1):
        vComparacaoBasica += 1
        
        if pSequencia[i:i + len(pSubsequencia)] == pSubsequencia:
            # Adiciona a posição ao conjunto 
            vPosicao.add(i)
    
    vPrefixo = CalcularPrefixo(pSubsequencia)
    j = 0
    for i in range(len(pSequencia)):
        vComparacaoKMP += 1

        while j > 0 and pSequencia[i] != pSubsequencia[j]:
            j = vPrefixo[j-1]
        
        if pSequencia[i] == pSubsequencia[j]:
            j += 1
        
        if j == len(pSubsequencia):
            # Adiciona posição ao conjunto
            vPosicao.add(i - len(pSubsequencia) + 1)
            j = vPrefixo[j-1]

    # Retorna Lista ordenada de posições    
    return sorted(list(vPosicao)), vComparacaoBasica, vComparacaoKMP

# Gabriela Villani - 23/02/2023 || Função para ajudar a Calcular Prefixo
def CalcularPrefixo(pPadrao):
    vPrefixo = [0] * len(pPadrao)
    j = 0

    for i in range(1, len(pPadrao)):
        while j > 0 and pPadrao[j] != pPadrao[i]:
            j = vPrefixo[j-1]
        
        if pPadrao[j] == pPadrao[i]:
            j += 1
        
        vPrefixo[i] = j
    
    return vPrefixo