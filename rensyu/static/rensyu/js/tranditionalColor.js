$(function(){

  // 컬러박스 클릭시
  $(".color-box").on("click", function() {
    let rgb_cd = $(this).data("rgb");
    console.log("rgb_cd", rgb_cd);

    // 표시용 배경색 변경
    $(".show-box").css("background-color", "#"+rgb_cd);

    // 색깔 명칭 변경
    $(".show-box-text h3").text($(this).children(".color-box-detail").text());

    let rnum = $(this).data("rnum");
    let gnum = $(this).data("gnum");
    let bnum = $(this).data("bnum");

    $(".detail-r-num").css("background-color", "rgb(" + rnum + ",0,0)");
    $(".detail-r-num").css("width", getRgbWidth(rnum)+"%");
    $(".detail-r-num").parent().attr("title", rnum); // tooltip

    $(".detail-g-num").css("background-color", "rgb(0," + gnum + ",0)");
    $(".detail-g-num").css("width", getRgbWidth(gnum)+"%");
    $(".detail-g-num").parent().attr("title", gnum); // tooltip

    $(".detail-b-num").css("background-color", "rgb(0,0," + bnum + ")");
    $(".detail-b-num").css("width", getRgbWidth(bnum)+"%");
    $(".detail-b-num").parent().attr("title", bnum); // tooltip

    // r
    // console.log($(this).children(".color-box-detail").text(), "색깔이름");

    // $(".show-box").animate({ "background-color": "#123123" }, "slow" );
    // $(".show-box").animate({
    //   left: '250px', 
    //   backgroundColor : 'white',
    // }, "slow");
    // $("div").animate({color: "red"});

  });


})

function getRgbWidth(num) {
  return (num / 255 * 100).toFixed(2);
}