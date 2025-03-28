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

print("                                                   Enfermaria     ")
print("______________________________________________________------_____ ")
print("                                                                 |")
print("    Corredor                                         Vocês       |")
print("     Escuro                                            o         |")
print(" ______________________________________                          |")
print("                                      |                          |")
print("                                      |                          |")
print("                                      |                          |")
print("                                      |                          |")
print("                                      |                          |")





