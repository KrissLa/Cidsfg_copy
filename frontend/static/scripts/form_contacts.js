const MessageAddUrl = 'http://127.0.0.1:8000/api/v1/contacts/add/';

const form = document.querySelector('#form'),
    requiredFields = form.querySelectorAll('[data-required]'),
    lengthFields = form.querySelectorAll('[data-length]'),
    inputs = form.querySelectorAll('.input'),
    sendMessageButton = document.querySelector('#send-message'),
    spinner = sendMessageButton.querySelector('.spinner'),
    hideAfterSendElements = form.querySelectorAll('.hide-after-send');


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
}


inputs.forEach(e => {
    let inp = e.querySelector('input');
    if (!inp) {
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

const showSpinner = () => {
    spinner.classList.remove('hide');
    spinner.classList.add('show');
}

const hideSpinner = () => {
    spinner.classList.add('hide');
    spinner.classList.remove('show');
}


// Validation

const hasErrorMessage = (element) => {
    if (element.querySelector('.error-messaage')) {
        return true;
    }
    return false;
}

const showErrorMessage = (element, errorMessage) => {
    if (!hasErrorMessage(element.parentNode)) {
        element.insertAdjacentHTML('afterEnd', `<span class="error-messaage">${errorMessage}</span>`);
    }
}

const hideErrorMessage = (element) => {
    if (hasErrorMessage(element.parentNode)) {
        element.parentNode.querySelector('.error-messaage').parentNode.removeChild(element.parentNode.querySelector('.error-messaage'))
    }
}

const showValidationError = (element, errorMessage) => {
    hideSpinner()
    element.classList.add('error');
    showErrorMessage(element, errorMessage)
}

const addEventInput = (element) => {
    element.addEventListener('input', () => {
        element.classList.remove('error')
        hideErrorMessage(element)
    });
}

const validationRequired = () => {
    const errorMessage = 'Это обязательное поле!';
    let result = []
    requiredFields.forEach(e => {
        if (!e.value) {
            showValidationError(e, errorMessage);
            addEventInput(e);
            result.push(false);
        }
    })
    return !result.includes(false);
}

const validationLength = () => {
    const errorMessage = 'Максимальная длина 255 символов!'
    let result = []
    lengthFields.forEach(e => {
        if (e.value.length > 254) {
            showValidationError(e, errorMessage);
            addEventInput(e);
            result.push(false);
        }
        return true;
    })
    return !result.includes(false);
}

const validationPhone = (input) => {
    const errorMessage = 'Пожалуйста, введите действительный номер телефона'
    if (!/^[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/.test(input.value)) {
        showValidationError(input, errorMessage);
        addEventInput(input);
        return false;
    }
    return true;
}

const validationEmail = (input) => {
    const errorMessage = 'Пожалуйста, введите действительный e-mail'
    if (!/[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+/.test(input.value)) {
        showValidationError(input, errorMessage);
        addEventInput(input);
        return false;
    }
    return true;
}

form.querySelector('#input-phone').addEventListener('input', (e) => {
    console.log(e.target.value);
    if (e.target.value.match(/[^0-9]/g)) {
        e.target.value = e.target.value.replace(/[^0-9]/g, "");
    }
});


const formIsValid = () => {
    const requiredIsValid = validationRequired(),
        lengthIsValid = validationLength(),
        phoneIsValid = validationPhone(form.querySelector('#input-phone')),
        emailIsValid = validationEmail(form.querySelector('#input-email'));
    return requiredIsValid && lengthIsValid && phoneIsValid && emailIsValid
}


sendMessageButton.addEventListener('click', (e) => {
    e.preventDefault();
    if(document.querySelector('#error-server-message').classList.contains('show')){
        document.querySelector('#error-server-message').classList.remove('show')
    }
    showSpinner()
    console.log(formIsValid())
    if (formIsValid()) {
        console.log('Form is Valid');
        const data = {
            'username': form.querySelector('#input-name').value,
            'email': form.querySelector('#input-email').value,
            'phone_number': form.querySelector('#input-phone').value,
            'message': form.querySelector('#input-comment').value
        };
        fetch(MessageAddUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(data)
        }).then(response => {
            if (response['ok']) {
                form.reset()
                form.style.display = 'none';
                document.querySelector('#success-message').classList.add('show');
            } else {
                document.querySelector('#error-server-message').classList.add('show');
                hideSpinner()
                console.log('Response NOT OK!! NOT OK!!');
                console.log(response);
                console.log(response.status);

            }
        }).catch(() => {
            document.querySelector('#error-server-message').style.display = 'block';
            hideSpinner()
        }).finally(() => {
        });
    } else {
        console.log('NOT VALID NOT VALID');
    }
});
