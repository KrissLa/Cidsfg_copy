const accordionItems = document.querySelectorAll('.contentBx');


const getHeight = function (el) {
    let el_style = window.getComputedStyle(el),
        el_display = el_style.display,
        el_position = el_style.position,
        el_visibility = el_style.visibility,
        el_max_height = el_style.maxHeight.replace('px', '').replace('%', ''),

        wanted_height = 0;

    // if its not hidden we just return normal height
    if (el_display !== 'none' && el_max_height !== '0') {
        return el.offsetHeight;
    }

    // the element is hidden so:
    // making the el block so we can meassure its height but still be hidden
    el.style.position = 'absolute';
    el.style.visibility = 'hidden';
    el.style.display = 'block';

    wanted_height = el.offsetHeight + 50;


    el.removeAttribute('style')
    el.style.height = '0';

    return wanted_height;
}

accordionItems.forEach((e) => {
    e.setAttribute('data-height', `${getHeight(e.querySelector('.contentBx .content'))}px`);
    e.querySelector('.label').addEventListener('click', () => {
        if (e.classList.contains('active')){
            e.classList.remove('active');
            e.querySelector('.contentBx .content').style.height = '0';
        } else{
            e.classList.add('active');
            e.querySelector('.contentBx .content').style.height = e.getAttribute('data-height');
        }

    })
})
