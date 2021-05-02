

$( document ).ready(function() {
    console.log( "ready!" );
});


(function( $ ){
   $.fn.clear_action = function() {
      $('#home').removeClass('active')
      $('#cases').removeClass('active')
      $('#clients').removeClass('active')
      $('#tasks').removeClass('active')
      $('#analytics').removeClass('active')
      $('#settings').removeClass('active')
      return this;
   };
})( jQuery );


$('#home').on('click',
    (e)=>{
    console.log( "home!" );
    $("#main").load( "/page/home" );
    $("#home").clear_action()
    $("#home").addClass("active")
    }
    )

$('#cases').on('click',
    (e)=>{
    console.log( "cases!" );
    $("#main").load( "/page/cases" );
    $("#cases").clear_action()
    $("#cases").addClass("active")
    }
    )

$('#tasks').on('click',
    (e)=>{
    console.log( "tasks!" );
    $("#main").load( "/page/tasks" );
    $("#tasks").clear_action()
    $("#tasks").addClass("active")
    }
    )

$('#clients').on('click',
    (e)=>{
    console.log( "clients!" );
    $("#main").load( "/page/clients" );
    $("#clients").clear_action()
    $("#clients").addClass("active")
    }
    )

$('#analytics').on('click',
    (e)=>{
    console.log( "analytics!" );
    $("#main").load( "/page/analytics" );
    $("#analytics").clear_action()
    $("#analytics").addClass("active")
    }
    )

$('#settings').on('click',
    (e)=>{
    console.log( "analytics!" );
    $("#main").load( "/page/settings" );
    $("#settings").clear_action()
    $("#settings").addClass("active")
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
