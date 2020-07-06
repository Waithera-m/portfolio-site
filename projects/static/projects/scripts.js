$(document).ready(function(){
    $(".gallery").mouseover(function(){
        $("$overlay").show();
    }).mouseout(function(){
        ("#overlay").hide();
    });
})