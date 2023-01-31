import random;

def abertura():
    print("*********************************");
    print("***Bem vindo ao jogo da Forca!***");
    print("*********************************");

def pede_chute():
    chute = input("Qual letra? ");
    chute = chute.strip().upper();
    return chute;

def marca_chute(chute, letras_acertadas, palavra_secreta):
    index = 0;
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra;
        index += 1;

def carrega_palavra_secreta():
    arquivo = open("Forca/palavras.txt", "r");
    palavras = [];
    for linha in arquivo:
        linha = linha.strip();
        palavras.append(linha);
    arquivo.close();
    numero = random.randrange(0, len(palavras));
    palavra_secreta = palavras[numero].upper();
    print(palavra_secreta)
    return palavra_secreta;

def desenha_forca(erros):
    print("  _______     ");
    print(" |/      |    ");
    if(erros == 1):
        print (" |      (_)   ");
        print (" |            ");
        print (" |            ");
        print (" |            ");
    if(erros == 2):
        print (" |      (_)   ");
        print (" |      \     ");
        print (" |            ");
        print (" |            ");
    if(erros == 3):
        print (" |      (_)   ");
        print (" |      \|    ");
        print (" |            ");
        print (" |            ");
    if(erros == 4):
        print (" |      (_)   ");
        print (" |      \|/   ");
        print (" |            ");
        print (" |            ");
    if(erros == 5):
        print (" |      (_)   ");
        print (" |      \|/   ");
        print (" |       |    ");
        print (" |            ");
    if(erros == 6):
        print (" |      (_)   ");
        print (" |      \|/   ");
        print (" |       |    ");
        print (" |      /     ");
    if (erros == 7):
        print (" |      (_)   ");
        print (" |      \|/   ");
        print (" |       |    ");
        print (" |      / \   ");
    print(" |            ");
    print("_|___         ");
    print();

def vencedor():
    print("Parabéns, você ganhou!");
    print("       ___________      ");
    print("      '._==_==_=_.'     ");
    print("      .-\\:      /-.    ");
    print("     | (|:.     |) |    ");
    print("      '-|:.     |-'     ");
    print("        \\::.    /      ");
    print("         '::. .'        ");
    print("           ) (          ");
    print("         _.' '._        ");
    print("        '-------'       ");

def perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!");
    print("A palavra era {}".format(palavra_secreta));
    print("    _______________         ");
    print("   /               \        ");
    print("  /                 \       ");
    print("//                   \/\    ");
    print("\|   XXXX     XXXX   | /    ");
    print(" |   XXXX     XXXX   |/     ");
    print(" |   XXX       XXX   |      ");
    print(" |                   |      ");
    print(" \__      XXX      __/      ");
    print("   |\     XXX     /|        ");
    print("   | |           | |        ");
    print("   | I I I I I I I |        ");
    print("   |  I I I I I I  |        ");
    print("   \_             _/        ");
    print("     \_         _/          ");
    print("       \_______/            ");

abertura()
palavra_secreta = carrega_palavra_secreta()
letras_acertadas = ["_" for letra in palavra_secreta];
print(letras_acertadas)
enforcou = False
acertou = False
erros = 0
while(not enforcou and not acertou):
    chute = pede_chute()
    if(chute in palavra_secreta):
        marca_chute(chute, letras_acertadas, palavra_secreta)
    else:
        erros += 1
        desenha_forca(erros)
    enforcou = erros == 7
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)
if(acertou):
    vencedor()
else:
    perdedor(palavra_secreta)