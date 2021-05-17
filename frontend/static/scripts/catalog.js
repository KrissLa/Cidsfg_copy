// табы

const navItems = document.querySelectorAll('.tabs-controls-item'),
    bodyItems = document.querySelectorAll('.body-item'),
    navArray = Array.prototype.slice.call(navItems);

const setActive = (e, itemList) => {
    itemList.forEach(el => {
        el.classList.remove('active');
    });
    e.classList.add('active');
}

const scrollToActiveTab = (e) => {
    let getWidth = 0;

    navArray.every(element => {
        if (e === element) {
            return false;
        } else {
            getWidth += element.offsetWidth;
            return true;
        }

    });
    document.querySelector('.tabs-controls-wrapper .container').scrollLeft = getWidth - 25;
}


navItems.forEach(e => {
    e.addEventListener('click', () => {
        if (!e.classList.contains('active')) {
            const tabId = e.getAttribute('data-for'),
                tabBodyItem = document.querySelector(`#${tabId}`);
            setActive(e, navItems);
            setActive(tabBodyItem, bodyItems);
        }
        scrollToActiveTab(e);

    })
})
scrollToActiveTab(document.querySelector('.tabs-controls-item.active'));
