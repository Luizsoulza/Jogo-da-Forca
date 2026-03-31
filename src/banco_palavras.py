import random

class BancoPalavras:
    def __init__(self):
        
        self._palavras = {
            "tecnologia": [
                "python", "java", "linux", "algoritmo", "variavel", "funcao", "classe", "objeto",
                "servidor", "database", "protocolo", "compilador", "framework", "backend", "frontend",
                "api", "docker", "github", "firebase", "kernel"
                ],
            "games": [
                "minecraft", "zelda", "mario", "sonic", "kirby", "halo", "skyrim", "tetris",
                "pacman", "pokemon", "pikachu", "fortnite", "valorant", "overwatch", "darksouls",
                "warcraft", "diablo", "fallout", "portal", "roblox"
                ],
            "filmes": [
                "matrix", "terminator", "avatar", "batman", "superman", "spiderman", "joker",
                "ironman", "thor", "hulk", "hobbit", "gandalf", "rocky", "gladiator", "inception",
                "interstellar", "robocop", "godzilla", "transformers", "jurassicpark"
                ],
        }
    
    def listar_categorias(self):
        return list(self._palavras.keys())
    
    def obter_palavras_categoria(self, categoria):  # retorna a lista de palavras de uma categoria específica

        categoria = categoria.lower()               # converte o texto para minúsculo para não dar erro
                                                    # exemplo: "Games", "GAMES" ou "games"
                                                    # Verifica se a categoria existe no banco de palavras
        if categoria in self._palavras:
                                                    # Retorna a lista de palavras daquela categoria
            return self._palavras[categoria]
        else:
            raise ValueError("Categoria inválida") # Caso a categoria não exista, gera um erro
                                                    # Isso impede o jogo de continuar com uma categoria inválida
                                    
    def sortear_palavra(self, categoria):            # Sorteia uma palavra aleatória dentro de uma categoria escolhida

        palavras_categoria = self.obter_palavras_categoria(categoria)   # Primeiro pega todas as palavras da categoria escolhida
    
        return random.choice(palavras_categoria)      # random.choice escolhe um elemento aleatório de uma lista