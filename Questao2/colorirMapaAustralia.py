# Definindo os estados e suas adjacências
listaEstados = {
    'Western Australia': ['Northern Territory', 'South Australia'],
    'Northern Territory': ['Western Australia', 'South Australia', 'Queensland'],
    'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
    'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
    'New South Wales': ['South Australia', 'Queensland', 'Victoria'],
    'Victoria': ['South Australia', 'New South Wales'],
    'Tasmania': []
}

# Definindo as possíveis cores
listaCores = ['rosa', 'amarelo', 'branco']

# Inicializando o mapa de cores
mapaCores = {}
for estado in listaEstados:
    mapaCores[estado] = None

def validarCor(estado, cor):
    """Verifica se a cor pode ser atribuída ao estado sem conflitar com as cores dos estados vizinhos"""
    for vizinho in listaEstados[estado]:
        corVizinho = mapaCores[vizinho]
        if corVizinho == cor:
            return False
    return True

def obterProximoEstado():
    """Obtém o próximo estado não colorido"""
    for estado in listaEstados:
        if mapaCores[estado] is None:
            return estado
    return None

def colorirEstado(estado):
    """Tenta atribuir uma cor ao estado atual e prossegue para o próximo estado"""
    # Se já colorimos todos os estados, então encontramos uma solução
    if estado is None:
        print(mapaCores)
        return
    # Tenta cada cor
    for cor in listaCores:
        if validarCor(estado, cor):
            # Se a cor é válida, a atribui ao estado
            mapaCores[estado] = cor
            # Pega o próximo estado que ainda não foi colorido
            proximoEstado = obterProximoEstado()
            # Recursivamente tenta colorir o restante do mapa
            colorirEstado(proximoEstado)
            # Se chegamos a este ponto, então a cor atual não levou a uma solução, então a remove
            mapaCores[estado] = None

# Começa a colorir pelo primeiro estado
primeiroEstado = obterProximoEstado()
colorirEstado(primeiroEstado)