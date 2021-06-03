const MessageAddUrl = `${window.location.origin}/api/v1/contacts/add/`;

const form = document.querySelector('#form'),
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

//Contact choice

const choicesButtons = document.querySelectorAll('.choices div');


choicesButtons.forEach(e => {
    e.addEventListener('click', () => {
        if (!e.classList.contains('active')) {
            const activeChoice = document.querySelector('.choices .active'),
                inputChoiceValue = activeChoice.getAttribute('data-key'),
                inputChoiceValueNew = e.getAttribute('data-key');
            document.querySelector(`[data-value="${inputChoiceValue}"]`).classList.remove('active');
            document.querySelector(`[data-value="${inputChoiceValue}"] input`).removeAttribute('data-required');
            activeChoice.classList.remove('active', 'b-shadow');
            e.classList.add('active', 'b-shadow');
            document.querySelector(`[data-value="${inputChoiceValueNew}"]`).classList.add('active');
            document.querySelector(`[data-value="${inputChoiceValueNew}"] input`).setAttribute('data-required', 'data-required');
        }
    })
})


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
    form.querySelectorAll('[data-required="data-required"]').forEach(e => {
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

const validationChoices = () => {
    const choiceType = document.querySelector('.choices div.active').getAttribute('data-key');
    if (choiceType === 'whatsapp') {
        return validationPhone(form.querySelector('#input-whatsapp'));
    } else if (choiceType === 'phone') {
        return validationPhone(form.querySelector('#input-phone'));
    } else if (choiceType === 'email') {
        return validationEmail(form.querySelector('#input-email'));
    } else {
        return true;
    }
}

const prohibitLetteEntry = (input) => {
    input.addEventListener('input', (e) => {
        if (e.target.value.match(/[^0-9]/g)) {
            e.target.value = e.target.value.replace(/[^0-9]/g, "");
        }
    });
}

prohibitLetteEntry(form.querySelector('#input-whatsapp'));
prohibitLetteEntry(form.querySelector('#input-phone'));


const formIsValid = () => {
    const requiredIsValid = validationRequired(),
        lengthIsValid = validationLength(),
        choiceIsValid = validationChoices();
    return requiredIsValid && choiceIsValid && lengthIsValid
}


sendMessageButton.addEventListener('click', (e) => {
    e.preventDefault();
    if (document.querySelector('#error-server-message').classList.contains('show')) {
        document.querySelector('#error-server-message').classList.remove('show')
    }
    showSpinner()
    if (formIsValid()) {
        let type_of_contact, contact;
        const choiceType = document.querySelector('.choices div.active').getAttribute('data-key');
        if (choiceType === 'whatsapp') {
            type_of_contact = 'Whatsapp';
            contact = form.querySelector('#input-whatsapp').value;
        } else if (choiceType === 'telegram') {
            type_of_contact = 'Telegram';
            contact = form.querySelector('#input-telegram').value;
        } else if (choiceType === 'phone') {
            type_of_contact = 'Мобильный';
            contact = form.querySelector('#input-phone').value;
        } else if (choiceType === 'email') {
            type_of_contact = 'E-mail';
            contact = form.querySelector('#input-email').value;
        }
        const data = {
            'username': form.querySelector('#input-name').value,
            'type_of_contact': type_of_contact,
            'contact': contact,
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

            }
        }).catch(() => {
            document.querySelector('#error-server-message').style.display = 'block';
            hideSpinner()
        }).finally(() => {
        });
    }
});
