window.scrollTo(0, 800)
var page= window.location.search.replace("?page=","")
console.log(page)
$(".pagination li").eq(page).addClass("active-page")
$(document).ready(()=>{
    var list_shopping_cart =  JSON.parse(localStorage.getItem('list_shoppong_cart')) || [];
    $("#add-to-cart").click(function(e){
        // var newItem={
        //     'slug': $('#slug-product-detail').text(),
        //     'size': $('#size-product-detail').text(),
        //     'quantity': '10'
        // }
        var newItem = {
            "slug": "stan-smith-shoe-C2ZOP4",
            "name": "Stan Smith Shoe",
            "sex": 1,
            "description": "Stan Smith Shoe",
            "store_id": null,
            "category_id": 1,
            "prices": [
                {
                    "price": 5000000.0,
                    "sale": 11.0,
                    "datetime_create":"2022-10-21T23:12:07.055550Z"
                }
            ],
            "sizes": [
                {
                    "id": 1,
                    "size": 35,
                    "quantity": 12,
                },
                {
                    "id": 2,
                    "size": 36,
                    "quantity": 334,
                },
                {
                    "id": 3,
                    "size": 37,
                    "quantity": 0,
                },
                {
                    "id": 4,
                    "size": 38,
                    "quantity": 0,
                },
                {
                    "id": 5,
                    "size": 39,
                    "quantity": 0,
                },
                {
                    "id": 6,
                    "size": 40,
                    "quantity": 0,
                },
                {
                    "id": 7,
                    "size": 41,
                    "quantity": 0,
                },
                {
                    "id": 8,
                    "size": 42,
                    "quantity": 0,
                },
                {
                    "id": 9,
                    "size": 43,
                    "quantity": 0,
                },
                {
                    "id": 10,
                    "size": 44,
                    "quantity": 0,
                }
            ]
        }
        var headers = {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val() };
        list_shopping_cart.push(newItem)
        localStorage.setItem('list_shoppong_cart', JSON.stringify(list_shopping_cart));
        product=JSON.stringify(newItem)
        $.ajax({
            type:'POST',
            url:"http://127.0.0.1:8000/api/product/",
            contentType: "application/json; charset=utf-8",
            headers: headers,
            data: product
            ,
            
            success:function(){
                    }
        })
    });

})