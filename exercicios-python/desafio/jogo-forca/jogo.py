# Importando 'Set' (conjuntos) para ajudar a não guardar letras repetidas
from typing import Set

#moldes do jogo

class Palavra:
    def __init__(self, secreta: str):
        # Já guarda a palavra secreta toda em maiúscula pra não ter problema na hora de comparar
        self.secreta = secreta.upper()

    def exibir_estado(self, letras_descobertas: Set[str]) -> str:
        # Monta a palavra na tela. Se o cara já chutou a letra, mostra ela. Se não, bota um "_" no lugar.
        return " ".join([letra if letra in letras_descobertas else "_" for letra in self.secreta])

    def foi_revelada(self, letras_descobertas: Set[str]) -> bool:
        # Verifica se todas as letras da palavra secreta estão dentro do "saco" de letras que o jogador já acertou
        return set(self.secreta).issubset(letras_descobertas)


class Jogador:
    def __init__(self, nome: str, tentativas: int = 6):
        self.nome = nome
        self.tentativas_restantes = tentativas
        # Uso 'set' em vez de lista '[]' porque o set não deixa adicionar letras iguais duas vezes
        self.letras_chutadas: Set[str] = set()

    def registrar_chute(self, letra: str) -> bool:
        letra = letra.upper()
        # Se a letra já tá no conjunto, aviso que deu ruim (False)
        if letra in self.letras_chutadas:
            return False  
        # Se for nova, eu adiciono no conjunto
        self.letras_chutadas.add(letra)
        return True


class Jogo:
    # O "Juiz" da partida. Ele precisa saber quem tá jogando e qual é a palavra
    def __init__(self, jogador: Jogador, palavra: Palavra):
        self.jogador = jogador
        self.palavra = palavra

    def processar_tentativa(self, letra: str) -> str:
        letra = letra.upper()
        
        # Tenta registrar o chute. Se o método devolver False, é porque a letra é repetida
        if not self.jogador.registrar_chute(letra):
            return f"[!] Você já chutou a letra '{letra}'. Tente outra."

        # Checa se a letra faz parte da palavra secreta
        if letra in self.palavra.secreta:
            return f"[✓] Boa! A letra '{letra}' existe na palavra."
        else:
            # Se errou, perde uma vida
            self.jogador.tentativas_restantes -= 1
            return f"[X] Ops! A letra '{letra}' não existe."

    def acabou(self) -> bool:
        # O jogo acaba se o cara zerar as vidas OU se adivinhar tudo
        if self.jogador.tentativas_restantes <= 0:
            return True
        if self.palavra.foi_revelada(self.jogador.letras_chutadas):
            return True
        return False


#rodando no terminal

# Essa trava faz com que o jogo só rode se eu apertar "play" direto nesse arquivo
if __name__ == "__main__":
    print("\n" + "="*40)
    print(" BEM-VINDO AO JOGO DA FORCA ")
    print("="*40)

    # Pegando as informações iniciais
    nome_jogador = input("Digite seu nome: ")
    palavra_escolhida = input("Mestre do Jogo, digite a palavra secreta (escondido): ")
    
    # "Pulo" 50 linhas em branco pra palavra secreta sumir da tela e o jogador não roubar
    print("\n" * 50) 

    # Criando os objetos na memória baseados nos moldes lá de cima
    jogador = Jogador(nome_jogador, tentativas=6)
    palavra = Palavra(palavra_escolhida)
    partida = Jogo(jogador, palavra)

    # Enquanto a partida NÃO acabar, continua repetindo esse menu
    while not partida.acabou():
        print("\n" + "-"*40)
        print(f"Palavra: {palavra.exibir_estado(jogador.letras_chutadas)}")
        print(f"Tentativas restantes: {jogador.tentativas_restantes}")
        # Pega as letras do conjunto, organiza em ordem alfabética e junta com vírgula pra ficar bonito
        print(f"Letras já chutadas: {', '.join(sorted(jogador.letras_chutadas))}")
        
        chute = input("\nDigite uma letra: ").strip()
        
        # Validação básica: tem que ter exatamente 1 caractere e tem que ser letra (não pode número)
        if len(chute) != 1 or not chute.isalpha():
            print("[!] Por favor, digite apenas uma letra válida.")
            continue # Pula pro próximo turno ignorando o que tá embaixo
            
        mensagem = partida.processar_tentativa(chute)
        print(mensagem)

    # Quando sai do loop, o jogo acabou. Aqui vê se o cara ganhou ou perdeu
    print("\n" + "="*40)
    if palavra.foi_revelada(jogador.letras_chutadas):
        print(f"🏆 PARABÉNS, {jogador.nome}! Você adivinhou a palavra '{palavra.secreta}'.")
    else:
        print(f"💀 FIM DE JOGO! Você foi enforcado. A palavra era '{palavra.secreta}'.")
    print("="*40 + "\n")