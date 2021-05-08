

$( document ).ready(function() {
    $("#main").load( "/page/home" );
    $("#home").clear_action()
    $("#home").addClass("active")
    console.log( "ready!" );
});


(function( $ ){
   $.fn.clear_action = function() {
      $('#home').removeClass('active')
      $('#cases').removeClass('active')
      $('#clients').removeClass('active')
      $('#tasks').removeClass('active')
      $('#statistic').removeClass('active')
      $("#search").html('<input id="search_input" class="form-control" type="search" placeholder="Type search"><button id="search_btn" class="btn btn-secondary" class="btn"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16"><path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/></svg></button>')
      return this;
   };
})( jQuery );


$('#home').on('click',
    (e)=>{
    console.log( "home!" );
    $("#main").load( "/page/home" );
    $("#home").clear_action()
    $("#search").html('')
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

$('#statistic').on('click',
    (e)=>{
    console.log( "statistic!" );
    $("#main").load( "/page/statistic" );
    $("#statistic").clear_action()
    $("#statistic").addClass("active")
    }
    )


