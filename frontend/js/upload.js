// Handle Image Selection and Preview
const imageInput = document.getElementById('imageInput');
const preview = document.getElementById('imagePreview');
const previewContainer = document.getElementById('imagePreviewContainer');
const dropZone = document.getElementById('dropZone');

if (imageInput) {
    imageInput.addEventListener('change', function (e) {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (event) {
                preview.src = event.target.result;
                previewContainer.classList.remove('hidden');
                dropZone.classList.add('hidden');

                // Save for later use in result page
                localStorage.setItem('lastImage', event.target.result);
            };
            reader.readAsDataURL(file);
        }
    });
}

// Drag and Drop Support
if (dropZone) {
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.style.borderColor = '#0575E6';
        dropZone.style.background = 'rgba(5, 117, 230, 0.1)';
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.style.borderColor = 'rgba(255, 255, 255, 0.2)';
        dropZone.style.background = 'transparent';
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        const file = e.dataTransfer.files[0];
        if (file && file.type.startsWith('image/')) {
            imageInput.files = e.dataTransfer.files;
            const event = new Event('change');
            imageInput.dispatchEvent(event);
        }
    });
}
