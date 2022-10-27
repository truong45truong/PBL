window.scrollTo(0, 800)
var page= window.location.search.replace("?page=","")
console.log(page)
$(".pagination li").eq(page).addClass("active-page")
$(document).ready(()=>{
    var list_shopping_cart =  JSON.parse(sessionStorage.getItem('list_shoppong_cart')) || [];

    $("#add-to-cart").click(function(e){
        var newItem={
            'slug': $('#slug-product-detail').text(),
            'name':$('#name-product-detail').text(),
            'sex':$('#sex-product-detail').text(),
            'size': $('#size-product-detail').text(),
            'quantity': $('.quantityItem').text()
        }
        list_shopping_cart.push(newItem)
        sessionStorage.setItem('list_shoppong_cart', JSON.stringify(list_shopping_cart));
        $.ajax({
            type:'POST',
            url:"http://127.0.0.1:8000/order/shoppingcart/",
            data:
            {
                cart:JSON.stringify(list_shopping_cart),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(){
                    }
        })
    });

})