function ScrollToBottom(){
    window.scrollTo(0,document.body.scrollHeight);
}


function getBotResponse(){
    var rawText = $("#textInput").val();
    var userHtml =  '<div class="dynamic"> <p class = "userText"> <img class="robot_pic" src="static/right-arrow.svg"/>' + rawText + '</p> </div>';
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    $.get("/get", {msg:rawText }).done(function(data) {
    var botHtml = '<div class="dynamic">' + '<p class ="botText"> <img class="robot_pic" src="static/robotics.svg"/>' + data + '</p> </div>';
    $("#chatbox").append(botHtml);
    ScrollToBottom();
    });
};

function clear_convo(){
    count = 1;
    var messages = document.querySelectorAll('.dynamic');
    var welcome_msg = document.querySelectorAll('.botText');
    for (var i = messages.length-1; i >= 0; i--){
        (function(i) {
            setTimeout(function(){
                messages[i].remove();
            }, 55 * count)
        })(i);
        count++;
    };

    welcome_msg[0].remove();
};

function click_section(a_index) {
    $(".footer_links")[a_index].click();
};


$("#textInput").keypress(function(e) {
    if(e.which == 13) {
        getBotResponse();
        ScrollToBottom();
    }
});
