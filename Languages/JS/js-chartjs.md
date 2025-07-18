---
title: Chart.js Configuration and Plugins
tags:
  - studies
  - programming
use: Documentation, Code-explanation
languages: JS
dependences: Chart.js
---

<details> <summary>Table of Contents 🔖</summary>

- [New Note](#new-note)

</details>

---
- [i] #to_review : Extrair conhecimento, formatar e adicionar na seção de QGis em programming studies
# Chart.js Configuration and Plugins Overview

```js
// Set new default font family and font color to mimic Bootstrap's default styling
// Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
// Chart.defaults.global.defaultFontColor = '#858796';

// TODO: Move this code to the backend

// Pie Chart
const stagesChartHTML = document.getElementById("stagesChart");
const dataValues = stagesChartHTML.getAttribute("data-values").split(',').map(Number); // Convert strings to numbers

const stagesChart = new Chart(stagesChartHTML, {
    type: 'doughnut',
    data: {
        labels: ["Self", "Manager", "Both", "Meeting"],
        datasets: [{
            data: dataValues,
            backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#f6c23e'],
            hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf', '#e6ac00'],
            hoverBorderColor: "rgba(234, 236, 244, 1)",
        }],
    },
    options: {
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: true,
                labels: {
                    usePointStyle: true,
                    pointStyle: 'circle',
                },
            },
            tooltips: {
                backgroundColor: "rgb(255,255,255)",
                bodyFontColor: "#858796",
                borderColor: '#dddfeb',
                borderWidth: 1,
                xPadding: 15,
                yPadding: 15,
                displayColors: false,
                caretPadding: 10,
            },
        },
        cutout: '70%',
    },
});

// Area Chart
function number_format(number, decimals, dec_point, thousands_sep) {
    // *     example: number_format(1234.56, 2, ',', ' ');
    // *     return: '1 234,56'
    number = (number + '').replace(',', '').replace(' ', '');
    var n = !isFinite(+number) ? 0 : +number,
        prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
        sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
        dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
        s = '',
        toFixedFix = function(n, prec) {
            var k = Math.pow(10, prec);
            return '' + Math.round(n * k) / k;
        };
    // Fix for IE parseFloat(0.55).toFixed(0) = 0;
    s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
    if (s[0].length > 3) {
        s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
    }
    if ((s[1] || '').length < prec) {
        s[1] = s[1] || '';
        s[1] += new Array(prec - s[1].length + 1).join('0');
    }
    return s.join(dec);
}

const periodChartHTML = document.getElementById("periodChart");
const data = periodChartHTML.getAttribute("data-data");
const periodChart = new Chart(periodChartHTML, {
    type: 'line',
    data: JSON.parse(data),
    options: {
        maintainAspectRatio: false,
        layout: {
            padding: {
                left: 10,
                right: 25,
                top: 25,
                bottom: 0
            }
        },
        scales: {
            xAxes: [{
                time: {
                    unit: 'date'
                },
                gridLines: {
                    display: false,
                    drawBorder: false
                },
                ticks: {
                    maxTicksLimit: 7
                }
            }],
            yAxes: [{
                ticks: {
                    maxTicksLimit: 5,
                    padding: 10,
                    // Include a dollar sign in the ticks
                    callback: function(value, index, values) {
                        return '$' + number_format(value);
                    }
                },
                gridLines: {
                    color: "rgb(234, 236, 244)",
                    zeroLineColor: "rgb(234, 236, 244)",
                    drawBorder: false,
                    borderDash: [2],
                    zeroLineBorderDash: [2]
                }
            }],
        },
        plugins: {
            legend: {
                display: true,
            }
        },
        tooltips: {
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            intersect: false,
            mode: 'index',
            caretPadding: 10,
            callbacks: {
                label: function(tooltipItem, chart) {
                    var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                    return datasetLabel + ': $' + number_format(tooltipItem.yLabel);
                }
            }
        }
    }
});

// Nine Box Chart
function createQuadrantPlugin() {
    try {
        return {
            id: "quadrants",
            // beforeDatasetsDraw: (chart) => {
            beforeDraw: (chart) => {
                const ctx = chart.ctx;
                const xScale = chart.scales.x;
                const yScale = chart.scales.y;
                const quadrants = chart.config.options.plugins?.quadrants?.quadrants;

                if (!quadrants) {
                    console.error("Quadrants are missing!");
                    return;
                }
                console.log(quadrants);

                quadrants.forEach((quadrant) => {
                    const xStart = xScale.getPixelForValue(quadrant.xMin);
                    const xEnd = xScale.getPixelForValue(quadrant.xMax);
                    const yStart = yScale.getPixelForValue(quadrant.yMax);
                    const yEnd = yScale.getPixelForValue(quadrant.yMin);

                    ctx.save();
                    ctx.fillStyle = quadrant.backgroundColor;
                    ctx.fillRect(xStart, yStart, xEnd - xStart, yEnd - yStart);

                    // Draw quadrant label
                    ctx.fillStyle = 'black';
                    ctx.font = '12px Arial';
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    if (quadrant.label) {
                        ctx.fillText(quadrant.label, xStart + (xEnd - xStart) / 2, yStart + (yEnd - yStart) / 2);
                    }

                    ctx.restore();
                });
            },
        };
    } catch (e) {
        console.error("Error creating quadrants plugin:", e);
        return null;
    }
}

function createPointRendererPlugin() {
    try {
        return {
            id: "customPointRenderer",
            afterDatasetsDraw: (chart) => {
                const ctx = chart.ctx;
                const dataset = chart.data.datasets[0];
                const meta = chart.getDatasetMeta(0);

                dataset.data.forEach((dataPoint, index) => {
                    const point = meta.data[index];
                    if (!point || point.hidden) return;

                    const x = point.x;
                    const y = point.y;
                    const users = dataPoint.users;

                    if (users.length > 1) {
                        // Render a counter for overlapping points
                        ctx.save();
                        ctx.fillStyle = "rgba(0, 0, 0, 0.7)";
                        ctx.beginPath();
                        ctx.arc(x, y, 15, 0, 2 * Math.PI);
                        ctx.fill();

                        ctx.fillStyle = "white";
                        ctx.font = "14px Arial";
                        ctx.textAlign = "center";
                        ctx.textBaseline = "middle";
                        ctx.fillText(+${users.length}, x, y);
                        ctx.restore();
                    } else {
                        // Render user photo for a single point
                        const user = users[0];
                        if (user.photo) {
                            const image = new Image();
                            image.src = data:image/jpeg;base64,${user.photo};
                            image.onload = () => {
                                ctx.save();
                                ctx.beginPath();
                                ctx.arc(x, y, 15, 0, 2 * Math.PI);
                                ctx.clip();
                                ctx.drawImage(image, x - 15, y - 15, 30, 30);
                                ctx.restore();
                            };
                        }
                    }
                });
            },
        };
    } catch (e) {
        console.error("Error creating point renderer plugin:", e);
        return null;
    }
}

function createTooltipHandler() {
    try {
        return (context) => {
            const { chart, tooltip } = context;
            let tooltipEl = document.getElementById("chartjs-tooltip");

            // Create tooltip element if it doesn't exist
            if (!tooltipEl) {
                tooltipEl = document.createElement("div");
                tooltipEl.id = "chartjs-tooltip";
                tooltipEl.style.position = "absolute";
                tooltipEl.style.background = "rgba(0, 0, 0, 0.7)";
                tooltipEl.style.color = "white";
                tooltipEl.style.borderRadius = "5px";
                tooltipEl.style.padding = "10px";
                tooltipEl.style.pointerEvents = "none";
                tooltipEl.style.transform = "translate(-50%, -100%)";
                tooltipEl.style.transition = "opacity 0.2s ease";
                document.body.appendChild(tooltipEl);
            }

            // Hide tooltip if not active
            if (tooltip.opacity === 0) {
                tooltipEl.style.opacity = 0;
                return;
            }

            // Build content for overlapping or single points
            const dataPoints = tooltip.dataPoints[0].raw.users;
            tooltipEl.innerHTML = dataPoints
                .map(
                    (user) => 
                        <div style="display: flex; align-items: center; margin-bottom: 5px;">
                            ${user.photo ? <img src="data:image/jpeg;base64,${user.photo}" style="width: 30px; height: 30px; border-radius: 50%; margin-right: 5px;" /> : ""}
                            <div>
                                <strong>${user.name}</strong>
                            </div>
                        </div>
                )
                .join("");

            // Position the tooltip
            const position = chart.canvas.getBoundingClientRect();
            tooltipEl.style.opacity = 1;
            tooltipEl.style.left = position.left + window.pageXOffset + tooltip.caretX + "px";
            tooltipEl.style.top = position.top + window.pageYOffset + tooltip.caretY + "px";
        };
    } catch (e) {
        console.error("Error creating tooltip handler:", e);
        return null;
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const chartElement = document.getElementById("nineBoxChart");
    const chartConfigData = chartElement.dataset.chartConfig;

    if (!chartConfigData) {
        console.error("Chart configuration data is missing!");
        return;
    }

    try {
        const chartConfig = JSON.parse(chartConfigData);
        const ctx = chartElement.getContext("2d");

        // Create Plugins
        const quadrantPlugin = createQuadrantPlugin();
        const pointRendererPlugin = createPointRendererPlugin();
        const tooltipHandler = createTooltipHandler();

        // Apply Plugins
        chartConfig.options.plugins = chartConfig.options.plugins || {};
        if (quadrantPlugin) chartConfig.options.plugins.quadrants = quadrantPlugin;
        if (pointRendererPlugin) chartConfig.options.plugins.customPointRenderer = pointRendererPlugin;
        chartConfig.options.plugins.tooltip = {
            enabled: false, // Disable default tooltip
            external: tooltipHandler,
        };

        // Create Chart Instance
        const myChart = new Chart(ctx, chartConfig);

        // Resize chart dynamically when window is resized
        window.addEventListener("resize", () => {
            myChart.resize();
        });
    } catch (e) {
        console.error("Error parsing chart configuration:", e);
    }
});
```

This script defines and initializes several **Chart.js** visualizations, along with custom plugins and tooltip handlers. It supports:
- A **doughnut chart** for feedback stages
- A **line chart** for feedback over time
- A **"Nine Box" scatter chart** with quadrant coloring and user photos

## 1. Global Chart Settings (Commented Out)

```js
// Chart.defaults.global.defaultFontFamily = 'Nunito', ...;
// Chart.defaults.global.defaultFontColor = '#858796';
```

These lines (commented out) set default fonts and colors to match Bootstrap styling.

## 2. Doughnut Chart: `feedbackStagesChart`

```js
const feedbackStagesChart = new Chart(...);
```
- Target: Element with ID `feedbackStagesChart`
- Labels: `["Self", "Manager", "Both", "Meeting"]`
- Data: Taken from `data-values` attribute (comma-separated)
- Colors: Custom background and hover colors
- Cutout: 70% for a donut-style chart

## 3. Line Chart: `feedbackPeriodChart`

```js
const feedbackPeriodChart = new Chart(...);
```
- Target: Element with ID `feedbackPeriodChart`
- Data: Extracted from `data-data` attribute (JSON string)
- Custom number formatting with `number_format()`
- Y-axis values prefixed with `$`
- Tooltips and legends are customized

### Utility: `number_format()`
A helper function that formats numbers with custom decimal and thousand separators.

## 4. Nine Box Scatter Chart (with User Photos)
The chart is rendered dynamically with a custom config from the `data-chart-config` attribute.

### a. `createQuadrantPlugin()`
Adds colored background rectangles (quadrants) to a scatter plot.
- Each quadrant is defined with `xMin`, `xMax`, `yMin`, `yMax`, `backgroundColor`, and optional `label`
- Renders labels inside each quadrant

### b. `createPointRendererPlugin()`
Custom rendering of data points:
- If **multiple users** share the same coordinates, a counter is displayed
- If **only one user**, it renders their photo (base64 image)

### c. `createTooltipHandler()`
Custom external tooltip that:
- Displays user photos and names in a styled floating div
- Replaces the default Chart.js tooltip

## 5. Chart Initialization on Page Load

```js
document.addEventListener("DOMContentLoaded", function () { ... });
```
- Gets config from `#nineBoxChart`
- Parses config and applies:
    - `quadrants` plugin
    - `customPointRenderer` plugin
    - External tooltip handler
- Initializes the chart
- Adds a listener to resize chart on window resize

## Summary

| Component                   | Description                                                                       |
| --------------------------- | --------------------------------------------------------------------------------- |
| `feedbackStagesChart`       | Doughnut chart showing feedback distribution (Self, Manager, Both, Meeting)       |
| `feedbackPeriodChart`       | Line chart visualizing feedback trends over time                                  |
| `number_format()`           | Utility function to format numbers with custom separators and decimals            |
| `createQuadrantPlugin`      | Plugin that adds background quadrants with labels to a scatter chart              |
| `createPointRendererPlugin` | Renders user avatars or counters depending on overlapping points                  |
| `createTooltipHandler`      | Custom HTML-based tooltip showing user name and optional photo                    |
| `DOMContentLoaded` init     | Loads `nineBoxChart` dynamically with custom plugins and resizes on window resize |
