// Smooth Scrolling for Navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Image Preview & Upload Logic
function previewImage(event) {
    const input = event.target;
    const preview = document.getElementById("imagePreview");
    const container = document.getElementById("imagePreviewContainer");
    const dropZone = document.getElementById("dropZone");

    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            preview.src = e.target.result;
            container.classList.remove("hidden");
            dropZone.classList.add("hidden"); // Hide upload area
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function resetDemo() {
    document.getElementById("imageInput").value = "";
    document.getElementById("imagePreviewContainer").classList.add("hidden");
    document.getElementById("dropZone").classList.remove("hidden");
    document.getElementById("result").classList.add("hidden");
    document.getElementById("confidenceBar").style.width = "0%";
}

function uploadImage() {
    let fileInput = document.getElementById("imageInput");
    let file = fileInput.files[0];

    if (!file) {
        alert("Please select an image first!");
        return;
    }

    // UI Updates
    document.getElementById("loader").classList.remove("hidden");
    document.getElementById("analyzeBtn").classList.add("hidden");
    document.getElementById("result").classList.add("hidden");

    let formData = new FormData();
    formData.append("image", file);

    fetch("/predict", {
        method: "POST",
        body: formData
    })
        .then(res => {
            if (!res.ok) {
                return res.json().then(err => { throw new Error(err.error || "Server error") });
            }
            return res.json();
        })
        .then(data => {
            document.getElementById("loader").classList.add("hidden");
            document.getElementById("analyzeBtn").classList.remove("hidden");
            document.getElementById("result").classList.remove("hidden");

            // Update Prediction Text
            const predictionText = document.getElementById("predictionText");
            predictionText.innerHTML = data.result;

            // Color Coding
            if (data.result === "Fresh") {
                predictionText.style.color = "#00f260"; // Neon Green
                document.getElementById("confidenceBar").style.background = "linear-gradient(90deg, #00f260, #0575E6)";
            } else {
                predictionText.style.color = "#ff4757"; // Red
                document.getElementById("confidenceBar").style.background = "linear-gradient(90deg, #ff4757, #ff6b81)";
            }

            // Update Confidence
            document.getElementById("confidenceText").innerHTML = `${data.confidence}%`;

            // Animate Bar
            setTimeout(() => {
                document.getElementById("confidenceBar").style.width = `${data.confidence}%`;
            }, 100);
        })
        .catch(err => {
            document.getElementById("loader").classList.add("hidden");
            document.getElementById("analyzeBtn").classList.remove("hidden");
            alert("Error: " + err.message);
            console.error(err);
        });
}
