{% for period in periods %}
    var newDiv = $("<div>", { id: "cy{{period.index}}", class: "cy" });
    $("#graphs").append(newDiv);
{% endfor %}
$("#myRange").attr("max", "{{periods|length}}");
$("#myRange").attr("value", "{{periods|length}}");

var times = [
    {% for period in periods %}
        "{{period.time}}",
    {% endfor %}
];
scrollerInput({{periods|length}});

function scrollerInput(val)
{
    document.getElementById("lab").innerHTML = times[val-1].split(" ")[3];
    for (var i = 1; i <= {{periods|length}}; i++)
        document.getElementById("cy" + i).style.visibility = 'hidden';
    document.getElementById("cy" + val).style.visibility = 'visible';
};



var cyS = [
    {% for period in periods %}
        cytoscape({
            container: document.getElementById('cy{{ period.index }}'),
            
            elements: [
                {% for node in period.nodes %}
                    {data: {id: '{{ node.id }}'}},
                {% endfor %}
                {% for edge in period.edges %}
                    {data: {id: '{{ edge.id }}', source: '{{edge.source}}', target: '{{edge.target}}'} },
                {% endfor %}
            ],
            style: [
                {
                    selector: 'node',
                    style: 
                    {
                      'background-color': '#bedce8',
                      'label': 'data(id)',
                      'text-valign': 'center',
                      'text-halign': 'center',
                      'color': 'black',
                      'shape': 'pentagon',
                      'border-color': 'black',
                      'border-width': 1,
                    }
                  },
                  {% for edge in period.edges %}
                        {
                            selector: '#{{edge.id}}',
                            style: 
                            {
                              'width': 3,
                              'line-color': "{{edge.color}}",
                              'curve-style': 'bezier',
                            }
                        },
                  {% endfor %}
            ],

            layout: {
            name: 'grid',
            rows: 3
              
              }
        }),
    {% endfor %}
]

function convertSecondsToMinutes(seconds) {
    let minutes = Math.floor(seconds / 60);
    let remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
  }

function selectDate(date)
{
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/set_page_for_data', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
    if (xhr.status === 200) {
        res = xhr.responseText;
        location.reload();
    }
    };
    xhr.send(JSON.stringify({folder_path: date}));
}

function poll_now()
{
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/get_latest_polled', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function()
    {
    if (xhr.status === 200) {
        res = xhr.responseText;
        if (res == "error")
            alert("An error occurred while processing your request. Please try again later.");
        else
            location.reload();
    }
    };
    xhr.send(JSON.stringify({}));
}

// show average mesurements
document.getElementById("avg_temp").innerHTML = "Temperature: {{avg_data['Temperature']}} °C";
document.getElementById("avg_humidity").innerHTML = "Humidity: {{avg_data['Humidity']}} %";
document.getElementById("avg_ir").innerHTML = "IR: {{avg_data['IR']}} watt";
document.getElementById("avg_vis").innerHTML = "Vis: {{avg_data['Vis']}} lux";
document.getElementById("avg_batt").innerHTML = "Battery: {{avg_data['Batt']}} %";

for (var i = 0; i < cyS.length; i++) // handle click on node
{
    cyS[i].on('click', 'node', function(evt)
    {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/node_clicked', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = function()
        {
        if (xhr.status === 200) 
        {
            document.getElementById('container2').style.visibility = 'visible';
            
            for (var i = 0; i < cyS.length; i++) 
            {
                cyS[i].nodes().style('overlay-opacity',0);
            }


            // change the bg-color of the node
            var node = evt.target;
            var overlayOpacity = node.style('overlay-opacity');
            if(overlayOpacity != 0)
            { // overlay-opacity exists
                node.style('overlay-opacity',0);
            }else
            { // overlay-opacity does not exist
            node.style('overlay-opacity',0.3);
            }

            // hide graph and modal button
            document.getElementById('c3_').style.visibility = 'hidden';
            document.getElementById('open-graph').style.visibility = 'hidden';

            var response = JSON.parse(xhr.response);
            var c2 = document.getElementById("container2");
            c2.querySelector("#nodeID").innerHTML = "Node ID: " + response["node_info"]["id"];
            c2.querySelector("#nodeIP").innerHTML = "Node IP: " + response["node_info"]["ip"].slice(0, 9) + "..." + response["node_info"]["ip"].slice(-9, -1);
            c2.querySelector("#nodeRLOC").innerHTML = "Rloc16: " + response["node_info"]["rloc16"];
            batt_list = response["measurement"]["Batt"];
            c2.querySelector("pre").innerHTML = 
                                batt_list[batt_list.length - 1] != undefined ? batt_list[batt_list.length - 1][1] + "%" : "undefined";
            temp_list = response["measurement"]["Temperature"];
            c2.querySelector("#nodeTEMP").innerHTML =
                temp_list[temp_list.length - 1] != undefined ? "Temperature: " + temp_list[temp_list.length - 1][1] + "°C" : "Temperature: undefined";
            humid_list = response["measurement"]["Humidity"];
            c2.querySelector("#nodeHUMIDITY").innerHTML =
                humid_list[humid_list.length - 1] != undefined ? "Humidity: " + humid_list[humid_list.length - 1][1] + "%" : "Humidity: undefined";
            IR_list = response["measurement"]["IR"];
            c2.querySelector("#nodeIR").innerHTML =
                IR_list[IR_list.length - 1] != undefined ? "IR: " + IR_list[IR_list.length - 1][1] + " watt" : "IR: undefined";
            vis_list = response["measurement"]["Vis"];
            c2.querySelector("#nodeVIS").innerHTML =
                                vis_list[vis_list.length - 1] != undefined ? "Vis: " + vis_list[vis_list.length - 1][1] + " lux" : "Vis: undefined";

            // add event for displaying graph
            var buttons = document.querySelectorAll(".measure");
            
            for (var i = 0; i < buttons.length; i++) {
                
                console.log(response);
                
                buttons[i].onclick = function() {
                    rows = [];
                    measure = this.innerHTML.split(":")[0];
                    for (var j = 0; j < response["measurement"][measure].length; j++) {
                        var date = new Date(Number(response["measurement"][measure][j][0])*1000);
                        var value = Number(response["measurement"][measure][j][1]);
                        var tooltip = date.toUTCString().slice(0, -3) + '<p class="tooltip-paragraph">' + measure + ": </p>" + value;
                        rows.push([date, value, tooltip]);
                    };
                    drawBasic(rows, measure);
                    document.getElementById('c3_').style.visibility = 'visible';
                    document.getElementById('open-graph').style.visibility = 'visible';
                };
            }
            
            
            
        }
        };
        xhr.send(JSON.stringify({node: this.id(), time: $("#lab").text(), date: $("#dates").val()}));
    });
  }

// display graph
google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawBasic);

function drawBasic(rows, measure) 
{
    console.log(rows, measure);
    var data = new google.visualization.DataTable();
    data.addColumn('date', 'X');
    data.addColumn('number', measure);
    data.addColumn({type: 'string', role: 'tooltip', 'p': {'html': true}});

    data.addRows(rows);

    minValue = data.getColumnRange(1).min
    maxValue = data.getColumnRange(1).max

    var options = 
    {
        hAxis: 
        {
            title: 'Time',
            format: 'dd/MM/yyyy'
        },
        vAxis:
        {
            title: measure,
            viewWindow: {
                min: minValue - (maxValue - minValue) * 0.35,
                max: maxValue + (maxValue - minValue) * 0.35
            }
        },
        tooltip: 
        {
            isHtml: true,
            trigger: 'focus'
        },
        curveType: 'none',
        interpolateNulls: true,
    };

    var chart = new google.visualization.LineChart(document.getElementById('c3_'));

    chart.draw(data, options);

    // add width and height to options
    options.width = window.innerWidth * 0.8;
    options.height = window.innerHeight * 0.8;
    options.hAxis.format = 'HH:mm';

    var chart = new google.visualization.LineChart(document.getElementById('temp'));

    chart.draw(data, options);
}

function autoPoll_changed(checkbox)
{
    // change the .ini settings
    var dic = {};
    dic["auto_poll"] = checkbox.checked;
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/change_settings', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() 
    {
        if (xhr.status === 200)
        {   
            if (xhr.response == "error")
            {
                alert("Error: could not change the settings");
            }
        };
    };
    xhr.send(JSON.stringify({options: dic}));

    // change the polling interval
    var par = $(".poll_button p")
    if (checkbox.checked)
        par.css("visibility", "visible");
    else
        par.css("visibility", "hidden");
}