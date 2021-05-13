// timeline

const timeline = document.querySelector('#timeline-1'),
    timelineItems = timeline.querySelectorAll('.timeline-item'),
    timelineActiveClass = "timeline-item--active",
    timelineItemIMGClass = "timeline__img";


const setActiveTimeline = (timelineItem) => {
    if (!timelineItem.classList.contains(timelineActiveClass)) {
        let bgImage;
        console.log(document.documentElement.clientWidth);
        if (document.documentElement.clientWidth > 768) {
            bgImage = timelineItem.querySelector(`.${timelineItemIMGClass}`).getAttribute('data-bg-src');
        } else {
            bgImage = timelineItem.querySelector(`.${timelineItemIMGClass}`).getAttribute('data-bg-src-mobile');
        }
        timelineItem.classList.add(timelineActiveClass);
        timeline.style.backgroundImage = `url(${bgImage})`;
        timeline.style.backgroundPosition = `center center`;
    }
}

const changeBGMobile = (timelineItem) => {
    let bgImage;
    bgImage = timelineItem.querySelector(`.${timelineItemIMGClass}`).getAttribute('data-bg-src-mobile');
    timeline.style.backgroundImage = `url(${bgImage})`;
    timeline.style.backgroundPosition = `center center`;
    timelineItem.classList.add('bg-active');
}

const getDiapasonsTimelineItems = (factor=2/3, first=500) => {
    const posTop = timeline.offsetTop;
    let diapasons = [];
    let maxPosPrev;
    timelineItems.forEach(e => {
        let minPos, maxPos;
        if (e === timelineItems[0]) {
            minPos = 0;
        } else {
            minPos = maxPosPrev;
        }

        if (e === timelineItems[-1]) {
            maxPos = 20000;
        }
        else {
            maxPos = e.offsetTop + posTop + e.offsetHeight * factor;
        }
        diapasons.push({'min': minPos, 'max': maxPos, 'el': e});
        maxPosPrev = maxPos;
    })
    console.log(diapasons)
    return diapasons
}

// const diapasons = getDiapasonsTimelineItems();

const scrollPage = (diapasons) => {
    diapasons.forEach(e => {
        if (window.pageYOffset > e.min && window.pageYOffset < e.max) {
            if (!e.el.classList.contains(timelineActiveClass)) {
                timeline.querySelector(`.${timelineActiveClass}`).classList.remove(timelineActiveClass);
                setActiveTimeline(e.el);
            }
        }
    })
}

const scrollPageMobile = (diapasons) => {
    diapasons.forEach(e => {
        if (window.pageYOffset > e.min && window.pageYOffset < e.max) {
            if (!e.el.classList.contains('bg-active')) {
                timeline.querySelector(`.bg-active`).classList.remove("bg-active");
                changeBGMobile(e.el);
            }
        }
    })
}

// document.addEventListener('scroll', scrollPage);

const initTimeLine = () => {

    if (document.documentElement.clientWidth > 768) {
        const diapasons = getDiapasonsTimelineItems();
        if (!document.querySelector(timelineActiveClass)) {
            setActiveTimeline(timelineItems[0]);
        }
        // document.addEventListener('scroll', () => scrollPage(diapasons));
    } else {
        const diapasons = getDiapasonsTimelineItems(1, 700);
        if (!document.querySelector('.bg-active')) {
            changeBGMobile(timelineItems[0]);
        }
        timelineItems.forEach(e => e.classList.add(timelineActiveClass));
        document.addEventListener('scroll', () => scrollPageMobile(diapasons));
    }

}

initTimeLine();

document.addEventListener('resize', initTimeLine);

// setActiveTimeline(timelineItems[0]);


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


