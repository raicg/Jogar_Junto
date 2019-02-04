function refresh() {
    $.ajax({
        url: 'games/chat/',
        success: function(data){ // if true (1)  
            $('#test').html(data);  
        }     
    });    
}
    
    $(function start(){
        refresh();
        setTimeout(start, 3000)
    });