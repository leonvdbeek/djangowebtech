$(document).ready(() => {

  $('.container2').on('mouseenter', event => {
    $(event.currentTarget).children().siblings('.info').fadeIn(150);
    $(event.currentTarget).children('.fadeimage').fadeTo(400, 0.3);
  }).on('mouseleave', event => {
    $(event.currentTarget).children(".fadeimage").fadeTo(400, 1);
    $(event.currentTarget).children().siblings('.info').fadeOut(150);
  });
});
