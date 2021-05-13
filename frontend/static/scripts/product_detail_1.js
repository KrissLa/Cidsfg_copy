const MessageAddUrl = 'http://127.0.0.1:8000/api/v1/houses/add_consultation_reqeust/';

//Swipers

const getCatalogSlidesPerView = () => {
    if (document.documentElement.clientWidth > 1199) {
        return 3
    } else if (document.documentElement.clientWidth > 768) {
        return 2
    } else {
        return 1
    }
}

const getCatalogSpaceBetween = () => {
    if (document.documentElement.clientWidth > 1199) {
        return 80
    } else if (document.documentElement.clientWidth > 992) {
        return 150
    } else if (document.documentElement.clientWidth > 768) {
        return 20
    } else {
        return 5
    }
}

const swiper = new Swiper('.swiper-container-detail', {
    pagination: {
        el: '.swiper-pagination',
        type: 'bullets',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',

    },
});

let swiperCatalog = new Swiper('#swiper1', {
    slidesPerView: getCatalogSlidesPerView(),
    spaceBetween: getCatalogSpaceBetween(),
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',

    },
});

swiperCatalog.params.slidesPerView = getCatalogSlidesPerView();
swiperCatalog.params.spaceBetween = getCatalogSpaceBetween();
swiperCatalog.init();

window.addEventListener('resize', function () {
    swiperCatalog.params.slidesPerView = getCatalogSlidesPerView();
    swiperCatalog.params.spaceBetween = getCatalogSpaceBetween();
    // swiperCatalog.reInit();

});

// табы

const navItems = document.querySelectorAll('.tabs-controls-item.info'),
    navItemsCatalog = document.querySelectorAll('.tabs-controls-item.catalog'),
    bodyItems = document.querySelectorAll('.body-item.info'),
    bodyItemsCatalog = document.querySelectorAll('.body-item.catalog'),
    navArray = Array.prototype.slice.call(navItems),
    navArrayCatalog = Array.prototype.slice.call(navItemsCatalog),
    infoContainer = document.querySelector('.tabs-controls-wrapper.info .container'),
    catalogContainer = document.querySelector('.tabs-controls-wrapper.catalog .container');

const setActive = (e, itemList) => {
    itemList.forEach(el => {
        el.classList.remove('active');
    });
    e.classList.add('active');
}

const scrollToActiveTab = (e, arr, container) => {
    let getWidth = 0;

    arr.every(element => {
        if (e === element) {
            return false;
        } else {
            getWidth += element.offsetWidth;
            return true;
        }

    });
    container.scrollLeft = getWidth - 25;
}


navItems.forEach(e => {
    e.addEventListener('click', () => {
        if (!e.classList.contains('active')) {
            const tabId = e.getAttribute('data-for'),
                tabBodyItem = document.querySelector(`#${tabId}`);
            setActive(e, navItems);
            setActive(tabBodyItem, bodyItems);
        }
        scrollToActiveTab(e, navArray, infoContainer);

    })
})

navItemsCatalog.forEach(e => {
    e.addEventListener('click', () => {
        if (!e.classList.contains('active')) {
            const tabId = e.getAttribute('data-for'),
                tabBodyItem = document.querySelector(`#${tabId}`);
            setActive(e, navItemsCatalog);
            setActive(tabBodyItem, bodyItemsCatalog);
            const swiperID = tabBodyItem.querySelector('.swiper-container-catalog').id;
            const nextID = tabBodyItem.querySelector('.swiper-button-next').id;
            const prevID = tabBodyItem.querySelector('.swiper-button-prev').id;
            swiperCatalog = new Swiper(`#${swiperID}`, {
                slidesPerView: getCatalogSlidesPerView(),
                spaceBetween: getCatalogSpaceBetween(),
                navigation: {
                    nextEl: `#${nextID}`,
                    prevEl: `#${prevID}`,

                },

            });
            window.addEventListener('resize', function () {
                swiperCatalog.params.slidesPerView = getCatalogSlidesPerView();
                swiperCatalog.params.spaceBetween = getCatalogSpaceBetween();
            });
            swiperCatalog.init();
        }
        scrollToActiveTab(e, navArrayCatalog, catalogContainer);

    })
})

scrollToActiveTab(document.querySelector('.tabs-controls-item.info.active'), navArray, infoContainer);
scrollToActiveTab(document.querySelector('.tabs-controls-item.container.active'), navArrayCatalog, catalogContainer);

//
const tabs = document.querySelectorAll('.tabs-controls-wrapper');

const addScrollbar = () => {
    tabs.forEach(e => {
        console.log(e);
        console.log(e.querySelector('.tabs-slider').offsetWidth);
        console.log(e.querySelector('.container').offsetWidth);
        console.log(window.clientWidth);
        if (e.querySelector('.tabs-slider').offsetWidth > e.querySelector('.container').offsetWidth) {
            e.classList.add('scroll');
        }
    })
}

addScrollbar()


//modal

const buttonShowRequestModal = document.querySelector('#show-request-info-modal'),
    bodyEl = document.querySelector('body'),
    html = document.querySelector('html'),
    buttonCloseInfo = document.querySelector('#close-info'),
    requestModal = document.querySelector('#modal-request-info');




const showModal = (modelSelector) => {
    bodyEl.classList.add('show-modal');
    modelSelector.classList.add('active');
    html.classList.add('modal-show');

}

const hideModal = (modelSelector) => {
    bodyEl.classList.remove('show-modal');
    modelSelector.classList.remove('active');
    html.classList.remove('modal-show');

}


// Модальное окно с консультацией
buttonShowRequestModal.addEventListener('click', (e) => {
    e.preventDefault();
    showModal(requestModal);

})

buttonCloseInfo.addEventListener('click', (e) => {
    hideModal(requestModal);
})

requestModal.addEventListener('click', (e) => {
    if (e.target === requestModal) {
        hideModal(requestModal);
    }
})



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
    if (!/[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+/.test(input.value) && input.value) {
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
            'message': form.querySelector('#input-comment').value,
            'house_name': document.querySelector('.breadcrumbs-custom__path .active').innerHTML
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






// const buttonForRequestInfo = document.querySelector('#show-request-info-modal'),
//     bodyEl = document.querySelector('body'),
//     requestInfoModal = document.querySelector('#modal-request-info'),
//     buttonCloseInfo = document.querySelector('#close-info'),
//
//     //Первое модальное окно со стоимостью
//     buttonForPriceInfo = document.querySelector('#show-price-info-modal'),
//     priceInfoModal = document.querySelector('#modal-price-info'),
//     buttonClosePriceInfo = document.querySelector('#close-price-info'),
//
//     //Второе модальное окно со стоимостью
//     buttonPriceNext = document.querySelector('#price-next'),
//     buttonPriceBack = document.querySelector('#price-back-2'),
//     priceModal2 = document.querySelector('#modal-price-info-2'),
//     buttonClosePriceModal2 = document.querySelector('#close-price-info-2'),
//     html = document.querySelector('html'),
//     navBar = document.querySelector('nav.rd-navbar'),
//     tabsNavItems = document.querySelectorAll('.nav-item'),
//
//     // Выбор планировки
//     selectLayout = document.querySelector('#layout'),
//
//     // Кнопки выбора отделки
//     addDecorationButtons = document.querySelectorAll('.add-decorations'),
//     selectDecorationsButtons = document.querySelectorAll('.decorations-choices.wall li'),
//     selectDecorationsInfoContainers = document.querySelectorAll('.decoration-info div'),
//     confirmDecorationsButtons = document.querySelectorAll('.decoration-info-header button'),
//
//     // модальное окно с инфой пользователя
//     openModalUserButton = document.querySelector('#price-next-2'),
//     userDataModal = document.querySelector('#modal-price-data'),
//     backToDecoration = document.querySelector('#price-back'),
//     closeUserDataModalButton = document.querySelector('#close-price-data');
//
//
// // Модальное окно с расчетом стоимости дома 1
// buttonPriceBack.addEventListener('click', (e) => {
//     hideModal(priceModal2);
//     showModal(priceInfoModal);
// })
// buttonForPriceInfo.addEventListener('click', (e) => {
//     showModal(priceInfoModal);
//
// })
//
// buttonClosePriceInfo.addEventListener('click', (e) => {
//     hideModal(priceInfoModal);
// })
//
// priceInfoModal.addEventListener('click', (e) => {
//     if (e.target === priceInfoModal) {
//         hideModal(priceInfoModal);
//     }
// })
//
// // Модальное окно с расчетом стоимости 2
//
// buttonPriceNext.addEventListener('click', (e) => {
//     hideModal(priceInfoModal);
//     showModal(priceModal2);
//
// })
//
// buttonClosePriceModal2.addEventListener('click', (e) => {
//     hideModal(priceModal2);
// })
//
// priceModal2.addEventListener('click', (e) => {
//     if (e.target === priceModal2) {
//         hideModal(priceModal2);
//     }
// })
//
// // Выбор планировки
// const onChangeSelectLayout = (e) => {
//     console.log(selectLayout.value);
//     if (selectLayout.value === 'standard-layout') {
//         document.querySelector('#standard-layout').classList.remove('hide');
//         document.querySelector('#personal-layout').classList.add('hide');
//     } else {
//         document.querySelector('#standard-layout').classList.add('hide');
//         document.querySelector('#personal-layout').classList.remove('hide');
//     }
// }
//
// $('#layout').on('change', onChangeSelectLayout);
//
//
// // Вызываем модальные окна с выбором отделок
//
// addDecorationButtons.forEach(e => {
//
//     e.addEventListener('click', (e) => {
//         const dataDecorations = e.target.getAttribute('data-decoration');
//         console.log(dataDecorations);
//         const modal = document.querySelector(`[data-for-decorations="${dataDecorations}"]`);
//         console.log(modal);
//         modal.classList.add('active');
//     })
// })
//
// // slider с выбором конкретной отделки
//
// console.log(selectDecorationsButtons);
//
// selectDecorationsButtons.forEach(e => {
//     e.addEventListener('click', e => {
//         if (!e.target.classList.contains('active')) {
//             selectDecorationsButtons.forEach(e => e.classList.remove('active'));
//             e.target.classList.add('active');
//             selectDecorationsInfoContainers.forEach(e => e.classList.remove('active'));
//             let attributeValue = e.target.getAttribute('data-for-item');
//             document.querySelector(`[data-item="${attributeValue}"]`).classList.add('active');
//         }
//     })
// })
//
// const parentsModal = document.querySelectorAll('.modal');
// for (let i = 0, parent; parent = parentsModal[i]; i++)
//     parent.addEventListener('click', e => {
//         if (e.target.hasAttribute('data-select-decoration')) {
//             const attributeValue = e.target.getAttribute('data-select-decoration');
//             const item = document.querySelector(`[data-item="${attributeValue}"]`);
//             const decorationTitle = item.querySelector('.decoration-info-title').textContent;
//             const decorationPrice = item.querySelector('.price span').textContent;
//             parent.classList.remove('active');
//             document.querySelector('[data-decoration="exterior-wall"]').innerHTML = 'Изменить';
//             document.querySelector('.modal-add p').innerHTML = `${decorationTitle} (${decorationPrice}р)`;
//         } else if (e.target.classList.contains('close') || e.target.classList.contains('modal')) {
//             parent.classList.remove('active');
//         }
//     });
//
// openModalUserButton.addEventListener('click', (e) => {
//     hideModal(priceModal2);
//     showModal(userDataModal);
// })
//
// backToDecoration.addEventListener('click', e => {
//     hideModal(userDataModal);
//     showModal(priceModal2);
// })
//
// closeUserDataModalButton.addEventListener('click', (e) => {
//     hideModal(userDataModal);
// })





