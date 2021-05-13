"use strict";

//lazyload

const lazyLoadInstance = new LazyLoad({});


const vh = document.querySelectorAll('.vh');

const fixVhHeight = () => {
    console.log('sdfsdfsdfd');
    if (document.documentElement.clientWidth < 768) {
        vh.forEach(e => {
            console.log(e.offsetHeight);
            e.style.height = `${e.offsetHeight}px`;
        })
    }
}

fixVhHeight();

// document.addEventListener('resize', fixVhHeight);