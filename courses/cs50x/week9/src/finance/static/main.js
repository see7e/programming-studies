document.addEventListener("DOMContentLoaded", function () {
    var stockChart = document.getElementById("stockChart").getContext("2d");
    var stockData = JSON.parse(document.getElementById("stockData").getAttribute("data-historical-data"));
    var labels = stockData.map(function (data) { return data.Date; });
    var prices = stockData.map(function (data) { return data["Adj Close"]; });

    console.log("stockChart", stockChart)
    console.log("stockData", stockData)
    console.log("labels", labels)
    console.log("prices", prices)
    
    var stockChart = new Chart(stockChart, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Stock Prices',
                data: prices,
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 2,
                fill: false,
                pointRadius: 0
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'day'
                    }
                },
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
