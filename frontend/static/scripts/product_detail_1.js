const buttonForRequestInfo = document.querySelector('#show-request-info-modal'),
    body = document.querySelector('body'),
    requestInfoModal = document.querySelector('#modal-request-info'),
    buttonCloseInfo = document.querySelector('#close-info'),

    //Первое модальное окно со стоимостью
    buttonForPriceInfo = document.querySelector('#show-price-info-modal'),
    priceInfoModal = document.querySelector('#modal-price-info'),
    buttonClosePriceInfo = document.querySelector('#close-price-info'),

    //Второе модальное окно со стоимостью
    buttonPriceNext = document.querySelector('#price-next'),
    buttonPriceBack = document.querySelector('#price-back-2'),
    priceModal2 = document.querySelector('#modal-price-info-2'),
    buttonClosePriceModal2 = document.querySelector('#close-price-info-2'),
    html = document.querySelector('html'),
    navBar = document.querySelector('nav.rd-navbar'),
    tabsNavItems = document.querySelectorAll('.nav-item'),

    // Выбор планировки
    selectLayout = document.querySelector('#layout'),

    // Кнопки выбора отделки
    addDecorationButtons = document.querySelectorAll('.add-decorations'),
    selectDecorationsButtons = document.querySelectorAll('.decorations-choices.wall li'),
    selectDecorationsInfoContainers = document.querySelectorAll('.decoration-info div'),
    confirmDecorationsButtons = document.querySelectorAll('.decoration-info-header button'),

    // модальное окно с инфой пользователя
    openModalUserButton = document.querySelector('#price-next-2'),
    userDataModal = document.querySelector('#modal-price-data'),
    backToDecoration = document.querySelector('#price-back'),
    closeUserDataModalButton = document.querySelector('#close-price-data');


const showModal = (modelSelector) => {
    if (navBar.classList.contains('rd-navbar--is-stuck')) {
        navBar.style.paddingRight = '32px';
        navBar.style.trasition = 'unset';
    }
    body.classList.add('show-modal');
    modelSelector.classList.add('active');
    html.classList.add('modal-show');

}

const hideModal = (modelSelector) => {
    navBar.style.paddingRight = '15px';
    body.classList.remove('show-modal');
    modelSelector.classList.remove('active');
    html.classList.remove('modal-show');

}


// Модальное окно с консультацией
buttonForRequestInfo.addEventListener('click', (e) => {
    showModal(requestInfoModal);

})

buttonCloseInfo.addEventListener('click', (e) => {
    hideModal(requestInfoModal);
})

requestInfoModal.addEventListener('click', (e) => {
    if (e.target === requestInfoModal) {
        hideModal(requestInfoModal);
    }
})


// Модальное окно с расчетом стоимости дома 1
buttonPriceBack.addEventListener('click', (e) => {
    hideModal(priceModal2);
    showModal(priceInfoModal);
})
buttonForPriceInfo.addEventListener('click', (e) => {
    showModal(priceInfoModal);

})

buttonClosePriceInfo.addEventListener('click', (e) => {
    hideModal(priceInfoModal);
})

priceInfoModal.addEventListener('click', (e) => {
    if (e.target === priceInfoModal) {
        hideModal(priceInfoModal);
    }
})

// Модальное окно с расчетом стоимости 2

buttonPriceNext.addEventListener('click', (e) => {
    hideModal(priceInfoModal);
    showModal(priceModal2);

})

buttonClosePriceModal2.addEventListener('click', (e) => {
    hideModal(priceModal2);
})

priceModal2.addEventListener('click', (e) => {
    if (e.target === priceModal2) {
        hideModal(priceModal2);
    }
})

// Выбор планировки
const onChangeSelectLayout = (e) => {
    console.log(selectLayout.value);
    if (selectLayout.value === 'standard-layout') {
        document.querySelector('#standard-layout').classList.remove('hide');
        document.querySelector('#personal-layout').classList.add('hide');
    } else {
        document.querySelector('#standard-layout').classList.add('hide');
        document.querySelector('#personal-layout').classList.remove('hide');
    }
}

$('#layout').on('change', onChangeSelectLayout);


// Вызываем модальные окна с выбором отделок

addDecorationButtons.forEach(e => {

    e.addEventListener('click', (e) => {
        const dataDecorations = e.target.getAttribute('data-decoration');
        console.log(dataDecorations);
        const modal = document.querySelector(`[data-for-decorations="${dataDecorations}"]`);
        console.log(modal);
        modal.classList.add('active');
    })
})

// slider с выбором конкретной отделки

console.log(selectDecorationsButtons);

selectDecorationsButtons.forEach(e => {
    e.addEventListener('click', e => {
        if (!e.target.classList.contains('active')) {
            selectDecorationsButtons.forEach(e => e.classList.remove('active'));
            e.target.classList.add('active');
            selectDecorationsInfoContainers.forEach(e => e.classList.remove('active'));
            let attributeValue = e.target.getAttribute('data-for-item');
            document.querySelector(`[data-item="${attributeValue}"]`).classList.add('active');
        }
    })
})

const parentsModal = document.querySelectorAll('.modal');
for (let i = 0, parent; parent = parentsModal[i]; i++)
    parent.addEventListener('click', e => {
        if (e.target.hasAttribute('data-select-decoration')) {
            const attributeValue = e.target.getAttribute('data-select-decoration');
            const item = document.querySelector(`[data-item="${attributeValue}"]`);
            const decorationTitle = item.querySelector('.decoration-info-title').textContent;
            const decorationPrice = item.querySelector('.price span').textContent;
            parent.classList.remove('active');
            document.querySelector('[data-decoration="exterior-wall"]').innerHTML = 'Изменить';
            document.querySelector('.modal-add p').innerHTML = `${decorationTitle} (${decorationPrice}р)`;
        } else if  (e.target.classList.contains('close') || e.target.classList.contains('modal')) {
            parent.classList.remove('active');
        }
    });

openModalUserButton.addEventListener('click', (e) => {
    hideModal(priceModal2);
    showModal(userDataModal);
})

backToDecoration.addEventListener('click', e => {
    hideModal(userDataModal);
    showModal(priceModal2);
})

closeUserDataModalButton.addEventListener('click', (e) => {
    hideModal(userDataModal);
})




