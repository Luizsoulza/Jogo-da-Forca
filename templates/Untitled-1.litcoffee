# File Tree: Jogo_Forca

**Generated:** 3/19/2026, 9:37:30 PM
**Root Path:** `c:\Users\luizs\OneDrive\Área de Trabalho\ENGENHARIA DA COMPUTAÇÃO\APS - 3º SEMESTRE\Jogo_Forca`

```
├── 📁 src
│   ├── 🐍 __init__.py
│   ├── 🐍 banco_palaras.py
│   ├── 🐍 estado_jogo.py
│   └── 🐍 jogo_forca.py
├── 📁 static
├── 📁 templates
├── 🐍 app.py
└── 📄 requeriments.txt
```

---

**Jogo da Forca Orientado a Objeto**

Classes:

- BancoPalavras
- JogoForca
- EstadoJogo

Atributos BancoPalavras:

- palavra(público)

Métodos BancoPalavras:

- sortear_palavra(privado)

Atributos JogoForca:

- palavra_secreta(público)
- letras_descobertas(público)
- erros(público)

* \_\_max_erros(privado)

- banco_palavras(público)
- estado(público)

Métodos JogoForca:

- iniciar_jogo(privado)
- tentar_letra(privado)
- verificar_vitoria(privado)
- verificar_derrota(privado)
- obter_palavra_mascarada(privado)

EstadoJogo:

- EM_ANDAMENTO
- VENCEU
- PERDEU
