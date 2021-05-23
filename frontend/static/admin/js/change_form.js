'use strict';
{
    const inputTags = ['BUTTON', 'INPUT', 'SELECT', 'TEXTAREA'];
    const modelName = document.getElementById('django-admin-form-add-constants').dataset.modelName;
    if (modelName) {
        const form = document.getElementById(modelName + '_form');
        for (const element of form.elements) {
            // HTMLElement.offsetParent returns null when the element is not
            // rendered.
            if (inputTags.includes(element.tagName) && !element.disabled && element.offsetParent) {
                element.focus();
                break;
            }
        }
    }
}

document.querySelector('#content-main form').addEventListener('submit', (e) => {
    document.querySelector('#container').insertAdjacentHTML('afterbegin', `<div id="loader-form">
            <span id="span-text">Идет сохранение. Пожалуйста подождите</span>
            <span class="img"><img class="spinner" src="/static/images/spinner.svg" width="30px"/></span>
            </div>`);
    document.querySelector('body').style.overflow = 'hidden';
    document.querySelector('#loader-form').style.cssText = `
            color=#fff;
        z-index: 999;
        position:fixed;
        height:100%;
        width:100%;
        display:flex;
        align-items:center;
        justify-content:center;
        flex-direction:column;
        background:rgba(0,0,0,0.5);
        `;
    document.querySelector('#span-text').style.color = '#fff';
})
