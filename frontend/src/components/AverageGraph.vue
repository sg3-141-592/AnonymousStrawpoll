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
      scales: {
          x: {
                display: "true",
                type: "time",
                ticks: {
                    source: 'auto',
                    maxTicksLimit: 5
                },
                time: {
                    unit: 'second'
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
            data.datasets[0].data = this.chartData
            data.datasets[1].data = this.latestPoints
            this.myChart.update()
        }
    },
    mounted() {
        config.options.scales.y.title.text = `${this.axisLabels.one} - ${this.axisLabels.two}`;
        data.datasets = [{
            type: 'line',
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