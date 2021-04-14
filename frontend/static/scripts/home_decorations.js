"use strict";

// HOME DECORATIONS

const homeDecorations = {
    baseUrl: 'http://127.0.0.1:8000/api/v1/home_decorations/?',
    categoriesField: 'categories=',
    subcategoriesField: 'sub_categories=',
    typesField: 'type=',
    orderingField: 'ordering=',
    offsetField: 'offset=',   //начинается с нуля
    limitField: 'limit=12',
    url: '',
    allCheckboxes: [],
    checkedCheckboxes: [],
    getUrl: function () {
        this.url = `${this.baseUrl}${this.categoriesField}&${this.subcategoriesField}&${this.typesField}&${this.orderingField}&${this.offsetField}&${this.limitField}`;
    },
    HDCount: 0,
    countPages: 1,
    homeDecorationsList: [],
    getAllCheckboxes: function () {
        this.allCheckboxes = Array.prototype.slice.call(document.querySelectorAll('.type_for_hd'));
    },
    getCheckedCheckboxes: function () {
        this.checkedCheckboxes = this.allCheckboxes.filter(e => e.checked);
    },
    getFilterParams: function () {
        this.checkedCheckboxes.forEach(e => {
            console.log(e.dataset);
            this.categoriesField += e.dataset.category + ',';
            this.subcategoriesField += e.dataset.subcategory + ',';
            this.typesField += e.dataset.type + ',';
        })
        this.categoriesField = this.categoriesField.slice(0, -1);
        this.subcategoriesField = this.subcategoriesField.slice(0, -1);
        this.typesField = this.typesField.slice(0, -1);
    },
    getCardData: function (obj) {
        return {
            'name': obj.name,
            'picture': obj.picture,
            'url': obj.get_absolute_url,
            'type': obj.type.name,
            'type_url': obj.type.get_absolute_url,
            'sub_category': obj.type.sub_category.name,
            'sub_category_url': obj.type.sub_category.get_absolute_url,
            'category': obj.type.sub_category.category.hd_name,
            'category_url': obj.type.sub_category.category.get_absolute_url
        }
    },
    createCard: function (cardData) {
        const divItem = document.createElement('div');
        divItem.classList.add('col-md-6', 'col-xl-4');
        divItem.innerHTML = `
           <div class="item">
            <div class="product product-grid">
                <div class="product-img-wrap"><img
                        src="${cardData.picture}"
                        alt="" width="300" height="300"/>
                </div>
                <div class="product-caption">
                    <ul class="product-categories">
                        <li><a href="${cardData.category_url}">${cardData.category}</a></li>
                        <li><a href="${cardData.sub_category_url}">${cardData.sub_category}</a></li>
                        <li><a href="${cardData.type_url}">${cardData.type}</a></li>
                    </ul>
                    <h6 class="product-title"><a href="${cardData.url}">${cardData.name}</a></h6>
                    </p><a class="button-gray-light-outline button button-icon button-icon-left"
                           href="${cardData.url}"><span
                        class="icon icon-md"></span><span>ПОДРОБНЕЕ</span></a>
                </div>
            </div>
            </div>
        `;
        return divItem
    },
    getData: function () {
        fetch(this.url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        }).then(data => {
            if (data['ok']) {
                console.log(`Success`);
                data.json().then(json => {
                    console.log(json);
                    json.results.forEach(e => {
                        const div = this.createCard(this.getCardData(e));
                        const wrapper = document.querySelector('.row.justify-content-sm-center.row-70')
                        wrapper.appendChild(div);
                    });
                })
            } else {
                console.log(`Error \n${data}`)
            }
        }).catch(() => {
            console.log(`Server Error \n ${data}`)
        }).finally(() => {
            console.log('finally')
        });
    },
    setDefaultParams: function () {
        this.categoriesField = 'categories=';
        this.subcategoriesField = 'sub_categories=';
        this.typesField = 'type=';
        this.orderingField = 'ordering=';
        this.offsetField = 'offset=';
        this.limitField = 'limit=12';
    },


    render: function () {
        this.getAllCheckboxes();
        this.getCheckedCheckboxes();
        this.getFilterParams();
        this.getUrl();
        this.getData();

        this.setDefaultParams();
    }
};

// console.log(homeDecorations.getUrl());
// homeDecorations.getAllCheckboxes();
// console.log(homeDecorations.allCheckboxes);
// homeDecorations.getCheckedCheckboxes();
// console.log(homeDecorations.checkedCheckboxes);
// homeDecorations.getFilterParams();
// console.log(homeDecorations.categoriesField)
// console.log(homeDecorations.subcategoriesField)
// console.log(homeDecorations.typesField)
// console.log(homeDecorations.getUrl())

homeDecorations.render();
