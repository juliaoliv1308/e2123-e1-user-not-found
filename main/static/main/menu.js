const btn = document.getElementById('botao');

function toggleMenu() {
    const header3 = document.getElementById('header3');
    header3.classList.toggle('active');
}

btn.addEventListener('click', toggleMenu);