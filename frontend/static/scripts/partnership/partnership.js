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
 *  partnership
 *
 */
const MessageAddUrl = `${window.location.origin}/nobots/api/v1/partnership/add/`,
    inputSelects = document.querySelectorAll('.input.select'),
    form = document.querySelector('#form'),
    sendMessageButton = document.querySelector('#send-message'),
    spinner = sendMessageButton.querySelector('.spinner'),
    selectArea = document.querySelector('#select-activity').parentNode,
    selectType = document.querySelector('#select-type-wrapper'),
    inputsAddAnimation = () => {
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
    },
    inputCompanyName = '<div class="input">\n' +
        '                            <input data-required="data-required" data-length type="text" name="company-name" id="company-name"\n' +
        '                                   class="text-input">\n' +
        '                            <label for="company-name" class="input-label">Название компании*</label>\n' +
        '                        </div>',
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
    showErrorMessageSelect = (element, errorMessage) => {
        if (!hasErrorMessage(element)) {
            element.insertAdjacentHTML('afterbegin', `<span class="error-messaage">${errorMessage}</span>`);
        }
    },
    hideErrorMessage = (element) => {
        if (hasErrorMessage(element.parentNode)) {
            element.parentNode.querySelector('.error-messaage').parentNode.removeChild(element.parentNode.querySelector('.error-messaage'))
        }
    },
    hideErrorMessageSelect = (element) => {
        if (hasErrorMessage(element)) {
            element.removeChild(element.querySelector('.error-messaage'))
        }
    },
    showValidationError = (element, errorMessage) => {
        hideSpinner()
        element.classList.add('error');
        showErrorMessage(element, errorMessage)
    },
    showValidationErrorSelect = (element, errorMessage) => {
        hideSpinner()
        element.classList.add('error');
        showErrorMessageSelect(element, errorMessage)
    },
    selectIsValid = (select) => {
        const placeholder = select.querySelector('span[data-placeholder]');
        const errorMessage = 'Это обязательное поле!';
        if (placeholder.getAttribute('data-placeholder') === placeholder.textContent) {
            showValidationErrorSelect(select, errorMessage);
            addEventInputSelect(select);
            return false;
        }
        return true;
    },
    addEventInput = (element) => {
        element.addEventListener('input', () => {
            element.classList.remove('error')
            hideErrorMessage(element)
        });
    },
    addEventInputSelect = (element) => {
        element.addEventListener('click', () => {
            element.classList.remove('error')
            hideErrorMessageSelect(element)
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
        const errorMessage = 'Максимальная длина 255 символов!'
        let result = []
        lengthFields.forEach(e => {
            if (e.value.length > 254) {
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
        if (!/^[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/.test(input.value) && input.value) {
            showValidationError(input, errorMessage);
            addEventInput(input);
            return false;
        }
        return true;
    },
    validationEmail = (input) => {
        const errorMessage = 'Пожалуйста, введите действительный e-mail'
        if (!/[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+/.test(input.value)) {
            showValidationError(input, errorMessage);
            addEventInput(input);
            return false;
        }
        return true;
    },
    validationSelect = () => {
        let result = [];
        inputSelects.forEach(e => {
            result.push(selectIsValid(e));
        })
        return !result.includes(false);
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
    prohibitLetterEntry = (input) => {
        input.addEventListener('input', (e) => {
            if (e.target.value.match(/[^0-9]/g)) {
                e.target.value = e.target.value.replace(/[^0-9]/g, "");
            }
        });
    },
    formIsValid = () => {
        const requiredIsValid = validationRequired(),
            lengthIsValid = validationLength(),
            choiceIsValid = validationChoices(),
            inputSelectsIsValid = validationSelect();
        return requiredIsValid && lengthIsValid && choiceIsValid && inputSelectsIsValid
    };

let requiredFields = form.querySelectorAll('[data-required="data-required"]'),
    lengthFields = form.querySelectorAll('[data-length]'),
    inputs = form.querySelectorAll('.input:not(.select)');


// selects init

inputSelects.forEach((eDiv) => {
    eDiv.querySelector('select').style.display = 'none';
    eDiv.querySelectorAll('option').forEach((eOption, i) => {
        if (i === 0) {
            eDiv.insertAdjacentHTML('afterbegin', `<div class="sel__box"></div>`);
            const placeholder = eOption.textContent;
            eDiv.insertAdjacentHTML('afterbegin', `<span data-placeholder="${placeholder}" class="sel__placeholder">${placeholder}</span>`);
            return;
        }
        eDiv.querySelector('div').insertAdjacentHTML('beforeend', `<span class="sel__box__options">${eOption.textContent}`);
    })
});

inputSelects.forEach(e => {
    e.addEventListener('click', () => {
        if (e.classList.contains('active')) {
            e.classList.remove('active');
        } else {
            e.classList.add('active');
        }
    })
});

const options = document.querySelectorAll('.sel__box__options');

options.forEach((e, i) => {
    e.addEventListener('click', () => {
        const txt = e.textContent;
        e.closest('.input.select').querySelectorAll('.sel__box__options').forEach(e => e.classList.remove('selected'));
        e.classList.add('selected');
        const select = e.closest('.input.select');
        select.querySelector(".sel__placeholder").textContent = txt;
    })
})

document.querySelector('body').addEventListener('click', (e) => {
    inputSelects.forEach(eSelect => {
        console.log(e.target.parentNode.parentNode)
        console.log(e.target)
        if (!(e.target === eSelect || e.target.parentNode.parentNode === eSelect) && eSelect.classList.contains('active')) {
            eSelect.classList.remove('active');
        }
    })
})

selectType.addEventListener('click', () => {
    const placeholder = selectType.querySelector('span[data-placeholder]');
    if (placeholder.textContent === 'компания') {
        if (!document.querySelector('#company-name')) {
            selectType.insertAdjacentHTML('afterend', inputCompanyName);
            inputs = form.querySelectorAll('.input:not(.select)');
            requiredFields = form.querySelectorAll('[data-required="data-required"]');
            lengthFields = form.querySelectorAll('[data-length]');
            inputsAddAnimation()
        }
    } else {
        if (document.querySelector('#company-name')) {
            form.removeChild(form.querySelector('#company-name').parentNode);
            inputs = form.querySelectorAll('.input:not(.select)');
            requiredFields = form.querySelectorAll('[data-required="data-required"]');
            lengthFields = form.querySelectorAll('[data-length]');
            inputsAddAnimation()
        }
    }
})

// choices init

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


// animation

inputsAddAnimation()

//prohibitLetterEntry

prohibitLetterEntry(form.querySelector('#input-whatsapp'));
prohibitLetterEntry(form.querySelector('#input-phone'));

//send form

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
        const data = () => {
            if ((!document.querySelector('#company-name'))) {
                return {
                    'area_of_activity': selectArea.querySelector('span[data-placeholder]').textContent,
                    'company_type': selectType.querySelector('span[data-placeholder]').textContent,
                    'firs_name': form.querySelector('#first-name').value,
                    'last_name': form.querySelector('#last-name').value,
                    'type_of_contact': type_of_contact,
                    'contact': contact
                }
            } else {
                return {
                    'area_of_activity': selectArea.querySelector('span[data-placeholder]').textContent,
                    'company_type': selectType.querySelector('span[data-placeholder]').textContent,
                    'company_name': form.querySelector('#company-name').value,
                    'firs_name': form.querySelector('#first-name').value,
                    'last_name': form.querySelector('#last-name').value,
                    'type_of_contact': type_of_contact,
                    'contact': contact
                }
            }
        };
        fetch(MessageAddUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(data())
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