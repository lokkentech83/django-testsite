$(function() {

  // 삭제버튼
  $(".del_item").on("click", function() {
    let dataId = $(this).data("id");
    let confirm = Util.common.confirmDialog('해당 항목을 삭제하시겠습니까? ( ID : ' + dataId + ' )');

    

    if (confirm) {
      var url = $(this).data("url");
      // alert(url);
      window.location.href = url;
    }
  })


});



//Util.common.confirmDialog('aaa');