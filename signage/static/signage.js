var week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];

$(document).ready(function(){
    var timerID = setInterval(updateTime, 1000);
    updateTime();
    getContent()
});


function updateTime() {
    var cd = new Date();
    cur_date = zeroPadding(cd.getFullYear(), 4) + '-' + zeroPadding(cd.getMonth()+1, 2) + '-' + zeroPadding(cd.getDate(), 2) + ' ' + week[cd.getDay()];
    cur_time = zeroPadding(cd.getHours(), 2) + ':' + zeroPadding(cd.getMinutes(), 2) + ':' + zeroPadding(cd.getSeconds(), 2);
    $("p.date").text(cur_date);
    $("p.time").text(cur_time);
};

function zeroPadding(num, digit) {
    var zero = '';
    for(var i = 0; i < digit; i++) {
        zero += '0';
    }
    return (zero + num).slice(-digit);
}

function Display(image) {
    $("#image").attr("src", image);
}

function getContent() {
    $.ajax({
        url: "/get_content",
        success: function(obj) {
            obj = JSON.parse(obj);
            total_delay = 0;
            delay = 0;
            for (let i=0; i < obj.length; i++) {
                display_msec = obj[i]["display_time"] * 1000
                setTimeout(Display, delay, obj[i]["url"])
                delay = display_msec;
                total_delay += delay;
            }
            setTimeout(getContent, total_delay);
        },
        error: function(err) {
            console.log(err);
        }
    });
};
