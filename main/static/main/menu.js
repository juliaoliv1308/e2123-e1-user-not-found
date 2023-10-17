const btnmobile = document.getElementById('btn-mobil');

function toggleMenu() {
    const nav = document.getElementById('nav');
    nav.classList.toggle('áctiva');

    btnmobile.addEventListener('click', toggleMenu);
    

}