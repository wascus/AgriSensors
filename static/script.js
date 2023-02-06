
var times = [
    "7:36:18",
    "7:47:25",
    "7:58:32",
    "8:09:39",
    "8:20:46",
    "8:31:53",
    "8:43:00",
    "8:54:07",
    "9:05:14",
    "9:16:21",
    "9:27:28",
]

function scrollerInput(val)
{
    document.getElementById("lab").innerHTML = times[val-1];
    for (var i = 1; i <= cyS.length; i++)
        document.getElementById("cy" + i).style.visibility = 'hidden';
    document.getElementById("cy" + val).style.visibility = 'visible';
}