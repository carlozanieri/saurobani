$(document).ready(function(){

	var val = 1;

  $(".nav-bar").click(function(){


  	if (val == 1) {

	  	$("header nav").animate({
	    	'left' : '0'
	    });
	    val = 0;
  	}else{
  		val = 1;
  		$("header nav").animate({
		    'left' : '-100%'
		});
  	}



    return false;
  });

  // submenu
  $('.sub-menu').click(function(){
  	$(this).children('.children').slideToggle();
  })




}); 