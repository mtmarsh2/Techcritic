 $( document ).ready(function() {
     $('.like_button').click(function(event){
        elem = $(this);
    event.preventDefault();
    var _dir = $(this).attr("val");
    var _id = $($(this).parent().parent().children()[0]).text()
    $.post('http://localhost:8000/update_likes/', {_dir: _dir, _id:_id}, function(data){
            if (_dir == "up") {
                valuee = parseInt($($(elem).siblings(".likes_count")[0]).text()) + 1
                $($(elem).siblings(".likes_count")[0]).text(valuee.toString())
            } else {
                valuee = parseInt($($(elem).siblings(".likes_count")[0]).text()) - 1
                $($(elem).siblings(".likes_count")[0]).text(valuee.toString())
            }
              
           });
});
});

