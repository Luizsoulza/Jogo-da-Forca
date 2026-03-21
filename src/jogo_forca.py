from src.estado_jogo import EstadoJogo
from src.banco_palavras import BancoPalavras


class JogoForca:
    def __init__(self, categoria):
        self.banco_palavras = BancoPalavras()
        self.categoria = categoria
        self.__max_erros = 6
        self.iniciar_jogo(categoria)

    def obter_palavra_mascarada(self):
        palavra_mascarada = ""
        
        for i in self.palavra_secreta:
            if i in self.letras_descobertas:
                palavra_mascarada = palavra_mascarada + i + " "
            else:
                palavra_mascarada = palavra_mascarada + "_ "
        return palavra_mascarada
        
    def verificar_vitoria(self):
        if all(letra in self.letras_descobertas for letra in self.palavra_secreta):
            self.estado = EstadoJogo.VENCEU
            
    def verificar_derrota(self):
        if self.erros >= self.__max_erros:
            self.estado = EstadoJogo.PERDEU
            
    def tentar_letra(self, letra):
        self.letras_tentadas.append(letra)
        
        if letra in self.palavra_secreta:
            self.letras_descobertas.append(letra)
            
        else:
            self.erros += 1
        self.verificar_vitoria()
        self.verificar_derrota()    
    
    def iniciar_jogo(self, categoria):
        self.palavra_secreta = self.banco_palavras.sortear_palavra(categoria)
        self.letras_descobertas = []
        self.letras_tentadas = []
        self.erros = 0
        self.estado = EstadoJogo.EM_ANDAMENTO     
                    
    def listar_categorias(self):
        return self.banco_palavras.listar_categorias()
    
    def obter_estado_completo(self):
        return {
            "palavra_mascarada": self.obter_palavra_mascarada(),
            "erros": self.erros,
            "max_erros": self.__max_erros,
            "letras_tentadas": self.letras_tentadas,
            "estado": self.estado.name,
            "categoria": self.categoria
        }
    
    def reiniciar_jogo(self, categoria):
        self.iniciar_jogo(categoria)