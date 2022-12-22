$(document).ready(()=>{
    var url = $('.btn-to-payment').attr('href') +"/?productpay="
    sessionStorage.setItem('productPay',[])
    var number = $('.quantity-product').val()
    sessionStorage.setItem('transport','VietheoPost')
    $('.select-transport').change(function() {
        sessionStorage.setItem('transport',this.value.split('-')[1])
    })
    const uploadClickQuantity = () => {
        $('.tolal-product-select').empty()
        var sum = 0
        var listProductPay = sessionStorage.getItem('productPay').split(',')
        for (i of listProductPay ){
            sum += parseInt(i.split(":")[1])
            url += i+'-'
        }
        $('.btn-to-payment').attr('href',url)
        if(isNaN(sum) == true )$('.tolal-product-select').append(0)
        else $('.tolal-product-select').append(sum)  
    }
    $('.check-select-product').change(function() {
        if (sessionStorage.getItem('productPay')){
            var listProductPay = sessionStorage.getItem('productPay').split(',')
            if(this.checked == true){
                listProductPay.push(this.value+":"+$('.quantity-'+this.value).attr('value'))
            }
            if(this.checked == false){
                listProductPay= listProductPay.filter(item =>  item.split(":")[0] != this.value)
            }
            sessionStorage.setItem('productPay',listProductPay)
        }else {
            if(this.checked == true){
                sessionStorage.setItem('productPay',[this.value+":"+$('.quantity-'+this.value).attr('value')])
            }
        }
        uploadClickQuantity()
    })
})