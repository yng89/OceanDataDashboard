document.addEventListener('DOMContentLoaded', function() {
    var humidityData = JSON.parse(document.getElementById('data-humidity').getAttribute('data-humidity'));
    var peakPeriodData = JSON.parse(document.getElementById('data-peak-period').getAttribute('data-peak-period'));
    var significantWaveHeightData = JSON.parse(document.getElementById('data-significant-wave-height').getAttribute('data-significant-wave-height'));

    function createPlot(x, y, elementId, xTitle, yTitle) {
        var data = [{
            x: x,
            y: y,
            mode: 'lines+markers',
            type: 'scatter'
        }];

        var layout = {
            xaxis: { title: xTitle },
            yaxis: { title: yTitle },
            height: 600
        };

        Plotly.newPlot(elementId, data, layout);
    }

    if (humidityData && humidityData.length > 0) {
        var humidityTime = humidityData.map(function (row) {
            return row.Time;
        });

        var humidityValues = humidityData.map(function (row) {
            return row.data;
        });

        createPlot(humidityTime, humidityValues, 'humidity-plot', 'Time', 'Humidity');
    }

    if (peakPeriodData && peakPeriodData.length > 0) {
        var peakPeriodTime = peakPeriodData.map(function (row) {
            return row.Time;
        });

        var peakPeriodValues = peakPeriodData.map(function (row) {
            return row.waves;
        });

        createPlot(peakPeriodTime, peakPeriodValues, 'peak-period-plot', 'Time', 'Peak Period');
    }

    if (significantWaveHeightData && significantWaveHeightData.length > 0) {
        var significantWaveHeightTime = significantWaveHeightData.map(function (row) {
            return row.Time;
        });

        var significantWaveHeightValues = significantWaveHeightData.map(function (row) {
            return row.waves;
        });

        createPlot(significantWaveHeightTime, significantWaveHeightValues, 'significant-wave-height-plot', 'Time', 'Significant Wave Height');
    }
    var locationData = JSON.parse(document.getElementById('data-location').getAttribute('data-location'));
    function createMap(data, elementId) {
        var latitudes = data.map(function(row) {
            return row.latitude;
        });

        var longitudes = data.map(function(row) {
            return row.longitude;
        });

        var mapData = [{
            type: 'scattermapbox',
            lat: latitudes,
            lon: longitudes,
            mode: 'markers',
            marker: {
                size: 14,
                color: 'rgb(255, 0, 0)',
            },
        }];

        var layout = {
            mapbox: {
                style: 'open-street-map',
                center: { lat: latitudes[0], lon: longitudes[0] },
                zoom: 10,
            },
            height: 600,
        };

        Plotly.newPlot(elementId, mapData, layout);
    }

    if (locationData && locationData.length > 0) {
        createMap(locationData, 'location-plot');
    }
});
