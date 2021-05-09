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

    }, 750)
}
const linesAnimation = (line, secondLine, text, picture) => {
    addClass(line, 'active');
    setTimeout(() => {
        addClass(secondLine, 'active');
        addClass(text, 'active');
        addClass(picture, 'active');

    }, 750)
}

const linesAnimationsInTurn = () => {
    for (let i = 0; i < 5; i++) {
        if (i === 0) {
            linesAnimation(lines[i], secondLines[i], texts[i], pictures[i]);
        } else {
            setTimeout(() => linesAnimation(lines[i], secondLines[i], texts[i], pictures[i]), 750 * i);

        }
    }
}

const getOffsetLines = () => {
    console.log(sectionLines.offsetTop);
    return sectionLines.offsetTop;
}

document.addEventListener('scroll', () => {
    if (window.pageYOffset > getOffsetLines() - 400){
        linesAnimationsInTurn()
    }
})


// bigImage.forEach(e => e.addEventListener('click', linesAnimation));
bigImage.forEach(e => e.addEventListener('click', linesAnimationsInTurn));
// linesAnimation();

getOffsetLines()

