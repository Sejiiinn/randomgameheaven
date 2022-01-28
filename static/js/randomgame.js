$(".button").css("width", ($("#num1").width()+30));
  
//not a perfect random number function, 
//just does what I need it to
//only use for integers 1-10, otherwise LOOP CAN'T BREAK 
function randInt(min, max){
  var x = Math.floor((Math.random()*10)+1);
  while ((x<min) || (x>max)) {
    x = Math.floor((Math.random()*10)+1);
  }
  return x;
}

function clearOptions() {
  $(".option").hide();
  $(".option").css("top", "-50px");
}

var scrolledIDs = [];

//scrolls element after given delay in milliseconds  여기서 갯수 추가해야함
function scroll(delay, quitArg){
    var IDNum = randInt(2,9);  
    //reassign randNum if already scrolled
    while (!(scrolledIDs.indexOf(IDNum) === -1)) {
      IDNum = randInt(2,9);
    }
    
    var id = "#num"+IDNum.toString();
    var width = ($(id).width()+30)+"px";
    //scroll unless on final option
    $(id).delay(delay).show(0, function(){
     
      $(".button").css("width", width);
      
      if (quitArg) {
        $(id).css("top", "0");
      } else {
        $(id).css("top", "50px").delay(200).hide(0, function(){
          $(id).css("top", "-50px");
        });
      }

    });
  //add ID to list of scrolled IDs
  scrolledIDs.push(IDNum);
}

$(".button").on("mouseenter", function() {
  
  $("#num1").css("top", "50px").delay(150).hide(0);
  
  var scrollDelay = -40;
  //i =  num of scrolling options + final
  //don't let i >= max parameter for randInt function, else endless loop
  for (i=0;i<4;i++){
    scrollDelay=scrollDelay+200;
    if (i >= 3){
      scroll(scrollDelay, 1);
      console.log("final");
    } else{
      scroll(scrollDelay);
      console.log("onedown");
    }
  } 
  scrolledIDs = [];
});

//TO-DO: make final option scroll away when mouseleave
$(".button").on("mouseleave", function() {
  clearOptions();
  //scroll default option from top
  $("#num1").css("top", "-50px");
  $("#num1").show(0, function(){
     $("#num1").css("top", "-15px");
  });
  $(".button").css("width", ($("#num1").width()+30));
});