<template>
    <canvas id="myChart"></canvas>
</template>

<script>
import moment from 'moment';
import Chart from 'chart.js/auto';
import 'chartjs-adapter-moment';

var data = {
  datasets: [{
    label: 'Average Vote',
    data: [ ],
    fill: false,
    borderColor: 'red'
  }]
};

var config = {
  type: 'scatter',
  data: data,
  options: {
      responsive: true,
      scales: {
          x: {
                type: "time",
                ticks: {
                    source: 'auto'
                },
                time: {
                    // format: timeFormat,
                    unit: 'second'
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
        // data.labels = this.chartData.labels
        // data.datasets[0].data = this.chartData.data
        data.datasets = [{
            label: 'Average Vote',
            data: this.chartData,
            fill: false,
            borderColor: 'red'
        }]
        console.log(data.datasets)
        
        this.myChart = new Chart(
            document.getElementById('myChart'),
            config
        );

        console.log(moment)
    },
    props: ['chartData'],
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