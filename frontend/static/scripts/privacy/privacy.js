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
 *  privacy
 */
const accordionItems = document.querySelectorAll('.contentBx'),
    getHeight = function (el) {
        let el_style = window.getComputedStyle(el),
            el_display = el_style.display,
            el_max_height = el_style.maxHeight.replace('px', '').replace('%', ''),

            wanted_height = 0;

        // if its not hidden we just return normal height
        if (el_display !== 'none' && el_max_height !== '0') {
            return el.offsetHeight;
        }

        // the element is hidden so:
        // making the el block so we can meassure its height but still be hidden
        el.style.position = 'absolute';
        el.style.visibility = 'hidden';
        el.style.display = 'block';

        wanted_height = el.offsetHeight + 50;


        el.removeAttribute('style')
        el.style.height = '0';

        return wanted_height;
    };


// accordion init

accordionItems.forEach((e) => {
    e.setAttribute('data-height', `${getHeight(e.querySelector('.contentBx .content'))}px`);
    e.querySelector('.label').addEventListener('click', () => {
        if (e.classList.contains('active')) {
            e.classList.remove('active');
            e.querySelector('.contentBx .content').style.height = '0';
        } else {
            e.classList.add('active');
            e.querySelector('.contentBx .content').style.height = e.getAttribute('data-height');
        }

    })
})

window.addEventListener('resize', () => {
    console.log('resize')
    accordionItems.forEach((e) => {
        if (e.classList.contains('active')) {
            e.classList.remove('active');
            e.querySelector('.contentBx .content').style.height = '0';
        }
        e.removeAttribute('data-height');
        e.querySelector('.contentBx .content').removeAttribute('style')
        e.querySelector('.contentBx .content').style.display = 'none';
        dataHigh = getHeight(e.querySelector('.contentBx .content'))
        console.log(dataHigh)
        e.setAttribute('data-height', `${dataHigh}px`);
    })
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