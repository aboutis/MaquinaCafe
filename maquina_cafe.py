from data import MENU
from data import recursos
import emoji

dinheiros = 0
descricao = {
    "Água": recursos['agua'],
    "Leite": recursos['leite'],
    "Café": recursos['cafe'],
}
print("-"*30)
for i, j in descricao.items():
    print(f"{i}:", end=' ')
    print(f"{j}ml")
print(f"Dinheiro em caixa: R${dinheiros}")
print(("-"*30))
escolha = input("Escolha entre espresso, latte ou cappuccino: ")


def verificando():
    """Verifica se os recursos são suficientes."""
    agua = MENU[escolha]['ingredientes']['agua']
    if agua > descricao['Água']:
        return False
    cafe = MENU[escolha]['ingredientes']['cafe']
    if cafe > descricao['Café']:
        return False
    if escolha == 'latte' or escolha == 'cappuccino':
        leite = MENU[escolha]['ingredientes']['leite']
        if leite > descricao['Leite']:
            return False
    return True


resultado = verificando()

if not resultado:
    print("Recursos insuficientes.")


def dinheiro():
    moedas = [0.05, 0.10, 0.25, 0.5, 1]
    total = []
    for i in moedas:
        valor = input(f"Quantas moedas de R$:{i}? ")
        mid = float(valor)*i
        total.append(mid)
    final = sum(total)
    return final


def check_dinheiro(moedas):
    if moedas >= MENU[escolha]['preco']:
        global dinheiros
        dinheiros += moedas
        dif = moedas - MENU[escolha]['preco']
        print(f"Seu troco é {dif:.2f}")
        return True
    else:
        print("Sinto muito, você não tem dinheiro suficiente. ")
        return False


def fazendo_cafe():
    descricao['Água'] -= MENU[escolha]['ingredientes']['agua']
    descricao['Café'] -= MENU[escolha]['ingredientes']['cafe']
    if escolha == 'latte' or escolha == 'cappuccino':
        descricao['Leite'] -= MENU[escolha]['ingredientes']['leite']


qtd_dinheiro = dinheiro()
chk_dinheiro = check_dinheiro(qtd_dinheiro)
fazendo_cafe()

print(emoji.emojize(f"\nAproveite o seu {escolha}! \u2615 \n"))
print("-"*20)
print("Recursos atualizados: ")
print("-"*20)
for i, j in descricao.items():
    print(f"{i}:", end=' ')
    print(f"{j}ml")
print(f"Dinheiro: R${dinheiros}")
