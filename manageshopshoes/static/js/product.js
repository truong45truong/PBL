window.scrollTo(0, 800)
var page= window.location.search.replace("?page=","")
console.log(page)
$(".pagination li").eq(page).addClass("active-page")
$(document).ready(()=>{
    $("#add-to-cart").click(function(e){
        alert('Clicked');
        e.preventDefault();
        $.ajax({
            type:'POST',
            url:"http://127.0.0.1:8000/puma",
            data:
            {
                task:"truobg",
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(){
                alert('Success');
                    }
            })
        });
})