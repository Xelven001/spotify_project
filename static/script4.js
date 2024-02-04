document.addEventListener('DOMContentLoaded', function () {

    axios.get('/app4/get_data')
        .then(function(response) {
    
            console.log(response.data);    
            var genres = [...new Set(response.data.map(item => item.genre))];
            var categories = Object.keys(response.data[0]).filter(column => !['genre', 'year'].includes(column));
    
            var genreDropdown = document.getElementById('genre4');
            genres.forEach(function(genre) {
                var option = document.createElement('option');
                option.value = genre;
                option.text = genre;
                genreDropdown.appendChild(option);
            });
    
            var categoryDropdown = document.getElementById('category4');
            categories.forEach(function(category) {
                var option = document.createElement('option');
                option.value = category;
                option.text = category;
                categoryDropdown.appendChild(option);
            });
    
            updateBarGraph(); 
        })
        .catch(function(error) {
            console.error('Error fetching data:', error);
        });
    
    document.getElementById('genre4').addEventListener('change', updateBarGraph);
    document.getElementById('category4').addEventListener('change', updateBarGraph);
    
    
    function updateBarGraph() {
        var selectedGenre = document.getElementById('genre4').value;
        var selectedCategory = document.getElementById('category4').value;
    
        axios.get(`/app4/get_data?genre4=${selectedGenre}`)
            .then(function(response) {
    
                var values = response.data.map(item => item[selectedCategory]);
                var years = response.data.map(item => item.year);
    
                if (window.myBarChart) {
                    window.myBarChart.destroy();
                }
    
                var ctx = document.getElementById('barGraph4').getContext('2d');
                window.myBarChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: years,
                        datasets: [{
                            label: selectedCategory,
                            data: values,
                            backgroundColor: '#38761d',
                            borderColor: 'black',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            x: {
                                type: 'linear',
                                position: 'bottom',
                                title: {
                                    display: true,
                                    text: 'Year'
                                },
                                ticks: {
                                    precision: 0, // Trying to fix date issue showing as 1,999 vs 1999
                                }
                            },
                            
                            y: {
                                beginAtZero: true,
                                title: {
                                    display: true,
                                    text: selectedCategory
                                }
                            }
                        }
                    }
                });
            })
            .catch(function(error) {
                console.error('Error fetching filtered data:', error);
            });
    }
    });