document.getElementById("travel-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const data = {
        destination: document.getElementById("destination").value,
        days: document.getElementById("days").value,
        budget: document.getElementById("budget").value
    };

    fetch('/get-itinerary', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById("result");
        resultDiv.innerHTML = `
            <div class="result-card">
                <h2>Itinerary for ${data.destination}</h2>
                <p><strong>Duration:</strong> ${data.days} days</p>
                <p><strong>Budget:</strong> ${data.budget}</p>
                <p><strong>Activities:</strong> ${data.activities.join(", ")}</p>
                <img src="https://source.unsplash.com/600x400/?travel,${data.destination}" alt="Travel Destination" class="travel-image">
            </div>`;
    });
});
