# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(B):
    destroyer = 0
    submarines = 0
    patrol = 0

    total_linhas = len(B)
    total_colunas = len(B[0])

    def verLinhaToda(B,nlinha,ncoluna):
        # coluna muda
        # linha fixa
        contador_hash = 0
        for c in range(ncoluna,len(B[0])):
            if B[nlinha][c] == ".":
                break
            else:
                contador_hash+=1
            

        return contador_hash

    def verColunaToda(B,nlinha,ncoluna):
        # coluna fixa
        # linha muda
        contador_hash = 0
        for l in range (nlinha,len(B)):
            if B[l][ncoluna] == ".":
                break
            else:
                contador_hash+=1
        return contador_hash




    posicoes_ja_vistas=list()

    '''

    .##.#
    #.#..
    #...#
    #.##.
    
    '''

    for linha in range(0,total_linhas):
        print(B[linha])
        for coluna in range(0,total_colunas):
            
            if [linha,coluna] in posicoes_ja_vistas:
                continue

            if B[linha][coluna] == ".":
                posicoes_ja_vistas.append([linha,coluna])
                continue

            else:
                # FOUND "#"
                posicoes_ja_vistas.append([linha,coluna])

                sumlinha = verLinhaToda(B,linha,coluna)
                
                if sumlinha == 1:
                    sumcoluna = verColunaToda(B,linha,coluna)
                    if sumcoluna == 1:
                        posicoes_ja_vistas.append([linha+1,coluna])
                        patrol+=1
                    
                    if sumcoluna == 2:
                        posicoes_ja_vistas.append([linha+1,coluna])
                        posicoes_ja_vistas.append([linha+2,coluna])
                        d=0
                        if verLinhaToda(B,linha+1,coluna) == 2:
                            # TEM L PADRAO
                            d=1
                            destroyer+=1
                            posicoes_ja_vistas.append([linha+1,coluna+1])
                            posicoes_ja_vistas.append([linha+1,coluna+2])
                        elif verLinhaToda(B,linha+1,coluna) != 2:
                            
                            c=0
                            try: 
                                if B[linha+1][coluna-1] == '#':
                                    c=1
                                    posicoes_ja_vistas.append([linha+1,coluna-1])
                            except: 
                                pass
                            if c==1:
                                destroyer+=1
                                d=1
                        
                        if d==0:
                            submarines+=1


                    if sumcoluna == 3:
                        posicoes_ja_vistas.append([linha+1,coluna])
                        posicoes_ja_vistas.append([linha+2,coluna])
                        posicoes_ja_vistas.append([linha+3,coluna])
                        destroyer +=1
                
                if sumlinha == 2:
                    posicoes_ja_vistas.append([linha,coluna+1])
                    posicoes_ja_vistas.append([linha,coluna+2])
                    if verColunaToda(B,linha,coluna) == 2:
                        destroyer+=1
                        posicoes_ja_vistas.append([linha+1,coluna])
                        posicoes_ja_vistas.append([linha+2,coluna])
                    elif verColunaToda(B,linha,coluna+1) == 2:
                        posicoes_ja_vistas.append([linha+1,coluna+1])
                        posicoes_ja_vistas.append([linha+2,coluna+1])
                        destroyer+=1
                    else:
                        submarines+=1

                if sumlinha == 3:
                    
                    destroyer+=1
                    posicoes_ja_vistas.append([linha,coluna+1])
                    posicoes_ja_vistas.append([linha,coluna+2])
                    posicoes_ja_vistas.append([linha,coluna+3])
                



    return [patrol,submarines,destroyer]



B=[".##.#","#.#..","#...#","#.##."] # has to produce [2,1,2]
#B=[".#..#","##..#","...#."] # has to produce  [1,1,1]
#B=["##.","#.#",".##"] # has to produce  [0,0,2]
#B=["...","...","..."] # has to produce  [0,0,0]





print(solution(B))


