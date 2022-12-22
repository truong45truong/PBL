const uploadClickQuantity = () => {
    $('.tolal-product-select').empty()
    var sum = 0
    var listProductPay = sessionStorage.getItem('productPay').split(',')
    for (i of listProductPay ){
        sum += parseInt(i.split(":")[1])
 
    }
    $('.tolal-product-select').append(sum)
}
const uploadSessionPayProduct = (slug,index) => {
    var listProductPay = sessionStorage.getItem('productPay').split(',')
    listProductPay= listProductPay.filter(item =>  item.split(":")[0] != slug)
    listProductPay.push(slug+":"+index)
    sessionStorage.setItem('productPay',listProductPay)
}
const uploadClickQuantityUp = (classInput,slug) =>{
    var index = parseInt($("."+classInput).attr('value')) +1
    $("."+classInput).attr('value',index)
    if (document.getElementById('checked-'+slug).checked == true){
        uploadSessionPayProduct(slug,index)
        uploadClickQuantity()
    }
}
const uploadClickQuantityDowm = (classInput,slug) =>{

    var index = parseInt($("."+classInput).attr('value')) - 1
    if(index > 0 ){
        $("."+classInput).attr('value',index)
        if (document.getElementById('checked-'+slug).checked == true){
            uploadSessionPayProduct(slug,index)
            uploadClickQuantity()
        }
    }
}
