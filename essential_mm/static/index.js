$(function(){

    refresh_weather = function(){
        $.ajax({
          url: "/weather",
          cache: false
        }).done(function( html ) {
            $( "#ul" ).html( html );
            setTimeout(refresh_weather, 1800000);
        });
    }

    refresh_quote = function(){
        $.ajax({
          url: "/quote",
          cache: false
        }).done(function( html ) {
            $( "#footer" ).fadeOut(7000, function(){
                $( "#footer" ).html(html);
                $( "#footer" ).fadeIn(7000);
                setTimeout(refresh_quote, 60000);
            });
        });
    }





    function showTime() {
        var a_p = "";
        var today = new Date();
        var curr_hour = today.getHours();
        var curr_minute = today.getMinutes();
        var curr_second = today.getSeconds();
        if (curr_hour < 12) {
            a_p = "<span>AM</span>";
        } else {
            a_p = "<span>PM</span>";
        }
        if (curr_hour == 0) {
            curr_hour = 12;
        }
        if (curr_hour > 12) {
            curr_hour = curr_hour - 12;
        }
        curr_hour = checkTime(curr_hour);
        curr_minute = checkTime(curr_minute);
        curr_second = checkTime(curr_second);
        document.getElementById('clock-large').innerHTML=curr_hour + " : " + curr_minute + " " + a_p;
        }

    function checkTime(i) {
        if (i < 10) {
            i = "0" + i;
        }
        return i;
    }


    var months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Okt', 'Nov', 'Dec'];
    var myDays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat'];
    var date = new Date();
    var day = date.getDate();
    var month = date.getMonth();
    var thisDay = date.getDay(),
        thisDay = myDays[thisDay];
    var yy = date.getYear();
    var year = (yy < 1000) ? yy + 1900 : yy;
         document.getElementById('date-large').innerHTML="<b>" + thisDay + "</b>, "  + " " + months[month] + " " + day + " " + year;


setInterval(showTime, 5000);
setTimeout(refresh_weather, 3000)
setTimeout(refresh_quote, 4000)

});