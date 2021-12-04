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
  type: 'line',
  data: data,
  options: {
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
            this.myChart.update()
        }
    },
    mounted() {
        config.options.scales.y.title.text = `${this.axisLabels.one} - ${this.axisLabels.two}`;
        data.datasets = [{
            label: 'Average Vote',
            data: this.chartData,
            fill: false,
            borderColor: 'red'
        }]
        this.myChart = new Chart(
            document.getElementById('myChart'),
            config
        );
    },
    props: ['chartData', 'axisLabels'],
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