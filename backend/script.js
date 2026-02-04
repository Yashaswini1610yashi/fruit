function previewImage(event) {
    const input = event.target;
    const preview = document.getElementById("imagePreview");
    const container = document.getElementById("imagePreviewContainer");
    const btn = document.getElementById("analyzeBtn");

    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            preview.src = e.target.result;
            container.classList.remove("hidden");
            btn.disabled = false;
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function uploadImage() {
    let fileInput = document.getElementById("imageInput");
    let file = fileInput.files[0];

    if (!file) {
        alert("Please select an image");
        return;
    }

    // UI Updates
    document.getElementById("loader").classList.remove("hidden");
    document.getElementById("result").classList.add("hidden");

    // Resize on client to 224x224 before upload to reduce transfer size and speed server processing
    resizeImage(file, 224, 224, function (resizedBlob) {
        let formData = new FormData();
        // keep original filename but ensure extension matches jpeg
        const name = file.name.replace(/\.[^.]+$/, '') + ".jpg";
        formData.append("image", resizedBlob, name);

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
                document.getElementById("result").classList.remove("hidden");

                const predictionText = document.getElementById("predictionText");
                predictionText.innerHTML = data.result;
                predictionText.style.color = data.result === "Fresh" ? "#2ed573" : "#ff4757";

                document.getElementById("confidenceText").innerHTML = `${data.confidence}%`;
                document.getElementById("confidenceBar").style.width = `${data.confidence}%`;
            })
            .catch(err => {
                document.getElementById("loader").classList.add("hidden");
                alert("Error: " + err.message);
                console.error(err);
            });
    });
}

// Resize an image file to target width/height (center-crop) and return a JPEG Blob via callback
function resizeImage(file, targetW, targetH, callback) {
    const reader = new FileReader();
    reader.onload = function (e) {
        const img = new Image();
        img.onload = function () {
            const canvas = document.createElement('canvas');
            canvas.width = targetW;
            canvas.height = targetH;
            const ctx = canvas.getContext('2d');

            // calculate aspect-fit crop (cover)
            const sw = img.width;
            const sh = img.height;
            const swRatio = targetW / sw;
            const shRatio = targetH / sh;
            const scale = Math.max(swRatio, shRatio);
            const dw = sw * scale;
            const dh = sh * scale;
            const dx = (targetW - dw) / 2;
            const dy = (targetH - dh) / 2;

            ctx.fillStyle = '#fff';
            ctx.fillRect(0, 0, targetW, targetH);
            ctx.drawImage(img, dx, dy, dw, dh);

            canvas.toBlob(function (blob) {
                callback(blob);
            }, 'image/jpeg', 0.9);
        };
        img.src = e.target.result;
    };
    reader.readAsDataURL(file);
}
