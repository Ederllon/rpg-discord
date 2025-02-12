
# inicio importações

from random import randint
# fim importações

# raise SystemExit("TEST FINISHED!")




# inicio dados                                                                                       
nenhuma = {'nome':'nenhuma', 'dano' : 0, 'defesa': 0, 'critico': 0, }
faca = {'nome':'faca', 'dano' : 2, 'defesa': 1, 'critico': 6, }
bastão = {'nome':'bastão', 'dano' : 3, 'defesa': 5, 'critico': 0, }
espada = {'nome':'espada', 'dano' : 7, 'defesa': 6, 'critico': 10, }
machado = {'nome':'machado', 'dano' : 10, 'defesa': 4, 'critico': 9, }
martelo = {'nome':'martelo', 'dano' : 7, 'defesa': 4, 'critico': 1, }
lança = {'nome':'lança', 'dano' : 6, 'defesa': 5, 'critico': 7,}
escudo = {'nome':'escudo', 'dano' : 2, 'defesa': 50, 'critico': 0, }
bengala = {'nome':'bengala', 'dano' : 1, 'defesa': 3, 'critico': 0, }
manopla = {'nome':'manopla', 'dano' : 2, 'defesa': 10, 'critico': 0, }
chicote = {'nome':'chicote', 'dano' : 2, 'defesa': -90, 'critico': 1, }
canivete = {'nome':'canivete', 'dano' : 3, 'defesa': 0, 'critico': 5, }
machete =  {'nome':'machete', 'dano' : 4, 'defesa': 6, 'critico': 6, }
pá = {'nome':'pá', 'dano' : 3, 'defesa': 4, 'critico': 0, }
foice = {'nome':'foice', 'dano' : 6, 'defesa': 5, 'critico': 6, }
trident = {'nome':'trident', 'dano' : 6, 'defesa': 6, 'critico': 6, }
marreta = {'nome':'marreta', 'dano' : 8, 'defesa': 5, 'critico': 1, }
chave = {'nome':'chave', 'dano' : 0, 'defesa': 0, 'critico': 1, }




magias = ['nenhuma', 'fogo', 'vento', 'terra', 'elétrico', 'água', 'amaldiçoado']
nmagias = magias.__len__() - 1

subna1 = ['al','jam','ada','bal','bel','dan','don','dom','can','chru','pe','a','e','i','o','u','y','oto','shik','Thi','Thy','cha','pe','si','sil','sh','ko','no','ha','kyo','za','mu','yu','ri','yuri','yuta','shi','ra','ryu','shira','ka','orochi','maru','ki']
subna2 = ['al','jam','ada','bal','bel','dan','don','dom','can','chru','pe','','k','th','ph','oto','ha','cha','dro','si','sil','va','','','','','ko','sh','ap','ko','no','ha','maru','kyo','za','moth','mu','yu','ri','yuri','yuta','shi','ra','ryu','shira','ka','orochi','maru','ki']
subna3 = ['al','jam','ada','bal','bel','dan','don','dom','can','chru','pe','','','k','th','ph','a','e','i','o','u','y','te','maru','ha','cha','si','sil','','','ko','sh','ap','kyo','ko','no','ha','maru','za','moth','mu','yu','ri','yuri','yuta','shi','ra','ryu','shira','ka','orochi','maru','ki']




# fim dados

# incio funções
def nameGen(pri, sec, trh, rvalue ):
    print('Herança: {} | Afiliação: {}'.format(rvalue,str(subna1[pri]).capitalize()+subna2[sec]+subna3[trh]))

def ficha(x):
    hp = int(randint(1,100))
    atk = int(randint(1,100))
    df = int(randint(1,100))
    spd = int(randint(1,100))
    car = int(randint(1,100))
    man = int(randint(1,100))
    magperc = int(randint(1,100))
    maestria = int(randint(1,100))
    luck = int(randint(1,100))
    prec = int(randint(1,100))
    riq = int(randint(0,100))
    




# inicio dados com adicionaveis     


    anel = {'nome':'anel do poder', 'dano' : magperc, 'defesa': man, 'critico': maestria, }
    chaveg = {'nome':'arco', 'dano' : 2, 'defesa': 5, 'critico': prec-1,}
    arco = {'nome':'arco', 'dano' : 3, 'defesa': 1, 'critico': prec, }
    cajado = {'nome':'cajado', 'dano' : int((magperc + maestria)/2), 'defesa': man, 'critico': maestria, }
    anel_de_energia = {'nome':'anel de energia', 'dano' : man, 'defesa': man, 'critico': man, }
    sai = {'nome':'sai', 'dano' : 2, 'defesa': 2, 'critico': spd, }
    soco = {'nome':'soco inglês', 'dano' : atk , 'defesa': df-30, 'critico': -1 }
    luva = {'nome':'luvas', 'dano' : 1, 'defesa': 1, 'critico': atk-50,}
    pedra = {'nome':'pedra', 'dano' : atk-prec, 'defesa': 0, 'critico': prec, }
    kunai = {'nome':'kunai', 'dano' : (spd+prec-30), 'defesa': 2, 'critico': (spd+prec-10), }
    shk = {'nome':'shiruken', 'dano' : (prec-50), 'defesa': -1, 'critico': 0, }
    livroDatabase = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

    livroRand = randint(0,len(livroDatabase))
    if livroRand > 0:
        livroRand = livroRand - 1 
    else:
        livroRand = 0

    if livroRand == 0:
        livro = {'nome': 'livro comum' , 'dano' : 0, 'defesa': 0, 'critico': (man-10),}
    else:
        if livroRand == 1:
            livro = {'nome': 'livro de magia negra' , 'dano' : 2, 'defesa': 1, 'critico':1,}
        else:
            if livroRand == 2:
                livro = {'nome': 'livro de humor/comedia' , 'dano' : 0, 'defesa': car, 'critico':car,}
            else:
                if livroRand == 3:
                    livro = {'nome': 'livro de romance' , 'dano' : 0, 'defesa': 0, 'critico':(hp+car-10),}
                else:
                    if livroRand == 4:
                        livro = {'nome': 'livro de suspense' , 'dano' : (2+spd-car), 'defesa': 2, 'critico':(spd-car),}
                    else:
                        if livroRand == 5:
                            livro = {'nome': 'livro de magia' , 'dano' : (man-25), 'defesa': man , 'critico':(man+car),}
                        else:
                            if livroRand == 6:
                                livro = {'nome': 'livro de druida' , 'dano' : (car-25), 'defesa': car, 'critico':car,}
                            else:
                                if livroRand == 7:
                                    livro = {'nome': 'livro de necromantico' , 'dano' : (100-car), 'defesa': (100-hp-man), 'critico':0,}
                                else:
                                    if livroRand == 8:
                                        livro = {'nome': 'livro de paladino' , 'dano' : (100-atk), 'defesa': (df+car), 'critico':car,}
                                    else:
                                        if livroRand == 9:
                                            livro = {'nome': 'livro de caça' , 'dano' : (atk+df-car), 'defesa': 0, 'critico':10,}
                                        else:
                                            if livroRand == 10:
                                                livro = {'nome': 'livro guia de arte marciais' , 'dano' : (atk-50), 'defesa':(df+25-atk) , 'critico':0,}
                                            else:
                                                if livroRand == 11:
                                                    livro = {'nome': 'diario pessoal' , 'dano' : (car-50), 'defesa': (car-100), 'critico':0,}
                                                else:
                                                    if livroRand == 12:
                                                        livro = {'nome': 'livro de caça' , 'dano' : luck, 'defesa': (luck+car), 'critico':luck,}
                                                    else:    
                                                        if livroRand == 13:
                                                                livro = {'nome':'livro do heroi', 'dano' : (car-75), 'defesa': (df+car), 'critico': 0, }
                                                        else:
                                                            if livroRand == 14:
                                                                livro = {'nome':'livro do vilão', 'dano' : (10+atk-car), 'defesa': (df-car), 'critico': (100-car), }
                                                            else:
                                                                if livroRand == 15:
                                                                     livro = {'nome':'livro de receitas', 'dano' : 0, 'defesa': 0, 'critico': 1, }
                                                                else:
                                                                    if livroRand == 16:
                                                                        livro = {'nome':'livro +18', 'dano' : 0, 'defesa': 0, 'critico': 1, }
                                                                    else:
                                                                        if livroRand == 17:
                                                                            livro = {'nome':'livro guia do arqueiro', 'dano' : 0, 'defesa': 0, 'critico': 100, }
                                                                        else:
                                                                            if livroRand == 18:
                                                                                livro = {'nome':'livro dos elfos', 'dano' : 0, 'defesa': (man-5), 'critico': 90, }
                                                                            else:
                                                                                if livroRand == 19:
                                                                                    livro = {'nome':'livro satanico', 'dano' : (100-car), 'defesa': -100, 'critico': 0, }  
                                                                                else:
                                                                                    if livroRand == 20:      
                                                                                        livro = {'nome':'livro religioso', 'dano' : 0, 'defesa': int((man)-(man/5+(5))), 'critico': 0, }



                                                            

                                                
  
    style_fightDatabase = [1,2]            
    style_fightRandom = randint(1,len(style_fightDatabase)) 
    print(style_fightRandom)
    if style_fightRandom == 1:
        style_fight = {'nome':'estilo de luta karate', 'dano' : int((spd+atk- man)) , 'defesa': int(df/10), 'critico': 0, }
    else:
        if style_fightRandom == 2:
            style_fight = {'nome':'estilo de luta boxe', 'dano' : spd+atk-car-25, 'defesa': df, 'critico': 0, }


# fim dados com adicionaveis
    
    # inicio dados insert 
    armas = [nenhuma,kunai, shk, faca, bastão, sai,pedra, luva, cajado, espada, arco, machado, martelo, soco, lança, escudo, bengala, manopla, chicote, canivete, machete, pá, foice, marreta , anel, anel_de_energia, chave, chaveg, livro, style_fight,]
    
    narmas = armas.__len__() - 1
    # fim dados insert
    mag = int(randint(0,nmagias))
    arm = int(randint(0,narmas))

    if mag == 0:
        magperc = 0

      
    
    newRandArm =  armas[arm]
    
    if newRandArm["nome"] == "nenhuma":
        maestria = 0

    if magias[mag] == 'amaldiçoado':
        print(' Ficha: #{} | Média De Poder: {}'.format(x,  int((hp+atk+df+spd+car+man+maestria+magperc+luck+prec+riq)/11-(magperc/11))))
    else:
        print(' Ficha: #{} | Média De Poder: {}'.format(x,  int((hp+atk+df+spd+car+man+maestria+magperc+luck+prec+riq)/11)))
    print('Vida:',hp)
    print('Força:',atk)
    print('Defesa:',df)
    print('Velocidade:',spd)
    print('Carisma:', car)
    print('Precisão: ', prec)
    print('Sorte: ', luck)
    print('Mana:', man)
    print('Magia:', magias[mag])
    print('Maestria da Magia: {}%'.format(magperc))
    print('Arma:', newRandArm)
    print('Maestria da Arma: {}%'.format(maestria))
    nameGen(randint(0,int(len(subna1)-1)),randint(0,int(len(subna2)-1)),randint(0,int(len(subna3)-1)),riq)   
    print(62*'-')

# fim funções
    
# inicio body
    
while True:

    print('')
    rodadas = int(input('Quantas fichas irão ser criadas? '))
    print('')
    vezes = rodadas
    
    for count in range(0,vezes):
        ficha(count+1)     

    retry = str(input('Deseja finalizar o programa? '))    
    if retry in  ['s']:
        print('')
        print('Programa finalizado! ')
        print('')
        break


# fim body 
