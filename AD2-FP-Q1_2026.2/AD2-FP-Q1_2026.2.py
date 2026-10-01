# AD1-FP-Q1

# lista de clientes
def fila_clientes(clientes, inv_cli):
    
    listaClientes = [0] * clientes
    
    for i in range(clientes):
        
        listaClientes[i] = inv_cli[i]
    
    return ordenação_cliente(listaClientes)





# ordenar clientes
def ordenação_cliente (listaCliente):

    for i in range(len(listaCliente)):
        
        for j in range(i + 1, len(listaCliente)):
            
            if listaCliente[i] > listaCliente[j]:
            
                listaCliente[i], listaCliente[j] = listaCliente[j], listaCliente[i]
    
    return listaCliente





# lista de funcionários
def caixas_disponiveis(funcionarios, cooldown_func, listaClientes):
    
    listaFuncionarios = [0] * funcionarios
    
    for i in range(funcionarios):
        listaFuncionarios[i] = cooldown_func[i]

    return funcionario_disponivel(listaFuncionarios, listaClientes)





# descobrir qual funcionário fica disponível primeiro
def funcionario_disponivel(listaFuncionarios, listaClientes):

    tempo_livre = [0] * len(listaFuncionarios)

    for i in range(len(listaClientes)):

        listaFuncionario = tempo_livre.index(min(tempo_livre))
    
        tempo_livre[listaFuncionario] += listaFuncionarios[listaFuncionario] * listaClientes[i]
   
    return max(tempo_livre)


# programa todo
def main():
    
    clientes, funcionarios = map(int,input("Quantos clientes serão atendidos? E quantos funcionarios estão disponiveis? ").split(),)
    
    cooldown_func = list(map(int, input("Digite o tempo por item cada funcionário leva respectivamente: ").split()))
    
    inv_cli = list(map(int, input("Digite quantos itens cada cliente possui: ").split()))
    
    listaClientes = fila_clientes(clientes, inv_cli)
    
    tempo_total = caixas_disponiveis(funcionarios, cooldown_func, listaClientes)
    
    print("O tempo total para atender todos os clientes é: ", tempo_total)

    main()