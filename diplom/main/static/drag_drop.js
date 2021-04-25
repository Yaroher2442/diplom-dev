$( init );
function init() {
  $( ".droppable-area1, .droppable-area2 , .droppable-area3, .droppable-area4" ).sortable({
      connectWith: ".connected-sortable",
      scroll: true,
      stop : function(event, ui) {
        var new_elem=document.elementFromPoint(event.originalEvent.clientX,event.originalEvent.clientY);
            $("div").each(function(i,elem){
            if ($(this).hasClass("overflow-auto")){
                 if ($.contains(elem,new_elem)){
                     console.log(new_elem);
                     console.log(new_elem.id);
                     item = {}
                     item ["container"] = elem.id;
                     item ["elem"] = new_elem.id;
                     $.ajax({
                        type: "POST",
                        url: "/DragDrop",
                        data: JSON.stringify(item),

                        contentType: 'application/json'
                        });
                 }
            }
        })
      },
    }).disableSelection();
}