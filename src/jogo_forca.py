from src.estado_jogo import EstadoJogo
from src.banco_palavras import BancoPalavras


class JogoForca:
    def __init__(self, categoria):
        self.banco_palavras = BancoPalavras()  # conecta no banco de palavras pra sortear depois
        self.categoria = categoria              # guarda qual categoria o jogador escolheu
        self.__max_erros = 6                   # limite de erros, coloquei como privado pra ninguém mudar por fora
        self.iniciar_jogo(categoria)           # já chama o inicio direto no construtor

    # insertion sort pra ordenar lista de letras em ordem alfabética
    # a lógica é: pega cada letra a partir da segunda, guarda ela como "chave"
    # e vai comparando com as anteriores, empurrando as maiores uma casa pra frente
    # até achar o lugar certo pra enfiar a chave, tipo organizar cartas na mão
    def _insertion_sort(self, letras: list) -> list:
        ordenadas = letras[:]                        # copia a lista antes pra não bagunçar o original
        for i in range(1, len(ordenadas)):           # começa do índice 1 porque o primeiro já tá "ordenado"
            chave = ordenadas[i]                     # letra que vai ser posicionada nessa rodada
            j = i - 1                                # j aponta pro elemento anterior à chave
            while j >= 0 and ordenadas[j] > chave:  # enquanto tiver elemento maior, empurra ele pra frente
                ordenadas[j + 1] = ordenadas[j]
                j -= 1                               # anda uma casa pra esquerda e continua comparando
            ordenadas[j + 1] = chave                 # achou o lugar certo, insere a chave
        return ordenadas

    # pega a palavra, tira as letras repetidas com set() e devolve ordenado via insertion sort
    # o set é importante porque palavras como "banana" teriam "a" e "n" duplicados
    # e aí a verificação de vitória ficaria errada sem isso
    def _letras_unicas_ordenadas(self, palavra: str) -> list:
        letras = list(set(palavra))        # set já elimina tudo que é repetido
        return self._insertion_sort(letras)

    # monta a palavra pra exibir na tela, mostrando as letras certas e _ no lugar das que ainda não foram descobertas
    def obter_palavra_mascarada(self):
        palavra_mascarada = ""
        for i in self.palavra_secreta:
            if i in self.letras_descobertas:
                palavra_mascarada = palavra_mascarada + i + " "  # letra já descoberta, mostra ela
            else:
                palavra_mascarada = palavra_mascarada + "_ "     # ainda não descoberta, esconde com _
        return palavra_mascarada

    def tentar_letra(self, letra):
        # checa se o jogador já tentou essa letra antes de fazer qualquer coisa
        if letra in self.letras_tentadas:
            raise ValueError(f"A letra '{letra}' já foi tentada.")

        self.letras_tentadas.append(letra)  # registra a tentativa independente de acerto ou erro

        if letra in self.palavra_secreta:
            self.letras_descobertas.append(letra)  # acertou, adiciona nas descobertas
        else:
            self.erros += 1  # errou, incrementa o contador de erros

        # usa o insertion sort pra pegar as letras únicas da palavra em ordem
        # depois converte as descobertas em set pra a busca ser O(1) em vez de percorrer lista toda vez
        letras_necessarias = self._letras_unicas_ordenadas(self.palavra_secreta)
        letras_descobertas_set = set(self.letras_descobertas)

        # verifica vitória primeiro, se todas as letras necessárias já foram descobertas ganhou
        # senão verifica derrota, se os erros chegaram no limite perdeu
        if all(l in letras_descobertas_set for l in letras_necessarias):
            self.estado = EstadoJogo.VENCEU
        elif self.erros >= self.__max_erros:
            self.estado = EstadoJogo.PERDEU

    def iniciar_jogo(self, categoria):
        self.palavra_secreta = self.banco_palavras.sortear_palavra(categoria)  # sorteia uma palavra da categoria
        self.letras_descobertas = []   # zera as descobertas
        self.letras_tentadas = []      # zera as tentativas
        self.erros = 0                 # zera os erros
        self.estado = EstadoJogo.EM_ANDAMENTO  # volta pro estado inicial

    def listar_categorias(self):
        return self.banco_palavras.listar_categorias()

    # monta o dicionário com o estado atual do jogo todo, é isso que o frontend consome pra atualizar a tela
    def obter_estado_completo(self):
        return {
            "palavra_mascarada": self.obter_palavra_mascarada(),
            "erros": self.erros,
            "max_erros": self.__max_erros,
            "letras_tentadas": self.letras_tentadas,
            "estado": self.estado.name,  # .name converte o enum pra string, ex: "VENCEU"
            "categoria": self.categoria
        }

    def reiniciar_jogo(self, categoria):
        self.iniciar_jogo(categoria)  # só chama o iniciar de novo, ele já reseta tudo