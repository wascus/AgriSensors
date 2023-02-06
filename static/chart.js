// google.charts.load('current', {packages: ['corechart', 'line']});
// google.charts.setOnLoadCallback(drawBasic);

// function drawBasic() {

//       var data = new google.visualization.DataTable();
//       data.addColumn('number', 'X');
//       data.addColumn('number', 'Temp');

//       data.addRows([
//         [0, 20.5888],   [1, 20.5805],  [2, 20.8999],  [3, 20.4863],  [4, 20.5805],  [5, 20.53217],
//         [6, 20.48631],   [7, 20.5888],  [8, 20.9351],  [9, 20.8563],  [10, 21.03217], [11, 20.8999],
    
//       ]);

//       var options = {
//         hAxis: {
//           title: 'Time'
//         },
//         vAxis: {
//           title: 'Temperature'
//         }
//       };

//       var chart = new google.visualization.LineChart(document.getElementById('c3'));

//       chart.draw(data, options);
//     }