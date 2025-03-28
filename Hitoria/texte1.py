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


while True:
    while True:
        texto_normal("\nO corredor estava úmido e frio, o cheiro forte de álcool e ferrugem impregnava o ar. Portas de salas de cirurgia estavam entreabertas, revelando")
        texto_normal("\nmacas abandonadas e instrumentos enferrujados espalhados pelo chão.")
        texto_normal("\nNo fim do corredor, Você acaba encontrando um \x1b[31mcorpo\x1b[0m ou o que restava dele. Um jaleco ensanguentado indicava que a vítima era um médico. A garganta")
        texto_normal("\nhavia sido rasgada, e os olhos estavam congelados em um olhar de horror absoluto. Em seu jaleco tinha escrito \x1b[3m'Pediatra'\x1b[0m"),pausa(" ")
        texto_normal("\nNa mesa perto do corpo, você encontra uma chave."), texto_lento("Mas"),texto_superlento("..."),texto_rapida("*CRIC*")
        texto_normal("\nVocê escuta um som de vidro sendo pisado em uma das salas, perto de você tem um armário"),pausa(" "),print()
        texto_normal("\nO que vai fazer?")
        print("\n1. Pegar a chave e se esconder no armário\n2. Se esconder no armário sem se preocupar com a chave\n3. Pegar a chave e correr"),print()
        caminho2 = int(input("> "))

        #Morte
        if caminho2 == 1:
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
        elif caminho2 == 2:
            
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
            resposta = int(input("> "))
            if resposta == 1:
                texto_normal("\n Lucas: Entendo"),texto_superlento("..."),texto_normal(" Vamos tentar escapar desse maldito lugar!"),pausa(" "),print()
            elif resposta == 2:
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
            escoolha = int(input("> "))

            # Finais da saída principal
            if escoolha == 1:
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
                final1 = int(input("> "))

                #Final junto com Lucas
                if final1 == 1:
                    
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
                elif final1 == 2:
                    
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

        #Morte
        else:
            texto_normal("\nVocê se agacha rapidamente no meio do corredor, seus dedos trêmulos pegando a chave que estava caída no chão. Com um suspiro de alívio, você a segura firme.")
            texto_normal("\nAgora, a única coisa que você precisa fazer é correr até a saída."),pausa(" ")
            texto_normal("\nCom a chave em mãos, você começa a correr, seu coração batendo forte no peito. Mas, antes que você consiga chegar à porta, um som abafado quebra o silêncio.")
            texto_normal("\nVocê olha para trás, apenas para ver a silhueta do monstro surgindo das sombras."),pausa(" ")
            texto_normal("\nEle está rápido, mais rápido do que você imaginava. O medo toma conta de você e, no momento em que tenta alcançar a porta, o monstro avança com uma velocidade")
            texto_normal("\nimpressionante, agarrando você com sua lâmina afiada."),pausa(" ")
            texto_normal("\nVocê grita, mas sua voz é abafada pelo som de ossos se quebrando. A dor é intensa, e tudo ao seu redor se torna escuridão."),texto_superlento("... "),pausa(" "),print()
            texto_lento("\n\x1b[31mGame Over...\x1b[0m"),print()
            pausa("  ")
            print("                                                             "), texto_lento("Carregando último checkpoint"),texto_superlento("..."),pausa("  "), print()
            break




