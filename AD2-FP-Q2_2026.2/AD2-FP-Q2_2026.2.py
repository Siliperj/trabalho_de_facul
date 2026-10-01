# Analizar o arquivo
def analisar_teste(arquivo_lesma):

    while True:      
    
        quantidade_lesmas = arquivo_lesma.readline()

        if quantidade_lesmas == "":
        
            break 

        quantidade_lesmas = int(quantidade_lesmas)

        velocidade_lesmas = list(map(int, arquivo_lesma.readline().strip().split()))

        lesma_lv = nivel_lesmas(velocidade_lesmas)

        analise_lesma(lesma_lv)



    

# Nivel das lesmas
def nivel_lesmas(velocidade_lesmas):

    lesma_lv = [0] * len(velocidade_lesmas)

    for i in range(len(velocidade_lesmas)):
            
        if velocidade_lesmas [i] < 10:
           
                lesma_lv [i] = 1
            
        elif velocidade_lesmas [i] >= 10 and velocidade_lesmas [i] < 20:
            
                lesma_lv [i] = 2
            
        else:
            
                lesma_lv [i] = 3

    
    return lesma_lv





# Media das lesmas
def analise_lesma(nivel_lesmas):

    media_lesmas = sum(nivel_lesmas) / len(nivel_lesmas)
    
    maior_nivel = max(nivel_lesmas)

    menor_nivel = min(nivel_lesmas)

    print (f"{media_lesmas:.2f} {maior_nivel} {menor_nivel}")




    
# Programa principal
def main():

    with open("lesmas.txt", "r", encoding="utf-8") as arquivo_lesma:

        analisar_teste(arquivo_lesma)

main()