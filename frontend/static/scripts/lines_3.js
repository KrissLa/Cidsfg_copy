// Общая функция - потом удалить!!!!

// const removeClass = (element, className) => {
//     if (element.classList.contains(className)) {
//         element.classList.remove(className);
//     }
// }
//
// const addClass = (element, className) => {
//     if (!element.classList.contains(className)) {
//         element.classList.add(className);
//     }
// }

const toggleClass = (element, className) => {
    if (!element.classList.contains(className)) {
        element.classList.add(className);
    } else {
        element.classList.remove(className);
    }
}


///

const lines = document.querySelectorAll('.lines .line'),
    secondLines = document.querySelectorAll('.lines .text'),
    texts = document.querySelectorAll('.lines .text span'),
    pictures = document.querySelectorAll('.lines .secondary-img');

const line = document.querySelector('#line-1'),
    secondLine = document.querySelector('#sec-text-1'),
    text = secondLine.querySelector('span'),
    picture = document.querySelector('#sec_1'),


    sectionLines = document.querySelector('section.lines'),
    bigImage = document.querySelectorAll('.center-img');

const allLinesAnimationOneTime = () => {
    lines.forEach(e => addClass(e, 'active'));
    setTimeout(() => {
        secondLines.forEach(e => addClass(e, 'active'));
        texts.forEach(e => addClass(e, 'active'));
        pictures.forEach(e => addClass(e, 'active'));

    }, 500)
}
const linesAnimation = (line, secondLine, text, picture) => {
    addClass(line, 'active');
    setTimeout(() => {
        addClass(secondLine, 'active');
        addClass(text, 'active');
        addClass(picture, 'active');

    }, 500)
}

const linesAnimationToggle = (line, secondLine, text, picture) => {

    if (!line.classList.contains('active')) {
        toggleClass(line, 'active');
        setTimeout(() => {
            toggleClass(secondLine, 'active');
            toggleClass(text, 'active');
            toggleClass(picture, 'active');

        }, 500)
    } else {
        toggleClass(secondLine, 'active');
        toggleClass(text, 'active');
        toggleClass(picture, 'active');

        setTimeout(() => {
            toggleClass(line, 'active');

        }, 500)
    }

}

const linesAnimationsInTurn = () => {
    for (let i = 0; i < 5; i++) {
        if (i === 0) {
            linesAnimation(lines[i], secondLines[i], texts[i], pictures[i]);
        } else {
            setTimeout(() => linesAnimation(lines[i], secondLines[i], texts[i], pictures[i]), 500 * i);

        }
    }
}

const getOffsetLines = () => {
    return sectionLines.offsetTop;
}

const dots = document.querySelectorAll('.dot');


dots.forEach(e => {
    e.addEventListener('click', () => {
        let num = e.parentNode.getAttribute('id').slice(-1);
        const line = document.querySelector(`#line-${num}`),
            secondLine = document.querySelector(`#sec-text-${num}`),
            text = secondLine.querySelector(`span`),
            picture = document.querySelector(`#sec_${num}`);
        linesAnimationToggle(line, secondLine, text, picture);
    })
})

// document.addEventListener('scroll', () => {
//     if (window.pageYOffset > getOffsetLines() - 400){
//         allLinesAnimationOneTime()
//     }
// })


