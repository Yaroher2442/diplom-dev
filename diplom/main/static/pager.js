
$( document ).ready(function() {
    console.log( "ready!" );
});


(function( $ ){
   $.fn.clear_action = function() {
      $('#home').removeClass('active')
      $('#clients').removeClass('active')
      $('#tasks').removeClass('active')
      $('#analytics').removeClass('active')
      return this;
   };
})( jQuery );


$('#home').on('click',
    (e)=>{
    $("#main").load( "/page/home" );
    console.log( "home!" );
    $("#home").clear_action()
    $("#home").addClass("active")
    }
    )

$('#clients').on('click',
    (e)=>{
    $("#main").load( "/page/clients" );
    console.log( "clients!" );
    $("#clients").clear_action()
    $("#clients").addClass("active")
    }
    )

$('#tasks').on('tasks',
    (e)=>{
    $("#main").load( "/page/tasks" );
    console.log( "tasks!" );
    $("#tasks").clear_action()
    $("#tasks").addClass("active")
    }
    )


$('#analytics').on('click',
    (e)=>{
    $("#main").load( "/page/analytics" );
    console.log( "analytics!" );
    $("#analytics").clear_action()
    $("#analytics").addClass("active")
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
