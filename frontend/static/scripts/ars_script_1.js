"use strict";

//lazyload

const lazyLoadInstance = new LazyLoad({});


const vh = document.querySelectorAll('.vh');

const fixVhHeight = () => {
    if (document.documentElement.clientWidth < 768) {
        vh.forEach(e => {
            e.style.height = `${e.offsetHeight}px`;
        })
    }
}

fixVhHeight();

// document.addEventListener('resize', fixVhHeight);