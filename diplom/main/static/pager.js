
$( document ).ready(function() {
    console.log( "ready!" );
});


var response;


$('.btn').on('click',
    (e)=>{
    $('.test').html('qqwwwwwwwww')
    $( ".test" ).load( "/page/1" );
    }
    )


//$('.btn').on('click',
//    (e)=>{
//    $('.test').html('qqwwwwwwwww')
//    $.get( "/page/1", function( r ) {
//            console.log( r );
//            $('.test').append(r)
//            });
//    }
//    )
