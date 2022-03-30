
 async function get_singapore_data(){

    let response = await fetch('http://localhost:8000/pop/',{method:"GET",headers:{'Content-Type':'application/json'}})
    const data = response.json()
    return data;
}

get_singapore_data().then( data => {

    const names = Object.keys(data.dataset_one).map( year => { return data.dataset_one[year].map( d => d.name)})
    const populations = Object.keys(data.dataset_one).map( year => { return data.dataset_one[year].map( d => d.value)})
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [...names[0]],
            datasets: [{
                label: '# of Votes',
                data: [...populations[0]],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
})