function viewport(){
    var st = $(window).scrollTop();
    var wh = $(window).height();
    
    var dif = $("nav").height() / $(document).height();
  
    $(".reference").css({
      'height': (wh * dif),
      'top': (st * dif)
    });
  }
  
  viewport();
  
  $(window).resize(function(){
    viewport();
  });
  
  $(window).scroll(function(){
    viewport();
  });
  
  $(document).on('click', 'a[href^="#"]', function (event) {
      event.preventDefault();
  
      $('html, body').animate({
          scrollTop: $($.attr(this, 'href')).offset().top
      }, 500);
  });