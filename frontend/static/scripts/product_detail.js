const buttonForRequestInfo = document.querySelector('#show-request-info-modal'),
    body = document.querySelector('body'),
    requestInfoModal = document.querySelector('#modal-request-info'),
    buttonCloseInfo = document.querySelector('#close-info'),
    buttonForPriceInfo = document.querySelector('#show-price-info-modal'),
    priceInfoModal = document.querySelector('#modal-price-info'),
    buttonClosePriceInfo = document.querySelector('#close-price-info'),
    buttonPriceNext = document.querySelector('#price-next'),
    buttonPriceBack = document.querySelector('#price-back'),
    priceDataModal = document.querySelector('#modal-price-data'),
    buttonClosePriceData = document.querySelector('#close-price-data'),
    html = document.querySelector('html'),
    navBar = document.querySelector('nav.rd-navbar');

const showModal = (modelSelector) => {
    if (navBar.classList.contains('rd-navbar--is-stuck')) {
        navBar.style.paddingRight = '32px';
        navBar.style.trasition = 'unset';
    }
    body.classList.add('show-modal');
    modelSelector.classList.add('active');
    html.classList.add('modal-show');
    console.log(navBar);

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
    if( e.target === requestInfoModal) {
        hideModal(requestInfoModal);
    }
})


// Модальное окно с расчетом стоимости дома 1
buttonPriceBack.addEventListener('click', (e) => {
    hideModal(priceDataModal);
    showModal(priceInfoModal);
})
buttonForPriceInfo.addEventListener('click', (e) => {
    showModal(priceInfoModal);

})

buttonClosePriceInfo.addEventListener('click', (e) => {
    hideModal(priceInfoModal);
})

priceInfoModal.addEventListener('click', (e) => {
    if( e.target === priceInfoModal) {
        hideModal(priceInfoModal);
    }
})

// Модальное окно с расчетом стоимости 2

buttonPriceNext.addEventListener('click', (e) => {
    hideModal(priceInfoModal);
    showModal(priceDataModal);

})

buttonClosePriceData.addEventListener('click', (e) => {
    hideModal(priceDataModal);
})

priceDataModal.addEventListener('click', (e) => {
    if( e.target === priceDataModal) {
        hideModal(priceDataModal);
    }
})

