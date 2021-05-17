//

timeline = document.querySelector('#timeline-1');

const setTimeLineBackground = () => {
    if (document.documentElement.clientWidth > 2000) {
        bgImage = timeline.getAttribute('data-bg-3000-src');
    } else if (document.documentElement.clientWidth > 768) {
        bgImage = timeline.getAttribute('data-bg-src');
    } else {
        bgImage = timeline.getAttribute('data-bg-src-mobile');
    }

    timeline.style.backgroundImage = `url(${bgImage})`;
}

setTimeLineBackground()


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

window.addEventListener('resize', function () {
    swiperCatalog.params.slidesPerView = getCatalogSlidesPerView();
    swiperCatalog.params.spaceBetween = getCatalogSpaceBetween();
    // swiperCatalog.reInit();

});

// табы

const navItemsCatalog = document.querySelectorAll('.tabs-controls-item.catalog'),
    bodyItemsCatalog = document.querySelectorAll('.body-item.catalog'),
    navArrayCatalog = Array.prototype.slice.call(navItemsCatalog),
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
            let swiperCatalog = new Swiper(`#${swiperID}`, {
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
        }
        scrollToActiveTab(e, navArrayCatalog, catalogContainer);

    })
})

scrollToActiveTab(document.querySelector('.tabs-controls-item.container.active'), navArrayCatalog, catalogContainer);

// сколлбар табов

const tabs = document.querySelectorAll('.tabs-controls-wrapper');

const addScrollbar = () => {
    tabs.forEach(e => {
        if (e.querySelector('.tabs-slider').offsetWidth > e.querySelector('.container').offsetWidth) {
            e.classList.add('scroll');
        }
    })
}

addScrollbar()


