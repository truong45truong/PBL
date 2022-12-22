const uploadClickQuantity = () => {
    $('.tolal-product-select').empty()
    var listProductPay = sessionStorage.getItem('productPay').split(',')
    for (i of listProductPay ){
        console.log(i)
    }
}
export default uploadClickQuantity