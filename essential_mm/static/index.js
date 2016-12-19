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



    run_splash_screen = function( sentences ){
        sentences = [
            "Welcome to Essential Magic Mirror",
            "The place for the fairest of them all",
            "Setting up your experience",
            "And we hope its as beautiful as you!",
        ]



        var update_center = function(sentences, index){
            var container = $("#center")
            //container.html(sentences[index]);
            container.shuffleLetters({"text": sentences[index]})
            index+=1
            if(index < sentences.length){
                setTimeout( function(){update_center(sentences, index)}, 3000 )
            }
            else{
                container.fadeOut(7000, function(){
                    container.html("")
                    container.show()
                })

            }
        }

        update_center(sentences, 0)
    }


    //clock stuff down here
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

        showDate()
    }

    function checkTime(i) {
        if (i < 10) {
            i = "0" + i;
        }
        return i;
    }

    function showDate(){
        var months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'];
        var myDays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat'];
        var date = new Date();
        var day = date.getDate();
        var month = date.getMonth();
        var thisDay = date.getDay(),
            thisDay = myDays[thisDay];
        var yy = date.getYear();
        var year = (yy < 1000) ? yy + 1900 : yy;
        document.getElementById('date-large').innerHTML="<b>" + thisDay + "</b>, "  + " " + months[month] + " " + day + " " + year;
    }

setInterval(showTime, 10000);
setTimeout(refresh_weather, 10000)
setTimeout(refresh_quote, 10000)
run_splash_screen()
});