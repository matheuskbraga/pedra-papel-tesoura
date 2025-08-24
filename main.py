import random
import os
import time

# --- Variáveis Globais ---
# Estas variáveis guardam o estado do jogo e são partilhadas entre as funções.
move_list = ["papel", "pedra", "tesoura"]
player_count = 0
computer_count = 0

# --- Funções do Jogo ---

def clear_screen():
    """Limpa o ecrã do terminal para uma melhor visualização."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main_print():
    """Imprime o cabeçalho e o placar atual do jogo."""
    print("="*40)
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura")
    print("="*40)
    print("Placar")
    print(f"Jogador: {player_count} x Computador: {computer_count}")
    print("\nEscolha sua jogada:")
    print("0 - Papel | 1 - Pedra | 2 - Tesoura")

def select_computer_move():
    """Seleciona uma jogada aleatória para o computador."""
    return random.choice(move_list)

def get_player_move():
    """
    Obtém a jogada do jogador e a valida.
    Esta função foi corrigida para tratar a entrada do utilizador corretamente.
    """
    while True:
        try:
            player_move_index = int(input("Digite sua jogada (0, 1, 2): "))
            # Verifica se o número digitado está dentro do intervalo válido
            if player_move_index in [0, 1, 2]:
                # Se for válido, retorna a jogada correspondente da lista e sai do loop
                return move_list[player_move_index]
            else:
                print("Jogada inválida. Por favor, escolha 0, 1 ou 2.")
        except ValueError:
            # Captura o erro se o utilizador digitar algo que não é um número
            print("Entrada inválida. Por favor, digite um número.")

def select_winner(p_move, c_move):
    """
    Determina o vencedor da rodada e atualiza o placar.
    Usa a palavra-chave 'global' para modificar as variáveis de contagem.
    """
    global player_count, computer_count
    
    # Lógica para empate
    if p_move == c_move:
        return "draw"
    
    # Lógica de vitória do jogador
    elif (p_move == "pedra" and c_move == "tesoura") or \
         (p_move == "tesoura" and c_move == "papel") or \
         (p_move == "papel" and c_move == "pedra"):
        player_count += 1
        return "player"
        
    # Se não empatou e o jogador não ganhou, o computador ganhou
    else:
        computer_count += 1
        return "computer"

# --- Loop Principal do Jogo ---
again = True
while again:
    clear_screen()
    main_print()
    
    player_move = get_player_move()
    computer_move = select_computer_move()
    
    winner = select_winner(player_move, computer_move)

    # Mostra os resultados da rodada
    print("\n" + "="*40)
    print(f"Você escolheu: {player_move.capitalize()}")
    print(f"O computador escolheu: {computer_move.capitalize()}")
    print("-" * 20)

    if winner == "player":
        print("Você ganhou esta rodada!")
    elif winner == "computer":
        print("O computador ganhou esta rodada!")
    else:
        print("Esta rodada foi um empate!")
    print("="*40)

    # Loop para perguntar se quer jogar novamente (corrigido)
    while True:
        try:
            # Adiciona uma pausa para o jogador ler o resultado
            time.sleep(1)
            choice = int(input("\nJogar novamente? (0 - SIM | 1 - NÃO): "))
            
            if choice == 0:
                break # Sai deste loop interno para começar uma nova rodada
            elif choice == 1:
                again = False # Define 'again' como False para sair do loop principal
                break
            else:
                print("Escolha inválida. Digite 0 ou 1.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

clear_screen()
print("="*40)
print("Obrigado por jogar!")
print("Placar Final:")
print(f"Jogador: {player_count} x Computador: {computer_count}")
print("="*40)
