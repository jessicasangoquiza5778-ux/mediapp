// Line Chart
var lineChartCanvas = document.getElementById('lineChart');
if (lineChartCanvas) {
    var lineChart = new Chart(lineChartCanvas, {
        type: 'line',
        data: {
            labels: ['2013', '2014', '2015', '2016', '2017'],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 15, 17, 14],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1,
                fill: true
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 20
                }
            }
        }
    });
}

// Bar Chart
var barChartCanvas = document.getElementById('barChart');
if (barChartCanvas) {
    var barChart = new Chart(barChartCanvas, {
        type: 'bar',
        data: {
            labels: ['Pink', 'Blue', 'Yellow'],
            datasets: [{
                label: '# of Votes',
                data: [15, 20, 10],
                backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)'],
                borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)'],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 20
                }
            }
        }
    });
}

// Area Chart
var areaChartCanvas = document.getElementById('areaChart');
if (areaChartCanvas) {
    var areaChart = new Chart(areaChartCanvas, {
        type: 'line',
        data: {
            labels: ['2013', '2014', '2015', '2016', '2017'],
            datasets: [{
                label: '# of Votes',
                data: [5, 10, 8, 15, 12],
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
                fill: true
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 20
                }
            }
        }
    });
}

// Doughnut Chart
var doughnutChartCanvas = document.getElementById('doughnutChart');
if (doughnutChartCanvas) {
    var doughnutChart = new Chart(doughnutChartCanvas, {
        type: 'doughnut',
        data: {
            labels: ['Pink', 'Blue', 'Yellow'],
            datasets: [{
                data: [15, 20, 10],
                backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)'],
                borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)'],
                borderWidth: 1
            }]
        }
    });
}

// Pie Chart
var pieChartCanvas = document.getElementById('pieChart');
if (pieChartCanvas) {
    var pieChart = new Chart(pieChartCanvas, {
        type: 'pie',
        data: {
            labels: ['Pink', 'Blue', 'Yellow'],
            datasets: [{
                data: [15, 20, 10],
                backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)'],
                borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)'],
                borderWidth: 1
            }]
        }
    });
}

// Scatter Chart
var scatterChartCanvas = document.getElementById('scatterChart');
if (scatterChartCanvas) {
    var scatterChart = new Chart(scatterChartCanvas, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Scatter Dataset',
                data: [
                    {x: 2013, y: 12},
                    {x: 2014, y: 19},
                    {x: 2015, y: 15},
                    {x: 2016, y: 17},
                    {x: 2017, y: 14}
                ],
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Año'
                    }
                },
                y: {
                    beginAtZero: true,
                    max: 20,
                    title: {
                        display: true,
                        text: '# of Votes'
                    }
                }
            }
        }
    });
}