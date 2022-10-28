var list_shopping_cart =  JSON.parse(sessionStorage.getItem('list_shoppong_cart')) || [];
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