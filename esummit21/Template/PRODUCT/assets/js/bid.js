$("#bid").click(function(e){
    e.preventDefault();
    var csrf = $("input[name=csrfmiddlewaretoken]").val();
        $.ajax({
            url:'',
            type:'post',
            data:{
                csrfmiddlewaretoken : csrf,
            },
            success:function(response){
                $("#change").text("₹ " + response.price + "K"),
                console.log(response.price)
                console.log(response.current)
                if (response.Name) {
                    $("#name").text(" " + response.Name + "")
                }
                
                if (response.err) {
                    alert(response.err)
                }
            }
        });
})