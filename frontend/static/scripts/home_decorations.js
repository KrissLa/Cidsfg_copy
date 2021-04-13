"use strict";

// HOME DECORATIONS

const hdCards = document.querySelectorAll('a.hd_item');
console.log(hdCards)

hdCards.forEach((e) => {
        e.addEventListener('mouseenter', e => {
            const title = e.target.querySelector('.hd_black_title');
            title.classList.add('hd_hide');
        })
    }
)
hdCards.forEach((e) => {
        e.addEventListener('mouseleave', e => {
            const title = e.target.querySelector('.hd_black_title');
            setTimeout(() => {
                title.classList.remove('hd_hide');
            }, 150);

        })
    }
)



