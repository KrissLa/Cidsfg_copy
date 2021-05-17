const MessageAddUrl = `${domain}/api/v1/partnership/add/`;

const inputSelects = document.querySelectorAll('.input.select');

inputSelects.forEach((eDiv) => {
    eDiv.querySelector('select').style.display = 'none';

    eDiv.querySelectorAll('option').forEach((eOption, i) => {
        if (i === 0) {

            eDiv.insertAdjacentHTML('afterbegin', `<div class="sel__box"></div>`);
            const placeholder = eOption.textContent;
            eDiv.insertAdjacentHTML('afterbegin', `<span data-placeholder="${placeholder}" class="sel__placeholder">${placeholder}</span>`);
            return;
        }
        eDiv.querySelector('div').insertAdjacentHTML('beforeend', `<span class="sel__box__options">${eOption.textContent}`);
    })
});

inputSelects.forEach(e => {
    e.addEventListener('click', () => {
        if (e.classList.contains('active')) {
            e.classList.remove('active');
        } else {
            e.classList.add('active');
        }
    })
});

const options = document.querySelectorAll('.sel__box__options')

options.forEach((e, i) => {
    e.addEventListener('click', () => {
        const txt = e.textContent;

        e.closest('.input.select').querySelectorAll('.sel__box__options').forEach(e => e.classList.remove('selected'));
        e.classList.add('selected');

        const select = e.closest('.input.select');
        select.querySelector(".sel__placeholder").textContent = txt;
    })
})

document.querySelector('body').addEventListener('click', (e) => {
    inputSelects.forEach(eSelect => {
        if (!(e.target === eSelect) && eSelect.classList.contains('active')) {
            eSelect.classList.remove('active');
        }
    })
})


const form = document.querySelector('#form'),
    sendMessageButton = document.querySelector('#send-message'),
    spinner = sendMessageButton.querySelector('.spinner'),
    selectArea = document.querySelector('#select-activity').parentNode,
    selectType = document.querySelector('#select-type-wrapper');

let requiredFields = form.querySelectorAll('[data-required]'),
    lengthFields = form.querySelectorAll('[data-length]'),
    inputs = form.querySelectorAll('.input:not(.select)');

const inputsAddAnimation = () => {
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
}

const inputCompanyName = '<div class="input">\n' +
    '                            <input data-required data-length type="text" name="company-name" id="company-name"\n' +
    '                                   class="text-input">\n' +
    '                            <label for="company-name" class="input-label">Название компании*</label>\n' +
    '                        </div>';



selectType.addEventListener('click', () => {
    const placeholder = selectType.querySelector('span[data-placeholder]');
    if (placeholder.textContent === 'компания') {
        if (!document.querySelector('#company-name')) {
            selectType.insertAdjacentHTML('afterend', inputCompanyName);
            inputs = form.querySelectorAll('.input:not(.select)');
            requiredFields = form.querySelectorAll('[data-required]');
            lengthFields = form.querySelectorAll('[data-length]');
            inputsAddAnimation()
        }

    } else {
        if (document.querySelector('#company-name')) {
            form.removeChild(form.querySelector('#company-name').parentNode);
            inputs = form.querySelectorAll('.input:not(.select)');
            requiredFields = form.querySelectorAll('[data-required]');
            lengthFields = form.querySelectorAll('[data-length]');
            inputsAddAnimation()
        }
    }
})

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

const showErrorMessageSelect = (element, errorMessage) => {
    if (!hasErrorMessage(element)) {
        element.insertAdjacentHTML('afterbegin', `<span class="error-messaage">${errorMessage}</span>`);
    }
}

const hideErrorMessage = (element) => {
    if (hasErrorMessage(element.parentNode)) {
        element.parentNode.querySelector('.error-messaage').parentNode.removeChild(element.parentNode.querySelector('.error-messaage'))
    }
}

const hideErrorMessageSelect = (element) => {
    if (hasErrorMessage(element)) {
        element.removeChild(element.querySelector('.error-messaage'))
    }
}

const showValidationError = (element, errorMessage) => {
    hideSpinner()
    element.classList.add('error');
    showErrorMessage(element, errorMessage)
}

const showValidationErrorSelect = (element, errorMessage) => {
    hideSpinner()
    element.classList.add('error');
    showErrorMessageSelect(element, errorMessage)
}

const selectIsValid = (select) => {
    const placeholder = select.querySelector('span[data-placeholder]');
    const errorMessage = 'Это обязательное поле!';
    if (placeholder.getAttribute('data-placeholder') === placeholder.textContent) {
        showValidationErrorSelect(select, errorMessage);
        addEventInputSelect(select);
        return false;
    }
    return true;
}

const addEventInput = (element) => {
    element.addEventListener('input', () => {
        element.classList.remove('error')
        hideErrorMessage(element)
    });
}

const addEventInputSelect = (element) => {
    element.addEventListener('click', () => {
        element.classList.remove('error')
        hideErrorMessageSelect(element)
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
    if (!/^[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/.test(input.value) && input.value) {
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

const validationSelect = () => {
    let result = [];
    inputSelects.forEach(e => {
        result.push(selectIsValid(e));
    })
    return !result.includes(false);
}


inputSelects.forEach(e => {
    e.addEventListener
});
form.querySelector('#input-phone').addEventListener('input', (e) => {
    if (e.target.value.match(/[^0-9]/g)) {
        e.target.value = e.target.value.replace(/[^0-9]/g, "");
    }
});

inputsAddAnimation()


const formIsValid = () => {
    const requiredIsValid = validationRequired(),
        lengthIsValid = validationLength(),
        phoneIsValid = validationPhone(form.querySelector('#input-phone')),
        emailIsValid = validationEmail(form.querySelector('#input-email')),
        inputSelectsIsValid = validationSelect();
    return requiredIsValid && lengthIsValid && phoneIsValid && emailIsValid && inputSelectsIsValid
}

sendMessageButton.addEventListener('click', (e) => {
    e.preventDefault();
    if (document.querySelector('#error-server-message').classList.contains('show')) {
        document.querySelector('#error-server-message').classList.remove('show')
    }
    showSpinner()
    if (formIsValid()) {
        const data = () => {
            if ((!document.querySelector('#company-name'))) {
                return {
                    'area_of_activity': selectArea.querySelector('span[data-placeholder]').textContent,
                    'company_type': selectType.querySelector('span[data-placeholder]').textContent,
                    'firs_name': form.querySelector('#first-name').value,
                    'last_name': form.querySelector('#last-name').value,
                    'email': form.querySelector('#input-email').value,
                    'phone_number': form.querySelector('#input-phone').value
                }
            } else {
                 return {
                    'area_of_activity': selectArea.querySelector('span[data-placeholder]').textContent,
                    'company_type': selectType.querySelector('span[data-placeholder]').textContent,
                    'company_name': form.querySelector('#company-name').value,
                    'firs_name': form.querySelector('#first-name').value,
                    'last_name': form.querySelector('#last-name').value,
                    'email': form.querySelector('#input-email').value,
                    'phone_number': form.querySelector('#input-phone').value
                }
            }

        };
        fetch(MessageAddUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(data())
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


