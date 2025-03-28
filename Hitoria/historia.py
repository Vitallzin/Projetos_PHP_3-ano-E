import time
import sys

def pausa(mensagem, velocidade=1):
    for letra in mensagem:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)

def texto_superlento(mensagem, velocidade=0.5):
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
    
def texto_rapida(mensagem, velocidade=0.02):
    for letra in mensagem:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
      

#Cores de texto: \x1b[30m: Preto, \x1b[31m: Vermelho, \x1b[32m: Verde, \x1b[33m: Amarelo, \x1b[34m: Azul, \x1b[35m: Magenta, \x1b[36m: Ciano.
# Loop principal (menu do jogo)
while True:
    print("\x1b[31mThe Forbidden Ward\x1b[0m")
    print("1 - Jogar")
    print("2 - Sair")
    escolha = input("> ")

    if escolha == "2":
        texto_lento("Saindo do jogo..."), print()
        break

    elif escolha == "1":
        texto_lento("Iniciando o jogo..."), print()
        texto_lento("\nRegras do jogo: "), print()
        texto_normal("\n1° Se fizer uma escolha fora das opções, automaticamente será escolhida a última.")
        texto_normal("\n2° Se aparecer uma mensagem 'Salvando...' indicara um chekpoint."), print()
        
        # Checkpoint 1
        while True:
            texto_rapida("\n\x1b[1mHistória completamente fictícia."), print()
            texto_rapida("Qualquer semelhança com nomes, locais ou acontecimentos reais é mera coincidência.Esta é apenas uma história de suspense e terror psicológico.\x1b[0m"), print()
            print("                                                             "), texto_superlento("Salvando..."), print()
            texto_normal("\nNa década de 80, em uma pequena cidade do interior, três jovens inseparáveis passavam os dias em busca de aventuras: "), print()
            texto_normal("Você, Lucas e Rafaela. Amigos desde a infância, sempre foram curiosos, explorando florestas, trilhas e ruínas abandonadas ao redor da cidade."), print()
            texto_normal("Em uma tarde qualquer, você estava em casa, assistindo televisão, quando sua mãe te chamou:"), print()
            texto_normal("\n Mãe: "), texto_lento("FILHOO!!!"), texto_normal("Os seus amigos estão te chamando!"),pausa(" "), print()
            print("\n 1. JÁ VOU!! (você grita)\n 2. Avisa que já vou mãe!")
            escolha1 = int(input("> ")) #escolha da fala com a mãe
            if escolha1 == 1:
                texto_normal("Mãe: OK!"), texto_lento(" ELE JÁ VAII!!"), print()
            else:
                texto_normal("Mãe: ") , texto_lento("VOCÊ FALOU O QUE?!"), print()
                texto_normal("Você: EU JÁ VOU MÃE!!"), print()
            texto_normal("\nVocê desliga a TV, calça seus tênis e e quando está saindo "), print()
            texto_normal("a sua mãe te chama e fala:"), print()
            texto_normal("\n Mãe: Tenha cuidado filho, eu quero você aqui antes das oito."),pausa(" "), print()
            texto_normal("\nela se aproxima, te da um abraço e um beijo"), print()
            texto_normal("\n Mãe: Que Deus te abençoe. "),pausa(" "), print()
            texto_normal("\nO céu ainda claro mostrava que a tarde estava longe de acabar. Vocês começam a andar pelas ruas da cidade, conversando sobre nada e tudo ao mesmo tempo,"), print()
            texto_normal("jogando conversa fora, rindo alto, sem pressa."), print()
            texto_normal("Mas as horas passam. O sol começa a desaparecer, e quando a noite cai, vocês decidem ir um pouco além do comum."), print()
            texto_normal("Foi então que Lucas, com um olhar malicioso, disse:"), print()
            texto_normal("\n Lucas: Ei"), texto_superlento("..."), texto_normal (" Vocês já ouviram falar do Hospital Saint Mary?"), print ()
            texto_lento("\nRafaela franze a testa."),pausa(" "), print ()
            texto_normal("\n Rafaela: Aquele abandonado?")
            texto_lento("\n Lucas: Sim"),texto_superlento("..."), print()
            texto_lento("\nLucas sorri."),pausa(" "), print()
            texto_normal("\n Lucas:Dizem que na década de 60, um incêndio começou no subsolo. Ninguém nunca descobriu o que causou"),texto_superlento("..."), texto_normal(" e o pior: médicos e pacientes presos lá embaixo jamais")
            texto_normal("\n foram encontrados. Alguns dizem que, nas noites mais silenciosas, dá pra ouvir gritos vindo de dentro do prédio."), print()
            texto_lento("\nRafaela, tentando bancar a corajosa, dá risada."),print ()
            texto_normal("\n Rafaela: Ah, isso é só história de velho pra assustar criança."),print
            texto_lento("\nLucas encara vocês dois."),pausa(" "), print()
            texto_normal("\n Então vamos até lá ou vocês vão correr?"), print
            #escolha para aventura
            print("1. Isso ai é história para boi dormir, já estou pronto!\n2. Acho melhor não, já está ficando tarde")
            escolha2 = int(input("> "))
            if escolha2 == 1:
                texto_normal("\n Rafaela: Sei não viu, mas como vocês dois vão, não me resta escolha. Vamos!"), print()
            else:
                texto_normal("\n Lucas: Sério que está com medo?"),texto_lento(" HAHAHAHAHA!!"),pausa(" "),texto_normal("Qual foi, vamos, vai ser divertido! e você Rafaela?"), print()
                texto_lento("\nRafaela fica pensativa e coçando a cabeça"),pausa(" "),print()
                texto_normal("\n Rafaela: Hmm"), texto_superlento("... "),texto_normal("Só vou se ele (Aponta para você) for! "),pausa(" ")
                texto_normal("\n Lucas: E ai mano? Vai fraquejar?"),pausa(" "), print()
                #esolha definitiva
                print("\n1. Caramba... Vamos vamos, o que pode dar de errado?\n2. Melhor não, vou para casa galera, até amanhã!")
                escolha4 = int(input("> "))
                if escolha4 == 1:
                    texto_normal("\n Lucas: AEEEE!!!"),pausa(" "),texto_normal("Vamos logo!")
                else:
                    texto_lento("\n Lucas: Poxa"),texto_superlento("..."),texto_normal(" Tudo bem, até mais"),pausa(" "), print()
                    texto_superlento("Fim de jogo!")
                    break
            print("\n         "),texto_superlento("Salvando..."), print()
            texto_normal("O caminho até o hospital não foi longo, mas pareceu uma eternidade. À medida que vocês se afastavam da cidadeas ruas de terra e a luz fraca das")
            texto_normal("\nlâmpadas públicas começavam a desaparecer. A escuridão tomava conta e o silêncio da noite interrompido apenas pelo som das próprias pedaladas")
            texto_normal("\nparecia pesado, como se a própria terra guardasse segredos antigos e esquecidos.")
            texto_normal("\nFinalmente, o hospital Saint Mary surgiu diante de vocês, imenso e ameaçador. Seus muros de pedra, desgastados pelo tempo, estavam cobertos de")
            texto_normal("\nmusgo e líquens, e a fachada, que um dia deve ter sido branca, agora estava desbotada e manchada de cinza, como se tivesse absorvido o ")
            texto_normal("\nsofrimento que ali se passou. O portão de ferro enferrujado estava entreaberto, rangendo a cada brisa que passava, criando um som ")
            texto_normal("\nfantasmagórico que parecia convidar a entrar, mas ao mesmo tempo avisava que algo não estava certo."),pausa(""),print()
            texto_normal("\n Lucas: Finalmente chegamos, vamos esconder as nossas bikes na arbustro."),pausa(" ")
            texto_normal("\n Lucas: Quem vai ser o primeiro a entra?"),pausa(" "),print()
            print("\n1.Eu vou!\n2.Primeiro as damas, né?\n3.Pode ir Lucas, estamos logo atrás de você.")
            #escolha de quem vai primeiro
            escolha5 = int(input("> "))
            if escolha5 == 1:
                texto_normal("\n Lucas: Olha para ele, todo corajoso, entre ai então")
            elif escolha5 ==2:
                texto_normal("\n Rafaela: Frouxo! Tudo bem, eu vou primeiro")
            else:
                texto_normal("\n Lucas: Tudo bem, eu lidero vocês, hehe."),pausa(" "), print()
                texto_normal("\nLucas passa primeiro pelo portão e então:"), pausa(" "), print()
                texto_normal("\n Lucas: AAAAAHHHHHHH!!! SOCORRO!!"), print()
                texto_normal("\nVocês entram rapidamente preocupados e se deparan com"),texto_superlento("..."),pausa(" "),texto_normal("Lucas rindo da cara de vocês"),pausa(" "),print()
                texto_normal("\n Lucas: HAHAHAHAHAHA!!!"), pausa(" ")
                texto_normal("\n Rafaela: Isso não tem graça seu idiota."), pausa(" ")
                texto_normal("\n Lucas: HAHAHA!!! Deviam ter visto da cara de vocês HAHAHAHA! Muito bom! ")
            texto_normal("Após entrarem, sente que o ar lá dentro era denso e gelado, diferente do calor da tarde. O vento parecia assobiar, como se sussurrasse palavras")
            texto_normal("\nesquecidas, e a sensação de desconforto aumentava a cada passo dado no terreno abandonado."),print()
            print("                              Mapa")
            print("\n                  |                                            | ")
            print("     Aréa         |                                            | ")
            print("      não         |                                            |")
            print("    explorada     |                    entrada                 |")
            print("                  |___________________---------________________|")
            print("                                                               |")
            print("                                                               |")
            print("                                                               |")
            print("                                                               |")
            print("                                                               |")
            print("                                      Vocês                    |")
            print("                                        o                      |")
            print("                                                               |")
            print("                               portão                          |")
            print("_____________________________-----------_______________________|")
            texto_normal("Qual a sua escolha?"),pausa(" "), print()
            print("\n1. Ir para entrada\n2. Ir para o portão\n3. Ir para Aréa não explorada")
            #escolha do caminho
            escolha6 = int(input("> "))
            if escolha6 == 1:
                texto_normal("\n Lucas: Concordo, vamos para a entrada!"),pausa(" "),print()
            elif escolha6 ==2:
                texto_normal("\n Lucas: Deixa de ser medroso, nós vamos direto para entrada"),pausa(" "),print()
            else:
                texto_normal("\n Lucas: Tudo bem, vamos explorar lá antes de entrar. Espero que você não esteja me enrolado em espertinho."),pausa(" "),print()
                print("                              Mapa")
                print("_________________\x1b[31m--------------------\x1b[0m____________________________")
                print("|                                                               |")
                print("|                                                               |")
                print("|                  Estacionamento                               |")
                print("|                                                               |")
                print("|                                                               |")
                print("\x1b[33m]\x1b[0m                                                               |")
                print("\x1b[33m]\x1b[0m                                                               |")
                print("\x1b[33m]\x1b[0m  Portão                                                       |")
                print("\x1b[33m]\x1b[0m                                                               |")
                print("\x1b[33m]\x1b[0m                                                               |")
                print("\x1b[33m]\x1b[0m                                                               |")
                print("|                                                               |")
                print("|                     Vocês                                     |")
                print("|                       o                                       |____")
                print("|                                                                ")
                texto_normal("Vocês veem um estacionamento, com um portão trancado, uma saida de emergencia e alguns carros abandonados e em pessímo estado. No lado direito, vocês veem algumas")
                texto_normal("\nJanelas tampadas e outras não, mas por dentro está tudo escuro e vocês não conseguem ver nada"),pausa(" "),print()
                texto_normal("\n Lucas: Vamos para entrada principal, aqui não vamos a lugar nenhum"),pausa(" "), print()
            #escolha que levou ate a entrada
            texto_normal("\nOs três se aproximaram da entrada principal. As portas de madeira estavam parcialmente quebradas, e uma cortina de poeira cobria o que parecia")
            texto_normal("\nser uma recepção, desmoronada pelo tempo e pelo abandono. No chão, pedaços de vidro e madeira estilhaçada misturavam-se com papéis amarelados e")
            texto_normal("\nenvelhecidos, como se o hospital tivesse sido interrompido em meio a uma rotina normal."),pausa(" "),print()
            texto_lento("\nRafaela olhou ao redor, uma expressão de ceticismo no rosto."),pausa(" "),print()
            texto_normal("\n Rafaela: Não é nada demais. É só um lugar velho e abandonado. Não tem nada aqui"),texto_superlento("..."), texto_rapida("  *Crack!*"),pausa("  "),print("")
            texto_normal("\nMas, enquanto ela falava, um ruído estranho veio de dentro do hospital. Um estalo, como se algo ou alguém tivesse movido algo pesado nas profundezas.")
            texto_normal("\nA expressão de Lucas e a sua própria ficaram tensas."), print()
            print("\n1. ... (Não falar nada)\n2. O que foi isso???")
            escolha7 = int(input("> "))
            if escolha7 == 1:
                texto_normal("\n Lucas: hahaha(Rindo de nervoso), isso não foi nada, vamos entrar."), print()
            else:
                texto_normal("\n Lucas: Deve ser só o vento, ou algum animal. Vamos logo, o que estamos esperando?"), print()    
            print("\n         "),texto_superlento("Salvando..."), print()
            #Checkpoint 2
            texto_normal("Antes de entrarem Lucas pega se sua mochila 3 lanternas e entrega uma cada dos seus amigos. Vocês entram e dão de cara com a recepção"),pausa(" "),print()
            while True:
                print("                                               MAPA"),print()
                print("\n|        Corredor             |                                     |           Corredor               |")
                print("|        Esquerdo             |                                     |           Direito                |")
                print("|                             |                                     |                                  |")
                print("|                             |                                     |                                  |")
                print("|                             |                                     |                                  |")
                print("|                             |_____________________________________|                                  |")
                print("|                                              Balcão de                                               |")
                print("|                                             Atedimentos                                              |")
                print("|                             |_____________________________________|                                  |")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("|                      Aréa de espera                                            Aréa de espera        |")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("|_________________________________________--------------_______________________________________________|")
                texto_normal("Qual a sua escolha?"),print()
                print("1. Corredor da direita\n2. Corredor da esquerda\n3. Voltar para área externa")
                #Escolha do corredor
                escolha8 = int(input("> "))
            


                #Escolha da direita
                if escolha8 == 1:
                    
                    print("                                                             "), texto_superlento("Salvando..."), print()
                    texto_normal("\n Lucas: Tudo bem, vamos pela direita"),pausa(" "),print()

                    texto_normal("\nDepois de atravessar a recepção, vocês seguem pelo corredor da direita. O cheiro de poeira e umidade enche o ar, e as paredes descascadas dão")
                    texto_normal("\num ar ainda mais sombrio ao ambiente. Conforme avançam, percebem que todas as portas estão trancadas, exceto uma, que está parcialmente aberta")
                    texto_normal("\ne completamente destruída. Quando espiam lá dentro, não há nada além de móveis quebrados, documentos espalhados pelo chão e uma maca virada."),pausa(" "),print()
                    texto_normal("\n Lucas: Bom, pelo menos sabemos que não estamos sozinhos aqui. Alguém já tentou abrir essas portas antes"),texto_superlento("... "),texto_normal("Um mendigo talvez"),pausa(" "),print()
                    texto_rapida("KABUMMM!!!"),pausa(" ")
                    texto_lento("\nAntes que alguém possa responder, o primeiro trovão ecoa do lado de fora. Começou a chover.")
                    texto_normal("\nRafaela franze o cenho, observando a tempestade que se forma através das janelas empoeiradas e completamente trancadas."),pausa(" "), print()
                    texto_normal("\n Rafaela: Isso está estranho. O tempo estava limpo"),texto_superlento("..."),pausa(" ")
                    texto_normal("\nVocês continuam caminhando e chegam até uma porta dupla maior, com uma placa metálica enferrujada escrita:"),print()
                    texto_lento("\n \x1b[1mALA DE EMERGÊNCIA\x1b[0m"),pausa(" "),print()
                    texto_normal("\nAntes que possam se aproximar, as lanternas começam a piscar descontroladamente. Primeiro a de Lucas, depois a de Rafaela e, por último, a sua.")
                    texto_normal("\nAo mesmo tempo, as luzes do hospital também piscam, como se o prédio tentasse voltar à vida por um instante.")
                    texto_normal("\nRafaela dá um passo para trás."),pausa(" "),print()
                    texto_normal("\n Rafaela: Isso… isso não faz sentido. Como esse lugar pode ter luz?"),pausa(" "), print()

                    print("                                                                                      ")
                    print("                                                            Entrada                   ")
                    print("                                                       Ala de Emergência              ")
                    print("______________________________________________________--------------------____________")
                    print("                                                                                      |")
                    print("                                                                                      |")
                    print("                                                                 Vocês                |")
                    print("                                                                   o                  |")
                    print("____________________________________________________                                  |")
                    print("                                                   |                                  |")
                    print("                                                   |                                  |")
                    print("                                                   |                                  |")
                    print("                                            Sala   |                                  |  Sala")
                    print("                                           Tranca  \x1b[33m]\x1b[0m                                  \x1b[33m]\x1b[0m Aberta")
                    print("                                                   \x1b[33m]\x1b[0m                                  \x1b[33m]\x1b[0m")
                    print("                                                   |                                  |")
                    print("                                                   |                                  |")
                    print("                                                   |                                  |")
                    print("                                                   |                                  |"),print()

                    texto_normal("Qual a sua escolha?"),print()
                    print("1. Entrar\n2. Voltar\n")
                    escolha9 = int(input("> "))
                    
                    #Se entrar
                    if escolha9 == 1:
                     print("                                                             "), texto_superlento("Salvando..."), print()
                     while True:
                        while True:
                            #texto_normal("\nO caminho até o hospital não foi longo, mas pareceu uma eternidade. À medida que vocês se afastavam da cidadeas ruas de terra e a luz fraca das")
                            texto_normal("\nO grupo atravessa a porta de emergência, e o primeiro impacto é o cheiro: algo podre, misturado com remédios antigos. Várias macas enferrujadas e")
                            texto_normal("\ncobertas de lençóis manchados estão espalhadas pelo local. Alguns monitores hospitalares desligados piscam luzes vermelhas fracas, sem motivo aparente.")
                            texto_lento("\nNo final do corredor, há uma porta com um letreiro:")
                            texto_lento("\n \x1b[1mSALA DE REGISTROS MÉDICOS\x1b[0m"),pausa(" "),print()
                            texto_normal("\nQuando vocês começam a se aproximar, um som surge de dentro da sala. É um barulho estranho, uma mistura de respiração ofegante e algo arranhando a madeira."),print()
                            texto_normal("Qual a sua escolha?"),print()
                            print("1. Galera, é melhor a gente voltar, isso ta muito estranho\n2. Gente... o que foi isso?")
                            escolha10 = int(input("> "))
                            
                            #Se hesitar
                            if escolha10 == 1:
                                texto_normal("\n Lucas: Ah, qual é, vai frangar agora?"),pausa(" "), texto_normal("Viemos até aqui, não dá para voltar agora!")
                            else: 
                                pass
                            pausa("...")
                            texto_normal("\n O AAAAAAIIIIIIIIIIIIIIIIIIIIIIII! "), pausa(" "), texto_normal("Vocês escutam um grito agudo vindo da sala"),print()
                            texto_normal("Então vocês verificam o que a dentro da sala pela janela da porta e quando iluminam"),texto_lento("...")
                            texto_normal("\nsurge uma mulher extremamente magra, vestindo apenas roupas íntimas. Sua pele está pálida e enrugada, e seus olhos parecem vazios e negros.")
                            texto_lento("\n \x1b[31mEla tem garras enormes e afiadas.\x1b[0m"),pausa(" ")
                            texto_normal("\nNo instante em que a luz da lanterna a toca, ela olha direto para vocês e começa a correr na direção da porta, batendo com força!"),pausa(" "),print()
                            texto_normal("O que você vai fazer?"),pausa(" "),print()
                            print("1. Segurar a porta e tentar trancá-la\n2. Se esconder em baixo de uma das camas\n3. Correr para fora da sala e fugir")
                            escolha_bixo = int(input("> "))

                            #escolha em trancar a sala
                            if escolha_bixo == 1:
                                texto_normal("\nVocê tenta trancar a sala mas monstro bate com força crescente e, em questão de segundos, arrebenta a porta")
                                texto_normal("\nVocê cai no chão por causa do impacto e vê o seus amigos fugindo, e quando você olha novamente para frente"),texto_superlento("...")
                                texto_normal("\nEm instantes o monstro te empala com as garras"),texto_superlento("..."),print()
                                texto_lento("\n\x1b[31mGame Over...\x1b[0m"),print()
                                pausa("  ")
                                print("                                                             "), texto_lento("Carregando último checkpoint"),texto_superlento("..."),pausa("  "), print()
                                break
                            #escolha em se esconder em baixo da cama
                            elif escolha_bixo == 2:
                                texto_normal("\nNo desespero Você e Rafaela se escondem em baixo de camas diferentes e Lucas corre para fora da sala"),pausa(" ")
                                texto_normal("\nO monstro começa a rondar a sala e Rafaela,"),texto_lento("tremendo,"),texto_normal("tenta respirar silenciosamente, mas acaba deixando escapar um soluço.")
                                texto_normal("\n O monstro logo percebe a localização de Rafaela"),print()
                                texto_normal("\nO que vai fazer?"),pausa(" "), print()
                                print("\n1. Ficar em silêncio\n2. Chamar a atenção do monstro fazendo barulho")
                                escolha_vida_morte = int(input("> "))
                                #escolha do silencio e Rafaela morre
                                if escolha_vida_morte == 1:
                                    texto_normal("\nO monstro se aproxima da cama onde Rafaela está e então"),texto_superlento("..."),pausa(" ")
                                    texto_rapida("\nAAAAAAAAAAHHHHHH!")
                                    texto_normal("Você escuta os gritos de Rafaela enquanto começa a espalhar \x1b[31msangue\x1b[0m por toda sala"),pausa(" ")
                                    texto_lento("\x1b[31mRafaela morreu\x1b[0m"),pausa(" "),print()
                                    texto_normal("\nO monstro começa a carregar o corpo de Rafaela para a sala de registro, sem escolha, Você sai consegue sair da sala"),pausa(" ")
                                    texto_normal("\nAterrorizado, você começa a caminhar em direção a \x1b[1mALA PEDIATRICA E CIRÚRGICA\x1b[0m  ")

                                    #Caminho para o final sem a Rafaela e distante de Lucas
                                    
                                    texto_normal("\nO monstro se aproxima da cama onde Rafaela está e então"),texto_superlento("..."),pausa(" ")
                                    texto_rapida("\nAAAAAAAAAAHHHHHH!")
                                    texto_normal("Você escuta os gritos de Rafaela enquanto começa a espalhar \x1b[31msangue\x1b[0m por toda sala"),pausa(" ")
                                    texto_lento("\x1b[31mRafaela morreu\x1b[0m"),pausa("  "),print()
                                    texto_normal("\nO monstro começa a carregar o corpo de Rafaela para a sala de registro, sem escolha, Você consegue sair da sala"),pausa(" ")
                                    texto_normal("\nAterrorizado, você começa a caminhar em direção a \x1b[1mALA PEDIATRICA E CIRÚRGICA\x1b[0m  "),print
                                    print("\n                                                                                      ")
                                    print("                                                                     Entrada          ")
                                    print("                                                                Ala de Emergência     ")
                                    print("_______________________________________________________________--------------------___")
                                    print(" \x1b[33m]\x1b[0m                                                                     ")
                                    print(" \x1b[33m]\x1b[0m Porta      Você                                                     ")
                                    print(" \x1b[33m]\x1b[0m aberta        o                                                     ")
                                    print(" \x1b[33m]\x1b[0m                                                                     ")
                                    print("_____________________________________________________________                         ")
                                    print("                                                             |                        ")
                                    print("                                                             |                        ")
                                    print("                                                             |                        ")
                                    print()
                                    pausa("    ")
                                    texto_normal("Você nota que a porta está meio aberta e pressupõe que possa ter sido Lucas."),pausa(" ")
                                    texto_normal("\nLucas havia sumido muito antes, correndo apavorado para algum lugar desconhecido. Rafaela, por outro lado"),texto_superlento("..."),texto_normal("ela não conseguiu escapar. O monstro")
                                    texto_normal("\na alcançou antes que ele pudesse fazer algo. O último grito dela ainda ecoava em sua mente, misturado à culpa esmagadora de ter fugido enquanto")
                                    texto_normal("\nela era dilacerada."),pausa(" ")
                                    texto_normal("\nA escuridão tomava conta do hospital. O som de seus passos ecoava pelos corredores desertos, interrompidos apenas pelo gotejar incessante da")
                                    texto_normal("\nchuva que agora caía do lado de fora.")
                                    texto_normal("\nnAgora Você encontrava no meio do corredor principal")
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
                                        texto_normal("Em frente: Saída.  A direita: Ala Pediátrica. A esquerda: Ala Cirúrgica")
                                        texto_normal("\nQual caminho você vai seguir primeiro?")
                                        print("\n1. Saída\n2. Ala Pediátrica\n 3. Ala Cirúrgica")
                                        caminho = int(input("> "))

                                        if caminho == 1:
                                            while True:
                                                texto_normal("Ao conferir a porta que leva a saída, percebe que está trancada com correntes e um grande cadeado resistente.")
                                                break
                                        elif caminho == 2:
                                            while True:
                                                texto_normal("Ao conferir a porta que leva a Ala Pediátrica, percebe que a porta está trancada.")
                                                break
                                        else:
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

                                                        # Finais com lucas
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
                                                                #texto_normal("\nO caminho até o hospital não foi longo, mas pareceu uma eternidade. À medida que vocês se afastavam da cidadeas ruas de terra e a luz fraca das")
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
                                                        else:
                                                            texto_normal("\n Lucas: Vamos ver o que tem aqui dentro primeiro, aquele corredor me da calafrios!")
                                                            break
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

                                else:
                                    texto_normal("\nO monstro te escuta e muda de direção rapidamente"),texto_superlento("...")
                                    texto_rapida("\n HAAAAAAA!"), texto_normal("   O monstro derrepente se abaixa e aparece na sua frente!"),print()
                                    texto_normal("\n O que vai fazer?"),print()
                                    print("\n1.Tenta sair da cama pelos lados\n2. Ligar a luz da lanterna na cara dela ")
                                    escolha_vida_morte1 = int(input("> "))
                                    #se sair da cama
                                    if escolha_vida_morte1 == 1:
                                        texto_normal("Você tenta sair da cama"),texto_superlento("..."),texto_normal(" Mas logo é supreendido pelo mosntro que em instantes o monstro te empala com as garras"),texto_superlento("..."),print()
                                        texto_lento("\n\x1b[31mGame Over...\x1b[0m"),print()
                                        pausa("  ")
                                        print("                                                             "), texto_lento("Carregando último checkpoint"),texto_superlento("..."),pausa("  "), print()
                                        break
                                    #Fugindo e salvando rafaela
                                    else:
                                        texto_normal("\nVocê liga a luz na cara do monstro, fazendo ele ficar atordoado, aproveitando, Você e Rafaela começam a correr e sair da sala")
                                        texto_normal("indo em direção a \x1b[1mALA PEDIATRICA E CIRÚRGICA\x1b[0m  ")

                                        #Caminho para o final com a Rafaela e distante de Lucas



                            #Fugir correndo mas rafaela morre
                            else:
                                texto_normal("\nVocê e Lucas começam a correr, conseguem sair da sala e vão em direção a \x1b[1mALA PEDIATRICA E CIRÚRGICA\x1b[0m  ")
                                texto_normal("Enquanto correm, percebem que Rafaela não está com vocês")

                                #Caminho para o Final sem a Rafaela e junto de Lucas
                                
                        
                    else:
                        while True:    
                            texto_normal("\nO grupo volta apressado para a recepção, mas ao chegar lá, se deparam com uma visão aterrorizante: a entrada do hospital está completamente obstruída.") 
                            texto_normal("\nAquela porta por onde tinham acabado de passar minutos atrás agora está coberta por entulho, móveis velhos e destroços. Como se algo"),texto_superlento("..."),texto_normal("ou alguém")
                            texto_normal("\nquisesse garantir que eles não saíssem.")
                            texto_normal("\nLucas dá um passo para trás, sua voz trêmula:"),pausa(" "),print()
                            texto_normal("\n Lucas: Isso"),texto_superlento("..."),texto_normal(" isso não tava assim antes."),pausa(" "),print()
                            texto_normal("\nSem outra saída, o grupo decide retornar para o corredor direito, que agora é a única opção"),pausa(" "),print()
                            break




                elif escolha8 == 2:
                    while True:
                        #texto_normal("\nO caminho até o hospital não foi longo, mas pareceu uma eternidade. À medida que vocês se afastavam da cidadeas ruas de terra e a luz fraca das")
                        texto_normal("\nO grupo decide seguir pelo corredor da esquerda, mas ao caminhar alguns metros, percebem que o caminho está completamente bloqueado. Móveis ")
                        texto_normal("\ncaídos, macas enferrujadas e pedaços do teto desabaram no meio do corredor, impossibilitando a passagem.")
                        texto_normal("\nLucas solta um suspiro frustrado:"),pausa(" "), print()
                        texto_normal("\n Lucas:Mas que merda"),texto_superlento("..."),texto_lento("e agora?"),pausa(" "),print()
                        texto_normal("\nRafaela ilumina os escombros com a lanterna, mas não parece haver nenhum jeito fácil de passar. O hospital inteiro parece estar desmoronando aos poucos."),pausa(" "), print()
                        texto_normal("\n Rafaela: Sem chance de atravessar isso. Vamos ter que voltar. "),pausa(" "),texto_lento("Ela diz, começando a andar na direção oposta."),pausa(" "), print()
                        texto_normal("\nSem escolha, o grupo retorna até a recepção."),pausa(" "),print()
                        break
                else:
                    while True:
                        texto_normal("\n Lucas: Você ta de brincadeira comigo né?"),pausa(" "),texto_normal("Vamos explorar primeiro"),pausa(" "),print()
                        break

                            

