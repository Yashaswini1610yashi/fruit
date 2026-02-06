// Handle API calls to the prediction endpoint
const analyzeBtn = document.getElementById('analyzeBtn');
const loader = document.getElementById('loader');

if (analyzeBtn) {
    analyzeBtn.addEventListener('click', function () {
        const fileInput = document.getElementById('imageInput');
        const file = fileInput.files[0];

        if (!file) {
            alert("No image selected!");
            return;
        }

        // UI Feedback
        loader.classList.remove('hidden');
        analyzeBtn.disabled = true;

        const formData = new FormData();
        formData.append('image', file);

        fetch('/predict', {
            method: 'POST',
            body: formData
        })
            .then(response => {
                if (!response.ok) throw new Error("Server error occurred");
                return response.json();
            })
            .then(data => {
                // Save result to local storage for the results page
                localStorage.setItem('lastPrediction', JSON.stringify(data));

                // Redirect to result page
                window.location.href = 'result.html';
            })
            .catch(error => {
                console.error('Error:', error);
                alert("Analysis failed: " + error.message);
                loader.classList.add('hidden');
                analyzeBtn.disabled = false;
            });
    });
}
