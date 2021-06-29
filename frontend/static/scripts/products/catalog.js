/**
    hystmodal
 */
!function(e){var t={};function n(i){if(t[i])return t[i].exports;var o=t[i]={i:i,l:!1,exports:{}};return e[i].call(o.exports,o,o.exports,n),o.l=!0,o.exports}n.m=e,n.c=t,n.d=function(e,t,i){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:i})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var i=Object.create(null);if(n.r(i),Object.defineProperty(i,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)n.d(i,o,function(t){return e[t]}.bind(null,o));return i},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s=1)}([function(e,t,n){"use strict";function i(){return(i=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var i in n)Object.prototype.hasOwnProperty.call(n,i)&&(e[i]=n[i])}return e}).apply(this,arguments)}function o(e,t){for(var n=0;n<t.length;n++){var i=t[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(e,i.key,i)}}n.d(t,"a",(function(){return l}));var s,r,a,l=function(){function e(t){!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,e);this.config=i({backscroll:!0,linkAttributeName:"data-hystmodal",closeOnOverlay:!0,closeOnEsc:!0,closeOnButton:!0,waitTransitions:!1,catchFocus:!0,fixedSelectors:"*[data-hystfixed]",beforeOpen:function(){},afterClose:function(){}},t),this.config.linkAttributeName&&this.init(),this._closeAfterTransition=this._closeAfterTransition.bind(this)}var t,n,s;return t=e,(n=[{key:"init",value:function(){this.isOpened=!1,this.openedWindow=!1,this.starter=!1,this._nextWindows=!1,this._scrollPosition=0,this._reopenTrigger=!1,this._overlayChecker=!1,this._isMoved=!1,this._focusElements=["a[href]","area[href]",'input:not([disabled]):not([type="hidden"]):not([aria-hidden])',"select:not([disabled]):not([aria-hidden])","textarea:not([disabled]):not([aria-hidden])","button:not([disabled]):not([aria-hidden])","iframe","object","embed","[contenteditable]",'[tabindex]:not([tabindex^="-"])'],this._modalBlock=!1,e._shadow||(e._shadow=document.createElement("button"),e._shadow.classList.add("hystmodal__shadow"),document.body.appendChild(e._shadow)),this.eventsFeeler()}},{key:"eventsFeeler",value:function(){document.addEventListener("click",function(e){var t=e.target.closest("["+this.config.linkAttributeName+"]");if(!this._isMoved&&t){e.preventDefault(),this.starter=t;var n=this.starter.getAttribute(this.config.linkAttributeName);return this._nextWindows=document.querySelector(n),void this.open()}this.config.closeOnButton&&e.target.closest("[data-hystclose]")&&this.close()}.bind(this)),this.config.closeOnOverlay&&(document.addEventListener("mousedown",function(e){!this._isMoved&&e.target instanceof Element&&!e.target.classList.contains("hystmodal__wrap")||(this._overlayChecker=!0)}.bind(this)),document.addEventListener("mouseup",function(e){if(!this._isMoved&&e.target instanceof Element&&this._overlayChecker&&e.target.classList.contains("hystmodal__wrap"))return e.preventDefault(),this._overlayChecker,void this.close();this._overlayChecker=!1}.bind(this))),window.addEventListener("keydown",function(e){if(!this._isMoved&&this.config.closeOnEsc&&27==e.which&&this.isOpened)return e.preventDefault(),void this.close();!this._isMoved&&this.config.catchFocus&&9==e.which&&this.isOpened&&this.focusCatcher(e)}.bind(this))}},{key:"open",value:function(t){if(t&&(this._nextWindows="string"==typeof t?document.querySelector(t):t),this._nextWindows){if(this.isOpened)return this._reopenTrigger=!0,void this.close();this.openedWindow=this._nextWindows,this._modalBlock=this.openedWindow.querySelector(".hystmodal__window"),this.config.beforeOpen(this),this._bodyScrollControl(),e._shadow.classList.add("hystmodal__shadow--show"),this.openedWindow.classList.add("hystmodal--active"),this.openedWindow.setAttribute("aria-hidden","false"),this.config.catchFocus&&this.focusContol(),this.isOpened=!0}else console.log("Warinig: hustModal selector is not found")}},{key:"close",value:function(){this.isOpened&&(this.config.waitTransitions?(this.openedWindow.classList.add("hystmodal--moved"),this._isMoved=!0,this.openedWindow.addEventListener("transitionend",this._closeAfterTransition),this.openedWindow.classList.remove("hystmodal--active")):(this.openedWindow.classList.remove("hystmodal--active"),this._closeAfterTransition()))}},{key:"_closeAfterTransition",value:function(){this.openedWindow.classList.remove("hystmodal--moved"),this.openedWindow.removeEventListener("transitionend",this._closeAfterTransition),this._isMoved=!1,e._shadow.classList.remove("hystmodal__shadow--show"),this.openedWindow.setAttribute("aria-hidden","true"),this.config.catchFocus&&this.focusContol(),this._bodyScrollControl(),this.isOpened=!1,this.openedWindow.scrollTop=0,this.config.afterClose(this),this._reopenTrigger&&(this._reopenTrigger=!1,this.open())}},{key:"focusContol",value:function(){var e=this.openedWindow.querySelectorAll(this._focusElements);this.isOpened&&this.starter?this.starter.focus():e.length&&e[0].focus()}},{key:"focusCatcher",value:function(e){var t=this.openedWindow.querySelectorAll(this._focusElements),n=Array.prototype.slice.call(t);if(this.openedWindow.contains(document.activeElement)){var i=n.indexOf(document.activeElement);console.log(i),e.shiftKey&&0===i&&(n[n.length-1].focus(),e.preventDefault()),e.shiftKey||i!==n.length-1||(n[0].focus(),e.preventDefault())}else n[0].focus(),e.preventDefault()}},{key:"_bodyScrollControl",value:function(){if(this.config.backscroll){var e=Array.prototype.slice.call(document.querySelectorAll(this.config.fixedSelectors)),t=document.documentElement;if(!0===this.isOpened)return t.classList.remove("hystmodal__opened"),t.style.marginRight="",e.map((function(e){e.style.marginRight=""})),window.scrollTo(0,this._scrollPosition),void(t.style.top="");this._scrollPosition=window.pageYOffset;var n=window.innerWidth-t.clientWidth;t.style.top=-this._scrollPosition+"px",n&&(t.style.marginRight=n+"px",e.map((function(e){e.style.marginRight=parseInt(getComputedStyle(e).marginRight)+n+"px"}))),t.classList.add("hystmodal__opened")}}}])&&o(t.prototype,n),s&&o(t,s),e}();a=!1,(r="_shadow")in(s=l)?Object.defineProperty(s,r,{value:a,enumerable:!0,configurable:!0,writable:!0}):s[r]=a},function(e,t,n){"use strict";n.r(t),function(e){var t=n(0);n(3),n(4);e.HystModal=t.a}.call(this,n(2))},function(e,t){var n;n=function(){return this}();try{n=n||new Function("return this")()}catch(e){"object"==typeof window&&(n=window)}e.exports=n},function(e,t){Element.prototype.matches||(Element.prototype.matches=Element.prototype.msMatchesSelector||Element.prototype.webkitMatchesSelector),Element.prototype.closest||(Element.prototype.closest=function(e){var t=this;do{if(t.matches(e))return t;t=t.parentElement||t.parentNode}while(null!==t&&1===t.nodeType);return null})},function(e,t,n){}]);

/**
 *
 *  lazy.min.js
 *
 */
!function (t, n) {
    "object" == typeof exports && "undefined" != typeof module ? module.exports = n() : "function" == typeof define && define.amd ? define(n) : (t = t || self).LazyLoad = n()
}(this, (function () {
    "use strict";

    function t() {
        return (t = Object.assign || function (t) {
            for (var n = 1; n < arguments.length; n++) {
                var e = arguments[n];
                for (var i in e) Object.prototype.hasOwnProperty.call(e, i) && (t[i] = e[i])
            }
            return t
        }).apply(this, arguments)
    }

    var n = "undefined" != typeof window,
        e = n && !("onscroll" in window) || "undefined" != typeof navigator && /(gle|ing|ro)bot|crawl|spider/i.test(navigator.userAgent),
        i = n && "IntersectionObserver" in window, o = n && "classList" in document.createElement("p"),
        r = n && window.devicePixelRatio > 1, a = {
            elements_selector: ".lazy",
            container: e || n ? document : null,
            threshold: 300,
            thresholds: null,
            data_src: "src",
            data_srcset: "srcset",
            data_sizes: "sizes",
            data_bg: "bg",
            data_bg_hidpi: "bg-hidpi",
            data_bg_multi: "bg-multi",
            data_bg_multi_hidpi: "bg-multi-hidpi",
            data_poster: "poster",
            class_applied: "applied",
            class_loading: "loading",
            class_loaded: "loaded",
            class_error: "error",
            class_entered: "entered",
            class_exited: "exited",
            unobserve_completed: !0,
            unobserve_entered: !1,
            cancel_on_exit: !0,
            callback_enter: null,
            callback_exit: null,
            callback_applied: null,
            callback_loading: null,
            callback_loaded: null,
            callback_error: null,
            callback_finish: null,
            callback_cancel: null,
            use_native: !1
        }, c = function (n) {
            return t({}, a, n)
        }, s = function (t, n) {
            var e, i = "LazyLoad::Initialized", o = new t(n);
            try {
                e = new CustomEvent(i, {detail: {instance: o}})
            } catch (t) {
                (e = document.createEvent("CustomEvent")).initCustomEvent(i, !1, !1, {instance: o})
            }
            window.dispatchEvent(e)
        }, l = "loading", u = "loaded", d = "applied", f = "error", _ = "native", g = "data-", v = "ll-status",
        p = function (t, n) {
            return t.getAttribute(g + n)
        }, b = function (t) {
            return p(t, v)
        }, h = function (t, n) {
            return function (t, n, e) {
                var i = "data-ll-status";
                null !== e ? t.setAttribute(i, e) : t.removeAttribute(i)
            }(t, 0, n)
        }, m = function (t) {
            return h(t, null)
        }, E = function (t) {
            return null === b(t)
        }, y = function (t) {
            return b(t) === _
        }, A = [l, u, d, f], I = function (t, n, e, i) {
            t && (void 0 === i ? void 0 === e ? t(n) : t(n, e) : t(n, e, i))
        }, L = function (t, n) {
            o ? t.classList.add(n) : t.className += (t.className ? " " : "") + n
        }, w = function (t, n) {
            o ? t.classList.remove(n) : t.className = t.className.replace(new RegExp("(^|\\s+)" + n + "(\\s+|$)"), " ").replace(/^\s+/, "").replace(/\s+$/, "")
        }, k = function (t) {
            return t.llTempImage
        }, O = function (t, n) {
            if (n) {
                var e = n._observer;
                e && e.unobserve(t)
            }
        }, x = function (t, n) {
            t && (t.loadingCount += n)
        }, z = function (t, n) {
            t && (t.toLoadCount = n)
        }, C = function (t) {
            for (var n, e = [], i = 0; n = t.children[i]; i += 1) "SOURCE" === n.tagName && e.push(n);
            return e
        }, N = function (t, n, e) {
            e && t.setAttribute(n, e)
        }, M = function (t, n) {
            t.removeAttribute(n)
        }, R = function (t) {
            return !!t.llOriginalAttrs
        }, G = function (t) {
            if (!R(t)) {
                var n = {};
                n.src = t.getAttribute("src"), n.srcset = t.getAttribute("srcset"), n.sizes = t.getAttribute("sizes"), t.llOriginalAttrs = n
            }
        }, T = function (t) {
            if (R(t)) {
                var n = t.llOriginalAttrs;
                N(t, "src", n.src), N(t, "srcset", n.srcset), N(t, "sizes", n.sizes)
            }
        }, j = function (t, n) {
            N(t, "sizes", p(t, n.data_sizes)), N(t, "srcset", p(t, n.data_srcset)), N(t, "src", p(t, n.data_src))
        }, D = function (t) {
            M(t, "src"), M(t, "srcset"), M(t, "sizes")
        }, F = function (t, n) {
            var e = t.parentNode;
            e && "PICTURE" === e.tagName && C(e).forEach(n)
        }, P = {
            IMG: function (t, n) {
                F(t, (function (t) {
                    G(t), j(t, n)
                })), G(t), j(t, n)
            }, IFRAME: function (t, n) {
                N(t, "src", p(t, n.data_src))
            }, VIDEO: function (t, n) {
                !function (t, e) {
                    C(t).forEach((function (t) {
                        N(t, "src", p(t, n.data_src))
                    }))
                }(t), N(t, "poster", p(t, n.data_poster)), N(t, "src", p(t, n.data_src)), t.load()
            }
        }, S = function (t, n) {
            var e = P[t.tagName];
            e && e(t, n)
        }, V = function (t, n, e) {
            x(e, 1), L(t, n.class_loading), h(t, l), I(n.callback_loading, t, e)
        }, U = ["IMG", "IFRAME", "VIDEO"], $ = function (t, n) {
            !n || function (t) {
                return t.loadingCount > 0
            }(n) || function (t) {
                return t.toLoadCount > 0
            }(n) || I(t.callback_finish, n)
        }, q = function (t, n, e) {
            t.addEventListener(n, e), t.llEvLisnrs[n] = e
        }, H = function (t, n, e) {
            t.removeEventListener(n, e)
        }, B = function (t) {
            return !!t.llEvLisnrs
        }, J = function (t) {
            if (B(t)) {
                var n = t.llEvLisnrs;
                for (var e in n) {
                    var i = n[e];
                    H(t, e, i)
                }
                delete t.llEvLisnrs
            }
        }, K = function (t, n, e) {
            !function (t) {
                delete t.llTempImage
            }(t), x(e, -1), function (t) {
                t && (t.toLoadCount -= 1)
            }(e), w(t, n.class_loading), n.unobserve_completed && O(t, e)
        }, Q = function (t, n, e) {
            var i = k(t) || t;
            B(i) || function (t, n, e) {
                B(t) || (t.llEvLisnrs = {});
                var i = "VIDEO" === t.tagName ? "loadeddata" : "load";
                q(t, i, n), q(t, "error", e)
            }(i, (function (o) {
                !function (t, n, e, i) {
                    var o = y(n);
                    K(n, e, i), L(n, e.class_loaded), h(n, u), I(e.callback_loaded, n, i), o || $(e, i)
                }(0, t, n, e), J(i)
            }), (function (o) {
                !function (t, n, e, i) {
                    var o = y(n);
                    K(n, e, i), L(n, e.class_error), h(n, f), I(e.callback_error, n, i), o || $(e, i)
                }(0, t, n, e), J(i)
            }))
        }, W = function (t, n, e) {
            !function (t) {
                t.llTempImage = document.createElement("IMG")
            }(t), Q(t, n, e), function (t, n, e) {
                var i = p(t, n.data_bg), o = p(t, n.data_bg_hidpi), a = r && o ? o : i;
                a && (t.style.backgroundImage = 'url("'.concat(a, '")'), k(t).setAttribute("src", a), V(t, n, e))
            }(t, n, e), function (t, n, e) {
                var i = p(t, n.data_bg_multi), o = p(t, n.data_bg_multi_hidpi), a = r && o ? o : i;
                a && (t.style.backgroundImage = a, function (t, n, e) {
                    L(t, n.class_applied), h(t, d), n.unobserve_completed && O(t, n), I(n.callback_applied, t, e)
                }(t, n, e))
            }(t, n, e)
        }, X = function (t, n, e) {
            !function (t) {
                return U.indexOf(t.tagName) > -1
            }(t) ? W(t, n, e) : function (t, n, e) {
                Q(t, n, e), S(t, n), V(t, n, e)
            }(t, n, e)
        }, Y = ["IMG", "IFRAME"], Z = function (t) {
            return t.use_native && "loading" in HTMLImageElement.prototype
        }, tt = function (t, n, e) {
            t.forEach((function (t) {
                return function (t) {
                    return t.isIntersecting || t.intersectionRatio > 0
                }(t) ? function (t, n, e, i) {
                    h(t, "entered"), L(t, e.class_entered), w(t, e.class_exited), function (t, n, e) {
                        n.unobserve_entered && O(t, e)
                    }(t, e, i), I(e.callback_enter, t, n, i), function (t) {
                        return A.indexOf(b(t)) >= 0
                    }(t) || X(t, e, i)
                }(t.target, t, n, e) : function (t, n, e, i) {
                    E(t) || (L(t, e.class_exited), function (t, n, e, i) {
                        e.cancel_on_exit && function (t) {
                            return b(t) === l
                        }(t) && "IMG" === t.tagName && (J(t), function (t) {
                            F(t, (function (t) {
                                D(t)
                            })), D(t)
                        }(t), function (t) {
                            F(t, (function (t) {
                                T(t)
                            })), T(t)
                        }(t), w(t, e.class_loading), x(i, -1), m(t), I(e.callback_cancel, t, n, i))
                    }(t, n, e, i), I(e.callback_exit, t, n, i))
                }(t.target, t, n, e)
            }))
        }, nt = function (t) {
            return Array.prototype.slice.call(t)
        }, et = function (t) {
            return t.container.querySelectorAll(t.elements_selector)
        }, it = function (t) {
            return function (t) {
                return b(t) === f
            }(t)
        }, ot = function (t, n) {
            return function (t) {
                return nt(t).filter(E)
            }(t || et(n))
        }, rt = function (t, e) {
            var o = c(t);
            this._settings = o, this.loadingCount = 0, function (t, n) {
                i && !Z(t) && (n._observer = new IntersectionObserver((function (e) {
                    tt(e, t, n)
                }), function (t) {
                    return {
                        root: t.container === document ? null : t.container,
                        rootMargin: t.thresholds || t.threshold + "px"
                    }
                }(t)))
            }(o, this), function (t, e) {
                n && window.addEventListener("online", (function () {
                    !function (t, n) {
                        var e;
                        (e = et(t), nt(e).filter(it)).forEach((function (n) {
                            w(n, t.class_error), m(n)
                        })), n.update()
                    }(t, e)
                }))
            }(o, this), this.update(e)
        };
    return rt.prototype = {
        update: function (t) {
            var n, o, r = this._settings, a = ot(t, r);
            z(this, a.length), !e && i ? Z(r) ? function (t, n, e) {
                t.forEach((function (t) {
                    -1 !== Y.indexOf(t.tagName) && (t.setAttribute("loading", "lazy"), function (t, n, e) {
                        Q(t, n, e), S(t, n), h(t, _)
                    }(t, n, e))
                })), z(e, 0)
            }(a, r, this) : (o = a, function (t) {
                t.disconnect()
            }(n = this._observer), function (t, n) {
                n.forEach((function (n) {
                    t.observe(n)
                }))
            }(n, o)) : this.loadAll(a)
        }, destroy: function () {
            this._observer && this._observer.disconnect(), et(this._settings).forEach((function (t) {
                delete t.llOriginalAttrs
            })), delete this._observer, delete this._settings, delete this.loadingCount, delete this.toLoadCount
        }, loadAll: function (t) {
            var n = this, e = this._settings;
            ot(t, e).forEach((function (t) {
                O(t, n), X(t, e, n)
            }))
        }
    }, rt.load = function (t, n) {
        var e = c(n);
        X(t, e)
    }, rt.resetStatus = function (t) {
        m(t)
    }, n && function (t, n) {
        if (n) if (n.length) for (var e, i = 0; e = n[i]; i += 1) s(t, e); else s(t, n)
    }(rt, window.lazyLoadOptions), rt
}));

// lazyLoad init

const lazyLoadInstance = new LazyLoad({});


/**  menu.js
 *
 */
window.addEventListener("scroll", () => {
    if (!document.querySelector('html').classList.contains('hystmodal__opened')) {
        document.querySelector("header").classList.toggle("sticky", window.scrollY > 0)
    }
});
const hamburger = document.querySelector(".hamburger"), menuUl = document.querySelector("header ul.main"),
    body = document.querySelector("body"), toggleMenuClassActive = () => {
        hamburger.classList.toggle("active"), menuUl.classList.toggle("active"), body.classList.toggle("menu-active")
    };
hamburger.addEventListener("click", toggleMenuClassActive);
const dropdownMenuItems = document.querySelectorAll(".dropdown-big"), removeClass = (e, s) => {
    e.classList.contains(s) && e.classList.remove(s)
}, addClass = (e, s) => {
    e.classList.contains(s) || e.classList.add(s)
}, setLiHeight = e => {
    const s = e.querySelectorAll(".ddb-li-body"), t = Array.prototype.slice.call(s).map(e => e.offsetHeight),
        o = Math.max(...t);
    s.forEach(e => e.style.height = `${o}px`)
}, showDropdown = (e, s) => {
    addClass(e, "active"), addClass(s, "active"), setLiHeight(e)
}, hideDropdown = (e, s) => {
    e.classList.contains("mouse-in") || (removeClass(e, "active"), removeClass(s, "active"))
}, mouseInDropdown = (e, s) => {
    e.addEventListener("mouseenter", () => addClass(e, "mouse-in")), e.addEventListener("mouseleave", () => {
        removeClass(e, "mouse-in"), removeClass(e, "active"), removeClass(s, "active")
    })
};
dropdownMenuItems.forEach(e => {
    const s = document.querySelector(`#${e.getAttribute("data-for")}`);
    e.addEventListener("mouseenter", () => showDropdown(s, e)), e.addEventListener("mouseleave", () => mouseInDropdown(s, e)), e.addEventListener("mouseleave", () => setTimeout(hideDropdown, 300, s, e))
});

/**
 * catalog
 *
 */
// табы

const navItems = document.querySelectorAll('.tabs-controls-item'),
    bodyItems = document.querySelectorAll('.body-item'),
    navArray = Array.prototype.slice.call(navItems),
    setActive = (e, itemList) => {
        itemList.forEach(el => {
            el.classList.remove('active');
        });
        e.classList.add('active');
    },
    scrollToActiveTab = (e) => {
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
    };


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

// modal

const individualProjectModal = new HystModal({
    linkAttributeName: "data-hystmodal",
    catchFocus: true,
    waitTransitions: true,
    closeOnEsc: true,
    beforeOpen: function (modal) {
        document.querySelector('html').classList.add('modal_opened');
    },
    afterClose: function (modal) {
        setTimeout(() => document.querySelector('html').classList.remove('modal_opened'), 50);
    },
});


// const showModalCards = document.querySelectorAll('[data-id="individual_project"]'),
//     showModalButtons = document.querySelectorAll('[data-id="individual_project"] a')
// modal = document.querySelector('.new_project_modal.ars-modal');
//
// showModalButtons.forEach(e => {
//     e.addEventListener('click', (evt) => evt.preventDefault())
// })
//
// showModalCards.forEach((e) => {
//     e.addEventListener('click', () => {
//             modal.classList.add('active');
//             document.querySelector('body').style.overflow = 'hidden';
//             // modal.style.overflow = 'scroll';
//             modal.style.top = pageYOffset + 'px';
//             // modal.style.height = modal.offsetHeight + 'px';
//             modal.querySelector('.ars_modal_body').style.height = modal.querySelector('.ars_modal_body').offsetHeight + 'px';
//             console.log(pageYOffset)
//         }
//     )
// })
//
// modal.addEventListener('click', evt => {
//     if (evt.target === modal || evt.target === document.querySelector('#close-info span')) {
//         modal.classList.remove('active');
//         document.querySelector('body').style.overflow = 'unset';
//     }
// })


// form and inputs

const form = document.querySelector('#form'),
    lengthFields = form.querySelectorAll('[data-length]'),
    onlyNumbersFields = form.querySelectorAll('[data-only-int]'),
    inputs = form.querySelectorAll('.input'),
    sendMessageButton = document.querySelector('#send-message'),
    spinner = sendMessageButton.querySelector('.spinner'),
    hideAfterSendElements = form.querySelectorAll('.hide-after-send'),
    blurLine = (inputElement, transition) => {
        inputElement.classList.add('blur-line');
        inputElement.classList.remove('focus-line');
        setTimeout(() => {
            inputElement.classList.add('jump');
            inputElement.classList.remove('blur-line');
            setTimeout(() => {
                inputElement.classList.remove('jump');
            }, 50)
        }, transition)
    },
    showSpinner = () => {
        spinner.classList.remove('hide');
        spinner.classList.add('show');
    },
    hideSpinner = () => {
        spinner.classList.add('hide');
        spinner.classList.remove('show');
    },
    choicesButtons = document.querySelectorAll('.choices div'),
    hasErrorMessage = (element) => {
        if (element.querySelector('.error-messaage')) {
            return true;
        }
        return false;
    },
    showErrorMessage = (element, errorMessage) => {
        if (!hasErrorMessage(element.parentNode)) {
            element.insertAdjacentHTML('afterEnd', `<span class="error-messaage">${errorMessage}</span>`);
        }
    },
    hideErrorMessage = (element) => {
        if (hasErrorMessage(element.parentNode)) {
            element.parentNode.querySelector('.error-messaage').parentNode.removeChild(element.parentNode.querySelector('.error-messaage'))
        }
    },
    showValidationError = (element, errorMessage) => {
        hideSpinner()
        element.classList.add('error');
        showErrorMessage(element, errorMessage)
    },
    addEventInput = (element) => {
        element.addEventListener('input', () => {
            element.classList.remove('error')
            hideErrorMessage(element)
        });
    },
    validationRequired = () => {
        const errorMessage = 'Это обязательное поле!';
        let result = []
        form.querySelectorAll('[data-required="data-required"]').forEach(e => {
            if (!e.value) {
                showValidationError(e, errorMessage);
                addEventInput(e);
                result.push(false);
            }
        })
        return !result.includes(false);
    },
    validationLength = () => {
        let result = []
        lengthFields.forEach(e => {
            const maxLength = parseInt(e.getAttribute('data-maxLength'));
            const errorMessage = `Максимальная количество символов ${maxLength}! `;
            if (e.value.length > maxLength) {
                showValidationError(e, errorMessage);
                addEventInput(e);
                result.push(false);
            }
            return true;
        })

        return !result.includes(false);
    },
    validationPhone = (input) => {
        const errorMessage = 'Пожалуйста, введите действительный номер телефона'
        if (!/^[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/.test(input.value)) {
            showValidationError(input, errorMessage);
            addEventInput(input);
            return false;
        }
        return true;
    },
    validationEmail = (input) => {
        const errorMessage = 'Пожалуйста, введите действительный e-mail'
        if (!/[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+/.test(input.value) && input.value) {
            showValidationError(input, errorMessage);
            addEventInput(input);
            return false;
        }
        return true;
    },
    validationChoices = () => {
        const choiceType = document.querySelector('.choices div.active').getAttribute('data-key');
        if (choiceType === 'whatsapp') {
            return validationPhone(form.querySelector('#input-whatsapp'));
        } else if (choiceType === 'phone') {
            return validationPhone(form.querySelector('#input-phone'));
        } else if (choiceType === 'email') {
            return validationEmail(form.querySelector('#input-email'));
        } else {
            return true;
        }
    },
    prohibitLetteEntry = (input) => {
        input.addEventListener('input', (e) => {
            if (e.target.value.match(/[^0-9]/g)) {
                e.target.value = e.target.value.replace(/[^0-9]/g, "");
            }
        });
    },
    formIsValid = () => {
        const requiredIsValid = validationRequired(),
            lengthIsValid = validationLength(),
            choiceIsValid = validationChoices();
        return requiredIsValid && choiceIsValid && lengthIsValid
    };


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

choicesButtons.forEach(e => {
    e.addEventListener('click', () => {
        if (!e.classList.contains('active')) {
            const activeChoice = document.querySelector('.choices .active'),
                inputChoiceValue = activeChoice.getAttribute('data-key'),
                inputChoiceValueNew = e.getAttribute('data-key');
            document.querySelector(`[data-value="${inputChoiceValue}"]`).classList.remove('active');
            document.querySelector(`[data-value="${inputChoiceValue}"] input`).removeAttribute('data-required');
            activeChoice.classList.remove('active', 'b-shadow');
            e.classList.add('active', 'b-shadow');
            document.querySelector(`[data-value="${inputChoiceValueNew}"]`).classList.add('active');
            document.querySelector(`[data-value="${inputChoiceValueNew}"] input`).setAttribute('data-required', 'data-required');
        }
    })
})

document.querySelector('#input-credit').checked = false;

document.querySelector('#credit-checkbox').addEventListener('click', (e) => {
    if (e.target.checked) {
        document.querySelector('#input-credit').parentNode.classList.add('active');
        document.querySelector('#input-credit').setAttribute('data-required', "data-required");
    } else {
        document.querySelector('#input-credit').parentNode.classList.remove('active');
        document.querySelector('#input-credit').removeAttribute('data-required');
    }

})

onlyNumbersFields.forEach(e => {
    prohibitLetteEntry(e);
})



const MessageAddUrl = `${window.location.origin}/nobots/api/v1/contact_forms/individual_project/add/`;

sendMessageButton.addEventListener('click', (e) => {
    e.preventDefault();
    if (document.querySelector('#error-server-message').classList.contains('show')) {
        document.querySelector('#error-server-message').classList.remove('show')
    }
    showSpinner()
    if (formIsValid()) {
        let type_of_contact, contact;
        const choiceType = document.querySelector('.choices div.active').getAttribute('data-key');
        if (choiceType === 'whatsapp') {
            type_of_contact = 'Whatsapp';
            contact = form.querySelector('#input-whatsapp').value;
        } else if (choiceType === 'telegram') {
            type_of_contact = 'Telegram';
            contact = form.querySelector('#input-telegram').value;
        } else if (choiceType === 'phone') {
            type_of_contact = 'Мобильный';
            contact = form.querySelector('#input-phone').value;
        } else if (choiceType === 'email') {
            type_of_contact = 'E-mail';
            contact = form.querySelector('#input-email').value;
        }
        const data = {
            'number_of_floors': form.querySelector('#input-floors').value,
            'area': form.querySelector('#input-area').value,
            'number_of_rooms': form.querySelector('#input-rooms').value,
            'number_of_bathrooms': form.querySelector('#input-bathrooms').value,
            'garage_is_needed': form.querySelector('#garage').checked,
            'credit_is_needed': form.querySelector('#credit-checkbox').checked,
            'credit_amount': form.querySelector('#input-credit').value || 0,
            'comment': form.querySelector('#input-comment').value,
            'username': form.querySelector('#input-name').value,
            'type_of_contact': type_of_contact,
            'contact': contact,
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

            }
        }).catch(() => {
            document.querySelector('#error-server-message').style.display = 'block';
            hideSpinner()
        }).finally(() => {
        });
    }
});


(function () {
        window['yandexChatWidgetCallback'] = function () {
            try {
                window.yandexChatWidget = new Ya.ChatWidget({
                    guid: '767e1a08-c6d1-9667-52a3-6a2de57fcc91',
                    buttonText: '',
                    title: 'Чат',
                    theme: 'light',
                    collapsedDesktop: 'never',
                    collapsedTouch: 'never'
                });
            } catch (e) {
            }
        };
        var n = document.getElementsByTagName('script')[0],
            s = document.createElement('script');
        s.async = true;
        s.charset = 'UTF-8';
        s.src = 'https://yastatic.net/s3/chat/widget.js';
        n.parentNode.insertBefore(s, n);
    })();
