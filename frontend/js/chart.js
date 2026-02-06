// Visualization logic using Chart.js
function initChart(confidence) {
    const ctx = document.getElementById('confidenceChart').getContext('2d');

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Confidence', 'Remainder'],
            datasets: [{
                data: [confidence, 100 - confidence],
                backgroundColor: [
                    '#0575E6',
                    'rgba(255, 255, 255, 0.1)'
                ],
                borderWidth: 0
            }]
        },
        options: {
            cutout: '80%',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: { enabled: false }
            },
            animation: {
                duration: 2000,
                easing: 'easeOutQuart'
            }
        }
    });
}
