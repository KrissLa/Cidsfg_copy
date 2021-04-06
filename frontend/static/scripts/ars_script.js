"use strict";

const orderAddUrl = 'http://127.0.0.1:8000/api/v1/orders/add/';

const cuboThumbs = document.querySelectorAll('ul.thumb li'),
    circle = document.querySelector('.circle-bg');

function imgSlider(imageUrl) {
    document.querySelector('.cuboImage').src = imageUrl;
}

function changeCircleColor(color) {
    circle.style.cssText = "background-image: linear-gradient(to top, #30cfd0 0%, #330867 100%);";
}


console.log(cuboThumbs);

cuboThumbs.forEach(e => {
    e.addEventListener('click', (e) => {
        console.log(e.target);
        console.log(e.target.dataset.fullsrc);
        imgSlider(e.target.dataset.fullsrc);
        // changeCircleColor(e.target.dataset.color)
    })
})


const forms = document.querySelectorAll('form.name-phone-form'),
    formWrapper = document.querySelector('#form-wrapper'),
    phoneInput = document.querySelector('#contact-phone'),
    nameInput = document.querySelector('#contact-name'),
    agreeCheckbox = document.querySelector('#contact-agree');

const nameValidate = () => {
    let spanError;
    try {
        spanError = document.querySelector(".form-validation.name-required");
    } catch {
        spanError = null;
    }
    if (!nameInput.value) {
        if (!spanError) {
            nameInput.insertAdjacentHTML("afterEnd", "<span class=\"form-validation name-required\">Это обязательное поле</span>");
        }
        return false;
    } else {
        if (spanError) {
            spanError.remove();
        }
        return true;
    }
}

const phoneRequiredIsValid = () => {
    let spanError;
    try {
        spanError = document.querySelector(".form-validation.required-validation");
    } catch {
        spanError = null;
    }
    if (!phoneInput.value) {
        if (!spanError) {
            phoneInput.insertAdjacentHTML("afterEnd", "<span class=\"form-validation required-validation\">Это обязательное поле</span>");
        }
        return false;
    } else {
        if (spanError) {
            spanError.remove();
        }
        return true;
    }
}
const phoneValueIsValid = () => {
    let spanError;
    try {
        spanError = document.querySelector(".form-validation.digit-validation");
    } catch {
        spanError = null;
    }
    console.log(!phoneInput.value);
    if (!/^[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/.test(phoneInput.value) && phoneInput.value) {
        if (!spanError) {
            phoneInput.insertAdjacentHTML("afterEnd", "<span class=\"form-validation digit-validation\">Пожалуйста, введите корректный номер телефона</span>");
        }
        return false;
    } else {

        if (spanError) {
            spanError.remove();
        }
        return true;
    }
}

const phoneIsValid = () => {
    return phoneRequiredIsValid() && phoneValueIsValid();
}

const agreeCheckboxIsValid = () => {
    console.log(agreeCheckbox.checked);
    if (!agreeCheckbox.checked) {
        agreeCheckbox.parentElement.classList.add('checkbox-error');
        return false;
    } else {
        if (agreeCheckbox.parentElement.classList.contains('checkbox-error')) {
            agreeCheckbox.parentElement.classList.remove('checkbox-error');
        }
        return true;

    }
}

const formIsValid = () => {
    return phoneIsValid() && nameValidate() && agreeCheckboxIsValid();

}

const phoneInputAddPlus = () => {
    phoneInput.parentElement.classList.add("phone-number");
}

const phoneInputRemovePlus = () => {
    phoneInput.parentElement.classList.remove("phone-number");
}

nameInput.addEventListener('input', (e) => nameValidate());

phoneInput.addEventListener('focus', (e) => phoneInputAddPlus());
phoneInput.addEventListener('blur', (e) => {
    if (!phoneInput.value) {
        phoneInputRemovePlus();
    }
});

phoneInput.addEventListener('input', (e) => {
    console.log(e.target.value);
    if(e.target.value.match(/[^0-9]/g)){
            e.target.value = e.target.value.replace(/[^0-9]/g, "");
        }
});
phoneInput.addEventListener('input', (e) => phoneRequiredIsValid());
phoneInput.addEventListener('input', (e) => phoneValueIsValid());
agreeCheckbox.addEventListener('change', (e) => agreeCheckboxIsValid());

const message = {
    loading: '/frontend/static/images/spinner.svg',
    success: 'Спасибо! Скоро мы с вами свяжемся.',
    failure: 'Ошибка! Пожалуйста, попробуйте позже.'
};
console.log(forms);

forms.forEach(item => {
    postData(item);
});

const validateForm = () => {
    nameValidate();
    phoneRequiredIsValid();
    phoneValueIsValid();
    agreeCheckboxIsValid();
}

function postData(form) {
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        validateForm();
        if (formIsValid()) {
            console.log('форма ОК');
            let spinner = document.createElement('img');
            spinner.src = message.loading;
            spinner.classList.add('confirm-spinner');
            form.insertAdjacentElement('beforeend', spinner);

            const formData = new FormData(form);

            const object = {
                'username': nameInput.value,
                'phone_number': phoneInput.value
            };
            console.log(JSON.stringify(object))
            fetch(orderAddUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(object)
            }).then(data => {
                spinner.remove();
                if (data['ok']) {
                    let successMessage = document.createElement('div');
                    successMessage.innerText = message.success;
                    successMessage.classList.add('success-send');
                    form.insertAdjacentElement('beforeend', successMessage);
                    setTimeout(() => {
                    successMessage.remove();
                }, 4000);
                } else {
                    let errorMessage = document.createElement('div');
                    errorMessage.innerText = message.failure;
                    errorMessage.classList.add('error-send');
                    form.insertAdjacentElement('beforeend', errorMessage);
                    setTimeout(() => {
                    errorMessage.remove();
                }, 4000);
                }
            }).catch(() => {
                let errorMessage = document.createElement('div');
                errorMessage.innerText = message.failure;
                errorMessage.classList.add('error-send');
                form.insertAdjacentElement('beforeend', errorMessage);
                setTimeout(() => {
                    errorMessage.remove();
                }, 4000);
            }).finally(() => {
                form.reset()
                phoneInputRemovePlus();
            });
        }
    });
}