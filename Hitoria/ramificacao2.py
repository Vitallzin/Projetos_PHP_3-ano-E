import time
import sys
def pausa(mensagem, velocidade=1):
    for letra in mensagem:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)

def texto_superlento(mensagem, velocidade=0.7):
    for letra in mensagem:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    
def texto_lento(mensagem, velocidade=0.08):
    for letra in mensagem:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
     
def texto_normal(mensagem, velocidade=0.05):
    for letra in mensagem:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    
def texto_rapida(mensagem, velocidade=0.01):
    for letra in mensagem:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)

#Caminho para o final com a Rafaela e distante de Lucas
texto_normal("\nVocê e Lucas começam a correr, conseguem sair da sala e vão em direção a \x1b[1mALA PEDIATRICA E CIRÚRGICA\x1b[0m  ")
texto_normal("\nEnquanto correm, percebem que Rafaela não está com vocês")
#texto_normal("\nO caminho até o hospital não foi longo, mas pareceu uma eternidade. À medida que vocês se afastavam da cidadeas ruas de terra e a luz fraca das")
texto_normal("\nVocê e Lucas correm desesperadamente pelos corredores escuros do hospital, a respiração ofegante e o medo consumindo cada passo. O som de passos atrás")
texto_normal("\nde vocês parece crescer a cada instante, o monstro se aproximando com velocidade O grito de Rafaela ressoa pelo corredor, uma mistura de desespero e dor")
texto_normal("\nfazendo seu estômago se revirar."),pausa(" ")
texto_normal("Você nota que a porta está meio aberta e pressupõe que possa ter sido Lucas."),pausa(" ")
texto_normal("\nLucas havia sumido muito antes, correndo apavorado para algum lugar desconhecido. Rafaela, por outro lado"),texto_superlento("..."),texto_normal("ela não conseguiu escapar. O monstro")
texto_normal("\na alcançou antes que ele pudesse fazer algo. O último grito dela ainda ecoava em sua mente, misturado à culpa esmagadora de ter fugido enquanto")
texto_normal("\nela era dilacerada."),pausa(" ")
texto_normal("\nA escuridão tomava conta do hospital. O som de seus passos ecoava pelos corredores desertos, interrompidos apenas pelo gotejar incessante da")
texto_normal("\nchuva que agora caía do lado de fora.")
texto_normal("\nnAgora Você encontrava no meio do corredor principal"),pausa(" "),print()
print("       |                            |")
print("       |          Ala               |")
print("       |        Pediátrica          |")
print("       |                            |")
print("_______|                            |_______________________")
print("\x1b[31m]\x1b[0m                                                            ")
print("\x1b[31m]\x1b[0m                                                            ")
print("\x1b[31m]\x1b[0m                        Você                              ")
print("\x1b[31m]\x1b[0m                          o                                ")
print("\x1b[31m]\x1b[0m_______                             _______________________")
print("       |                            |")
print("       |                            |")
print("       |           Ala              |")
print("       |        Cirúrgica           |")
print("       |                            |")
print("       |                            |"),print()
texto_normal("Três placas iluminadas por uma luz trêmula indicavam os caminhos restantes:")
print("                                                             "), texto_superlento("Salvando..."), print()
while True:
    texto_normal("\nEm frente: Saída.  A direita: Ala Pediátrica. A esquerda: Ala Cirúrgica")
    texto_normal("\nQual caminho você vai seguir primeiro?")
    print("\n1. Saída\n2. Ala Pediátrica\n 3. Ala Cirúrgica")
    caminho4 = int(input("> "))

    if caminho4 == 1:
        while True:
            texto_normal("Ao conferir a porta que leva a saída, percebe que está trancada com correntes e um grande cadeado resistente.")
            break
    elif caminho4 == 2:
        while True:
            texto_normal("Ao conferir a porta que leva a Ala Pediátrica, percebe que a porta está trancada.")
            break
    else:
     while True:
        while True:
            texto_normal("\nO corredor estava úmido e frio, o cheiro forte de álcool e ferrugem impregnava o ar. Portas de salas de cirurgia estavam entreabertas, revelando")
            texto_normal("\nmacas abandonadas e instrumentos enferrujados espalhados pelo chão."),pausa(" ")
            texto_normal("\nNo fim do corredor, Vocês acabam encontrando um \x1b[31mcorpo\x1b[0m ou o que restava dele. Um jaleco ensanguentado indicava que a vítima era um médico. A garganta")
            texto_normal("\nhavia sido rasgada, e os olhos estavam congelados em um olhar de horror absoluto. Em seu jaleco tinha escrito \x1b[3m'Pediatra'\x1b[0m"),pausa(" ")
            texto_normal("\nNa mesa perto do corpo, vocês encontram uma chave."), texto_lento("Mas"),texto_superlento("..."),texto_rapida("*CRIC*"),pausa(" ")
            texto_normal("\nVocês escutam um som de vidro sendo pisado em uma das salas, perto de vocês tem alguns armários"),pausa(" "),print()
            texto_normal("\nO que vai fazer?")
            print("\n1. Pegar a chave e se esconder no armário\n2. Se esconder no armário sem se preocupar com a chave\n3. Pegar a chave e correr"),print()
            caminho5 = int(input("> "))

                        #Morte
            if caminho5 == 1:
                texto_normal("\nVocê se esconde dentro do armário, respirando pesado enquanto tenta controlar o nervosismo. Através de uma pequena fresta, consegue enxergar ")
                texto_normal("\numa figura. A criatura é um homem alto e esquelético, vestido com um avental médico ensanguentado. Sua pele parece pálida e doentia, os olhos")
                texto_normal("\nfundos e opacos, como se já tivesse perdido qualquer vestígio de humanidade. Em suas mãos, um bisturi longo e serrilhado reflete a luz fraca")
                texto_normal("\ndo corredor. Ele anda lentamente, arrastando os pés pelo chão sujo, como se estivesse caçando algo"),texto_superlento("..."),texto_normal("ou alguém.")
                texto_normal("\nSeu coração dispara. Suas mãos tremem e, sem querer, você solta a chave que segurava. O som metálico ecoa pelo ambiente, rompendo o silêncio sufocante.")
                texto_normal("\nO monstro para abruptamente. Sua cabeça se vira bruscamente em direção ao armário.")
                texto_normal("\nPor um instante, nada acontece."),pausa(" "),texto_normal("Então, em um movimento grotesco e veloz, ele avança.")
                texto_normal("\nO armário é arrancado do lugar com força descomunal. Você tenta reagir, mas não há tempo. A lâmina fria corta sua pele antes mesmo de conseguir gritar.")
                texto_normal("\n Seu corpo é puxado brutalmente para fora, e a última coisa que vê é o brilho distorcido do bisturi descendo em sua direção"),texto_superlento("... "),pausa(" "),print()
                texto_lento("\n\x1b[31mGame Over...\x1b[0m"),print()
                pausa("  ")
                print("                                                             "), texto_lento("Carregando último checkpoint"),texto_superlento("..."),pausa("  "), print()
                break
            #caminho para o fim com Lucas
            elif caminho5 == 2:
                
                texto_normal("\nVocê se esconde no armário, prendendo a respiração enquanto observa pela fresta. O monstro caminha lentamente pela sala, seus passos ecoando no chão frio.")
                texto_normal("\nA criatura parece procurar algo, movendo a cabeça de um lado para o outro. Seus olhos fundos percorrem o ambiente, e por um momento, ele para bem diante do")
                texto_normal("\nseu esconderijo. O silêncio é insuportável.")
                texto_normal("\nSeu coração martela no peito, mas você se mantém imóvel. Depois de alguns segundos angustiantes, o monstro se afasta, rondando o local. Ele ainda está ali"),texto_superlento("..."),texto_normal("esperando.")
                texto_normal("\nVocê consegue escutar ele entrando em alguma sala e agora é a sua chance e pega a chave."),pausa(" "),texto_normal("Andando lentamente pelo corredor, Lucas aparece saindo de uma sala."),pausa(" ")
                texto_normal("\nA sua cara é de alívio, mesmo tenso e se tremendo, Você mostra a chave para ele e seguem a diante."),pausa(" ")
                texto_normal("\n Lucas:Essa chave deve ser da Ala pedriática, a chave da saída deve ser maior."),texto_lento("   Ele cochihca"),pausa(" ")
                texto_normal("\nEntrando na Ala, se movem lentamente, os passos ecoando nos corredores forrados com murais infantis desgastados pelo tempo. Bonecas quebradas estavam")
                texto_normal("\nespalhadas pelo chão, olhos de plástico olhando para ele no escuro."),pausa(" ")

                texto_normal("\n Lucas:Aannn"),texto_superlento("..."),texto_normal("Cadê a Rafaela?"),print()
                print("1. ...\n 2. Ela... Você sabe...\n 3. Eu não tinha o que fazer, o monstro acabou pegando ela..."),print()
                resposta2 = int(input("> "))
                if resposta2 == 1:
                    texto_normal("\n Lucas: Entendo"),texto_superlento("..."),texto_normal(" Vamos tentar escapar desse maldito lugar!"),pausa(" "),print()
                elif resposta2 == 2:
                    texto_normal("\n Lucas: Desculpa"),texto_superlento("..."),texto_normal(" Depois lamentamos, vamos tentar sair daqui!"),pausa(" "),print()
                else:
                    texto_normal("\n Lucas: Não se sinta culpado."),pausa(" "),texto_normal("Eu que fugi na situação"),texto_superlento("..."),texto_normal(" Vamos sair daqui!"),pausa(" "),print()

                texto_normal("\nNo fim do corredor, vocês encontram uma sala de enfermaria. O vidro da janela estava rachado e a cama, coberta de poeira e manchas escuras.")
                texto_normal("\nVocê se aproxima da porta e percebe um papel amassado no chão."),pausa(" ")
                texto_normal("\n\x1b[3m'Os testes foram um fracasso. Paciente 12 entrou em frenesi e eliminou toda a equipe da ala médica. Apenas o Sujeito Zero permaneceu"),texto_superlento("...")
                texto_normal("\nmas ele também está mudando. Não há mais esperança de contê-los.'\x1b[0m"),pausa(" ")
                
                print("\n                                                   Enfermaria     ")
                print("______________________________________________________------_____ ")
                print("                                                                 |")
                print("    Corredor                                         Vocês       |")
                print("     Escuro                                            o         |")
                print(" ______________________________________                          |")
                print("                                      |                          |")
                print("                                      |                          |")
                print("                                      |                          |")
                print("                                      |                          |")
                print("                                      |                          |"),print()
                
                texto_normal("\n Lucas: Vai entrar na enfermaria ou adentrar nesse corredor?"),pausa(" "),print()
                print("\n1. Vamos explorar na enfermaria\n2. Vamos para o corredor, temos que sair daqui logo"),print()
                escoolha22 = int(input("> "))

                # Finais da saída principal
                if escoolha22 == 1:
                    texto_normal("\nEnquanto exploravam a enfermaria, Lucas chutou algo metálico no chão. O som ecoou pelo corredor vazio, fazendo os dois prenderem a respiração")
                    texto_normal("\npor um instante.")
                    texto_normal("\nEle abaixou e pegou o objeto:"),pausa(" "),texto_normal("um pé de cabra, enferrujado e frio ao toque"),pausa(" "),print ()
                    texto_normal("\n Lucas:  Isso pode ser útil"),texto_superlento("..."),texto_normal(" Mas é claro, isso pode servir para a porta da saída"),pausa(" "),print()
                    texto_normal("\nDe forma sutil e rápida, eles saem da enfermaira e vão em direção a saída, mas"),texto_superlento("..."),texto_normal("Ao chegarem um pouco perto")
                    texto_normal("\nda porta da entrada da ala pediátrica"),pausa(" "),texto_normal("as fracas luzes se apagam e as lanternas começam a falhar"),pausa("  "),print()
                    texto_rapida("\n *PAAAAAAAM* "),pausa(" "),print()
                    texto_normal("\nVocês se assustam com o barulho repentino, e as luzes piscam, voltando de forma abrupta. Quando a luz se estabiliza"),pausa(" ")
                    texto_normal("\na figura da ala cirúrgica está bem na sua frente, coma cara toda desfigurada e com um sorrisop macabro"),texto_superlento("..."),print()

                    texto_lento("\nQual a sua reação?")
                    print("\n1. Ir para cima do monstro junto com Lucas\n2. Tentar distrair ele para que Lucas possa fugir\n3. Esperar a reação de Lucas"),print()
                    final12 = int(input("> "))

                    #Final junto com Lucas
                    if final12 == 1:
                        
                        texto_normal("\nVocê e Lucas não pensam duas vezes. Sabem que é a última chance. Com coragem renovada, ambos partem para cima do monstro, tentando pegá-lo de surpresa.")
                        texto_normal("\nO bicho se agita, mas vocês conseguem derrubá-lo, sua força combinada sendo o suficiente para imobilizá-lo por um momento. Com a criatura fora de")
                        texto_normal("\ncombate, vocês correm até a porta da saída, Lucas quebra o cadeado e a porta se abre.")
                        texto_normal("\nO corredor estreito à frente é quase claustrofóbico. Vocês não perdem tempo e viram à esquerda, encontrando uma porta de emergência, a última barreira")
                        texto_normal("\nentre vocês e a liberdade. Com um empurrão, a porta se abre, revelando o estacionamento lá fora, iluminado apenas pelas luzes fracas de alguns postes")
                        texto_normal("\ndistantes.")
                        texto_normal("\nFinalmente, respiram o ar fresco da noite. A fuga está completa, mas a sensação de perda é inevitável."),pausa("   "),print()
                        texto_lento("\n\x1b[1mEpílogo:\x1b[0m"),print()
                        texto_normal("\n\x1b[36mRafaela não teve a mesma sorte. A coragem de Lucas e sua própria determinação foram essenciais para a fuga, mas a amiga deles não conseguiu sobreviver àquele")
                        texto_normal("\nmonstro. O silêncio é pesado, e a culpa aperta o peito enquanto você e Lucas olham para trás, sabendo que, por mais que a liberdade tenha sido conquistada")
                        texto_normal("\n\x1bo custo foi alto.\x1b[0m"),pausa("  "),print()
                        texto_normal("\n\x1b[32mFinal: Fuga Sombriamente Vitoriosa\x1b[0m"),pausa("         ")
                        sys.exit()

                    #Final onde o protagonista se sacrifica:   
                    elif final12 == 2:
                        
                        texto_normal("\nVocê e Lucas sabem que a única maneira de escapar é distraindo o monstro, mas a tensão no ar é insuportável. Olhando ao redor, você percebe que a única")
                        texto_normal("\nchance é usar o ambiente a seu favor."),pausa(" ")
                        texto_normal("\nCom um movimento rápido, você pega uma garrafa quebrada no chão e faz um barulho estridente ao jogá-la contra a parede. O monstro, atraído pelo som")
                        texto_normal("\nvira a atenção para o lado oposto, deixando você com uma brecha de tempo para agir."),print()
                        texto_normal("\n Você: Vai, Lucas!"),pausa(" "),texto_lento("AGORA!!"),pausa(" "),print()
                        texto_normal("\nLucas não hesita. Ele corre para a porta de emergência, passando por você com rapidez. O monstro ainda está distraído  mas você sabe que é uma questão")
                        texto_normal("\nde tempo até ele voltar a te notar."),pausa(" "),texto_lento("Você respira fundo"),pausa(","),texto_normal("preparado para o sacrifício. Quando o monstro percebe que você não está mais ali, ele se vira"),pausa("  ")
                        texto_normal("\nmas já é tarde demais. Você está de pé, fazendo de tudo para mantê-lo ocupado, enquanto Lucas, finalmente, alcança a liberdade."),pausa("  "),print()
                        texto_lento("\n\x1b[1mEpílogo:\x1b[0m"),print()
                        texto_normal("\n\x1b[36mLucas consegue sair, mas você não tem a mesma sorte. No último momento, a criatura te alcança, e tudo o que resta é o som abafado do monstro")
                        texto_normal("\nse aproximando. Ele finalmente escapou, mas o custo foi a sua vida. Quando Lucas olha para trás, só vê a escuridão — e a lembrança de um sacrifício que")
                        texto_normal("\nele nunca esquecerá.\x1b[0m"),pausa("  "),print()
                        texto_normal("\n\x1b[32mFinal: Sacrifício Pela Liberdade\x1b[0m"),pausa("         ")
                        sys.exit()
                    else:
                        texto_normal("\nVocê e Lucas estão no corredor, a criatura se aproximando rapidamente. A porta de saída está ali, ao alcance das mãos  mas você sabe que não será possível")
                        texto_normal("\nos dois escaparema tempo. O pânico toma conta de você, mas você não consegue agir. Apenas olha para Lucas, esperando que ele tome uma decisão.")
                        texto_normal("\nLucas, com os olhos fixos na porta, vê a mesma realidade que você, a única chance é uma pessoa. Ele percebe que você não reagiu e, com um olhar firme, toma")
                        texto_normal("\na frente."),pausa(" "),print()
                        texto_normal("\n Lucas: Vai, corre!"),pausa("  "),texto_normal("Eu vou distrair ele."),pausa(" "),print()
                        texto_normal("\nVocê não diz nada. A resposta está em seus olhos, mas Lucas já se adianta. Ele se joga na direção do monstro, fazendo o máximo de barulho possível, tentando")
                        texto_normal("\ndesviar a atenção da criatura para si. O monstro se vira imediatamente, fixando-se nele, e você fica parado, assistindo ao sacrifício sem poder reagir."),pausa(" ")
                        texto_normal("\nCom uma última troca de olhares, Lucas te garante a fuga. Você corre para a porta de emergência e, ao olhar para trás, vê a sombra dele sendo engolida pela escuridão")
                        texto_normal("\nsabendo que ele fez isso por você."),pausa("  "),print()
                        texto_lento("\n\x1b[1mEpílogo:\x1b[0m"),print()
                        texto_normal("\n\x1b[36mVocê escapa, finalmente respirando o ar fresco da noite. Mas a vitória tem um gosto amargo. Lucas não conseguiu sair. Quando você olha para trás, a única coisa que vê")
                        texto_normal("\n\x1bé a porta que ele ficou para trás. Seu sacrifício não será esquecido.[0m"),pausa("         ")
                        texto_normal("\n\x1b[32mFinal: O Último Sacrifício\x1b[0m"),pausa("         ")
                        sys.exit()

            #final diferente
            else:
               #texto_normal("\nO caminho até o hospital não foi longo, mas pareceu uma eternidade. À medida que vocês se afastavam da cidadeas ruas de terra e a luz fraca das")
                texto_normal("\nVocê pega a chave e começa a correr a todo vapor, o som dos seus passos ecoando pelos corredores escuros e vazios. A ala pediátrica está logo ali")
                texto_normal("\na porta à frente se tornando um farol de esperança. Mas, de repente, o som pesado e arrastado do monstro se aproxima com força. Você pode ouvi-lo,")
                texto_normal("\nmuito mais perto agora."),pausa(" ")
                texto_normal("\nLucas olha para trás, e seu rosto se contorce de pavor ao ver a figura horrível do monstro logo atrás, com garras afiadas e olhos que parecem brilhar")
                texto_normal("\nna escuridão. Ele acelera os passos, mas é tarde demais."),pausa(" ")
                texto_normal("\nO monstro agarra Lucas pelo braço com uma força brutal, fazendo-o parar abruptamente. Você escuta o grito de dor e pavor  mas não pode parar.")
                texto_normal("\nLucas, com uma expressão de desespero, olha para você e grita:"),pausa(" "),print()
                texto_normal("\n Lucas: VAI!"),pausa(" "),texto_normal("Não olhe para trás! Eu seguro ele!"),pausa(" "),print()
                texto_normal("\nSem hesitar, você corre em direção à ala pediátrica, sem ousar olhar para trás. Lucas luta, tentando se desvencilhar, mas sabe que está preso.")
                texto_normal("\nO som de garras raspando na parede e o grito de Lucas ecoam enquanto você corre, mas você não pode parar."),pausa(" ")
                texto_normal("\nA porta da ala se fecha atrás de você com um estrondo, e, mesmo com o coração pesado, você sabe que não pode mais fazer nada. O silêncio que se segue")
                texto_normal("\n é ensurdecedor, e o som dos gritos de Lucas começa a desaparecer à medida que você se afasta."),pausa(" ")
                texto_normal("\nEntrando na Ala, se move lentamente, os passos ecoando nos corredores forrados com murais infantis desgastados pelo tempo. Bonecas quebradas estavam")
                texto_normal("\nespalhadas pelo chão, olhos de plástico olhando para ele no escuro."),pausa(" ")
                texto_normal("\nNo fim do corredor, você encontra uma sala de enfermaria. O vidro da janela estava rachado e a cama, coberta de poeira e manchas escuras.")
                texto_normal("\nVocê se aproxima da porta e percebe um papel amassado no chão."),pausa(" ")
                texto_normal("\n\x1b[3m'Os testes foram um fracasso. Paciente 12 entrou em frenesi e eliminou toda a equipe da ala médica. Apenas o Sujeito Zero permaneceu"),texto_superlento("...")
                texto_normal("\nmas ele também está mudando. Não há mais esperança de contê-los.'\x1b[0m"),pausa(" ")
                
                print("\n                                                   Enfermaria     ")
                print("______________________________________________________------_____ ")
                print("                                                                 |")
                print("    Corredor                                         Vocês       |")
                print("     Escuro                                            o         |")
                print(" ______________________________________                          |")
                print("                                      |                          |")
                print("                                      |                          |")
                print("                                      |                          |")
                print("                                      |                          |")
                print("                                      |                          |"),print()
                
                texto_normal("\nQual a sua escolha?"),pausa(" "),print()
                print("\n1. Explorar a enfermaria \n2. Seguir o corredor escuro"),print()
                escoolha11 = int(input("> "))

                if escoolha11 == 1:
                   #texto_normal("\nO caminho até o hospital não foi longo, mas pareceu uma eternidade. À medida que vocês se afastavam da cidadeas ruas de terra e a luz fraca das")
                    texto_normal("\nEnquanto você explora a enfermaria, os restos do passado ainda estão espalhados por todo o lugar. Camas enferrujadas, lençóis embolorados e armários")
                    texto_normal("\ndestruídos preenchem o ambiente com um cheiro de poeira e abandono.Seu olhar percorre o local até que algo chama sua atenção no canto de uma prateleira")
                    texto_normal("\ncaída."),pausa(" ")
                    texto_normal("\nAo se aproximar, percebe um objeto metálico entre os escombros. Você o puxa para fora e vê que é um pé de cabra enferrujado, mas ainda firme o suficiente")
                    texto_normal("\npara ser útil. egurando-o com força, uma sensação estranha percorre seu corpo. Algo lhe diz que essa ferramenta pode ser sua única chance de sair vivo daqui."),pausa(" ")
                    texto_normal("\nVocê sai da enfermaria e agora tem duas escolhas"),pausa(" "),print()
                    print("\n                                                   Enfermaria     ")
                    print("______________________________________________________------_____ ")
                    print("                                                                 |")
                    print("    Corredor                                         Vocês       |")
                    print("     Escuro                                            o         |")
                    print(" ______________________________________                          |")
                    print("                                      |                          |")
                    print("                                      |                          |")
                    print("                                      |           Voltar         |")
                    print("                                      |             ↓            |")
                    print("                                      |                          |"),print()
                    
                    texto_normal("\nQual a sua escolha?"),pausa(" "),print()
                    print("\n1. Voltar \n2. Seguir o corredor escuro"),print()
                    escoolha33 = int(input("> "))

                    #final macabro
                    if escoolha33 == 1:
                        pass
                    #final diferente o jogador vai enfretar, esquivar ou voltar
                    else:
                        pass
                