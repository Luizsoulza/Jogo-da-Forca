const API = '';

const telaCategorias = document.getElementById('tela-categorias');
const telaJogo = document.getElementById('tela-jogo');
const listaCategorias = document.getElementById('lista-categorias');
const categoriaLabel = document.getElementById('categoria-label');
const forcaImg = document.getElementById('forca-img');
const palavraMascarada = document.getElementById('palavra-mascarada');
const errosLabel = document.getElementById('erros-label');
const inputLetra = document.getElementById('input-letra');
const btnTentar = document.getElementById('btn-tentar');
const letrasTentadas = document.getElementById('letras-tentadas');
const btnReiniciar = document.getElementById('btn-reiniciar');

async function carregarCategorias() {
    const response = await fetch(`${API}/categorias`);
    const categorias = await response.json();
    categorias.forEach(categoria => {
        const btn = document.createElement('button');
        btn.textContent = categoria;
        btn.onclick = () => iniciarJogo(categoria);
        listaCategorias.appendChild(btn);
    });
}

async function iniciarJogo(categoria) {
    const response = await fetch(`${API}/iniciar`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ categoria })
    });
    const estado = await response.json();
    telaCategorias.style.display = 'none';
    telaJogo.style.display = 'flex';
    atualizarTela(estado);
}

async function tentarLetra() {
    const letra = inputLetra.value.toLowerCase().trim();
    if (!letra) return;

    if (!/^[a-z]$/.test(letra)) {
        alert('Apenas letras são permitidas!');
        inputLetra.value = '';
        return;
    }

    const response = await fetch(`${API}/tentar-letra`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ letra })
    });
    const estado = await response.json();
    inputLetra.value = '';
    atualizarTela(estado);
}

function atualizarTela(estado) {
    categoriaLabel.textContent = `Categoria: ${estado.categoria}`;
    palavraMascarada.textContent = estado.palavra_mascarada;
    errosLabel.textContent = `Erros: ${estado.erros} / ${estado.max_erros}`;
    letrasTentadas.textContent = `Tentadas: ${estado.letras_tentadas.join(' ')}`;
    forcaImg.src = `/static/img/forca_${estado.erros}.png`;

    if (estado.estado === 'VENCEU') {
        setTimeout(() => alert('🎉 Você venceu!'), 100);
        btnReiniciar.style.display = 'block';
        btnTentar.disabled = true;
        inputLetra.disabled = true;
    }

    if (estado.estado === 'PERDEU') {
        setTimeout(() => alert('💀 Você perdeu!'), 100);
        btnReiniciar.style.display = 'block';
        btnTentar.disabled = true;
        inputLetra.disabled = true;
    }
}

btnReiniciar.addEventListener('click', () => {
    telaJogo.style.display = 'none';
    telaCategorias.style.display = 'flex';
    btnReiniciar.style.display = 'none';
    btnTentar.disabled = false;
    inputLetra.disabled = false;
    listaCategorias.innerHTML = '';
    carregarCategorias();
});

btnTentar.addEventListener('click', tentarLetra);
inputLetra.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') tentarLetra();
});

carregarCategorias();