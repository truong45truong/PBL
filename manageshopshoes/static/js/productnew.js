$(document).ready(()=>{
    $(".btn-add-size").click(function(){
        var size = $("#id_size").val()
        var quantity = $("#id_quantity").val()
        $("#select-option_id"+size).remove()
        var size_option = "<option id='select-option_id"+size+"' value='"+size+"-"+quantity+"'>"+size+"-"+quantity+"</option>"
        $("#id_select_size").append(size_option)
        console.log($("#id_select_size"))
    })
})