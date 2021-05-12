const inputs = document.querySelectorAll('.input');

console.log(inputs);


const blurLine = (inputElement, transition) => {

    inputElement.classList.add('blur-line');
    inputElement.classList.remove('focus-line');
    setTimeout(() => {
        inputElement.classList.add('jump');
        inputElement.classList.remove('blur-line');

        setTimeout(() => {
            inputElement.classList.remove('jump');


        }, 50)

    }, transition)

    // inputElement.classList.remove('focus-line');
    //
    // setTimeout(() => {
    //     inputElement.classList.remove('jump');
    //
    // }, transition)

}


inputs.forEach(e => {
    let inp = e.querySelector('input');
    if (!inp){
        inp = e.querySelector('textarea');
    }
    inp.addEventListener('focus', (event) => {
        e.classList.add('focus');
        e.classList.add('focus-line');
    });
    inp.addEventListener('blur', (event) => {
        if (!inp.value) {
            e.classList.remove('focus');
        }
        blurLine(e, 400);

    });
})