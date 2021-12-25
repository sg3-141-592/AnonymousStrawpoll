<template>
    <canvas id="myChart"></canvas>
</template>

<script>
import Chart from 'chart.js/auto';
import 'chartjs-adapter-date-fns';

var data = {
  datasets: [{
    label: 'Average Vote',
    data: [ ],
    fill: false,
    borderColor: 'red'
  }]
};

var config = {
  data: data,
  options: {
      animation: {
        duration: 0
      },
      parsing: false,
      plugins: {
          legend: {
              display: false
          }
      },
      response: true,
      scales: {
          x: {
                display: "true",
                type: "time",
                ticks: {
                    source: 'auto',
                    maxTicksLimit: 10
                },
          },
          y: {
              min: 0.0,
              max: 1.0,
              stepSize: 0.2,
              title: {
                  display: true,
                  text: "PLACEHOLDER",
              }
          }
      }
  }
};

export default {
    methods: {
        updateGraph: function() {
            // We have to multiply incoming dates by 1000 as Javascript uses
            // milliseconds since epoch instead of seconds
            this.chartData.forEach((o) => o.x *= 1000)
            this.latestPoints.forEach((o) => o.x *= 1000)
            //
            data.datasets[0].data = this.chartData
            data.datasets[1].data = this.latestPoints
            this.myChart.update()
        }
    },
    mounted() {
        // We have to multiply incoming dates by 1000 as Javascript uses
        // milliseconds since epoch instead of seconds
        this.chartData.forEach((o) => o.x *= 1000)
        this.latestPoints.forEach((o) => o.x *= 1000)
        //
        config.options.scales.y.title.text = `${this.axisLabels.one} - ${this.axisLabels.two}`;
        data.datasets = [{
            type: 'line',
            borderDash: [15, 12],
            pointRadius: 0,
            label: 'Average Vote',
            data: this.chartData,
            fill: false,
            borderColor: 'red'
        },
        {
            type: 'scatter',
            label: 'Latest Points',
            data: this.latestPoints,
            fill: false,
            borderColor: 'grey',
            borderWidth: 1,
            pointRadius: 5,
            pointStyle: "cross",
        }]
        this.myChart = new Chart(
            document.getElementById('myChart'),
            config
        );
    },
    unmounted() {
        this.myChart.destroy()
    },
    props: ['chartData', 'axisLabels', 'latestPoints'],
    watch: {
        chartData: function() {
          this.updateGraph()
        }
    },
    data() {
        this.myChart = null
        return { }
    }
}
</script>