const capacityCards = document.querySelectorAll('.hd_item.big');


capacityCards.forEach(e => {
    e.addEventListener('click', (el) => el.preventDefault())
})