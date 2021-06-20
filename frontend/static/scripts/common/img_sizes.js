const images = document.querySelectorAll('img');

images.forEach(e => {
    console.log(e)
    console.log(e.getAttribute('width'))
    e.width = e.offsetWidth;
    e.height = e.offsetHeight;
})

// window.addEventListener('resize',)