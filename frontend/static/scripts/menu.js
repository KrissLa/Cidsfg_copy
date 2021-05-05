window.addEventListener('scroll', () => {
    const header = document.querySelector('header');
    header.classList.toggle("sticky", window.scrollY > 0);
})


const hamburger = document.querySelector('.hamburger'),
    menuUl = document.querySelector('header ul.main'),
    body = document.querySelector('body');


const toggleMenuClassActive = () => {
    hamburger.classList.toggle('active');
    menuUl.classList.toggle('active');
    body.classList.toggle('menu-active');
}

hamburger.addEventListener('click', toggleMenuClassActive);


//DRODOWN

const dropdownMenuItems = document.querySelectorAll('.dropdown-big');

const removeClass = (dropdown, className) => {
    if (dropdown.classList.contains(className)) {
        dropdown.classList.remove(className);
    }
}

const addClass = (dropdown, className) => {
    if (!dropdown.classList.contains(className)) {
        dropdown.classList.add(className);
    }
}

const setLiHeight = (dropdown) => {
    const dropdownItems = dropdown.querySelectorAll('.ddb-li-body'),
        DIArray = Array.prototype.slice.call(dropdownItems),
        heights = DIArray.map((e) => e.offsetHeight),
        maxHeight = Math.max(...heights);
    dropdownItems.forEach(e => e.style.height = `${maxHeight}px`);
}

const showDropdown = (dropdown, menuItem) => {
    addClass(dropdown, 'active');
    addClass(menuItem, 'active');
    setLiHeight(dropdown);
}

const hideDropdown = (dropdown, menuItem) => {
    if (!dropdown.classList.contains('mouse-in')) {
        removeClass(dropdown, 'active');
        removeClass(menuItem, 'active');
    }
}

const mouseInDropdown = (dropdown, menuItem) => {
    dropdown.addEventListener('mouseenter', () => addClass(dropdown, 'mouse-in'));

    dropdown.addEventListener('mouseleave', () => {
        removeClass(dropdown, 'mouse-in');
        removeClass(dropdown, 'active');
        removeClass(menuItem, 'active');
    });
}


dropdownMenuItems.forEach(e => {
    const dropdown = document.querySelector(`#${e.getAttribute('data-for')}`);

    e.addEventListener('mouseenter', () => showDropdown(dropdown, e));

    e.addEventListener('mouseleave', () => mouseInDropdown(dropdown, e));

    e.addEventListener('mouseleave', () => setTimeout(hideDropdown, 100, dropdown, e));
})