
  $(document).ready(function(){
  $('#data').after('<div id="nav"></div>');
  $('#nav').after('<ul id="plist" class="pagination"></ul>')
  var rowsShown = 4;
  var rowsTotal = $('#data tbody tr').length;
  var numPages = rowsTotal/rowsShown;
  for(i = 0;i < numPages;i++) {
      var pageNum = i + 1;
          $('#plist').append('<li class="page-item"><a class="page-link" rel="'+i+'">'+pageNum+'</a></li>');
  }
  $('#data tbody tr').hide();
  $('#data tbody tr').slice(0, rowsShown).show();
  $('#plist a:first').addClass('active');
  $('#plist a').bind('click', function(){

      $('#plist a').removeClass('active');
      $(this).addClass('active');
      var currPage = $(this).attr('rel');
      var startItem = currPage * rowsShown;
      var endItem = startItem + rowsShown;
      $('#data tbody tr').css('opacity','0.0').hide().slice(startItem, endItem).
      css('display','table-row').animate({opacity:1}, 300);
  });
});
