//javascript comment 

$(function() {
    //Executed when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        //$(this) : Self element, namely div.js-menu-icon
        // next() : Next to div.js-menu-icon
        //toggle() : Swithc show and hide
        $(this).next().toggle();  
    })



})
