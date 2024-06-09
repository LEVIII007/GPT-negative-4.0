function handleImageUpload(event) {
    const files = event.target.files;
    
    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const reader = new FileReader();
        
        reader.onload = function() {
            const imageSrc = reader.result;
            const image = document.createElement('img');
            image.src = imageSrc;
            image.classList.add('uploaded-image');
            
            const outputDiv = document.getElementById('outputContainer');
            const newOutput = document.createElement('div');
            newOutput.classList.add('output-item');
            
            const imageBlock = document.createElement('div');
            imageBlock.classList.add('image-block');
            imageBlock.appendChild(image);
            
            newOutput.appendChild(imageBlock);
            
            const timestamp = document.createElement('div');
            timestamp.textContent = `Uploaded at: ${new Date().toLocaleString()}`;
            newOutput.appendChild(timestamp);
            
            outputDiv.appendChild(newOutput);
        };
        
        reader.readAsDataURL(file);
    }
}

function handleSubmit(event) {
    event.preventDefault();
    
    const images = document.querySelectorAll('.uploaded-image');
    if (images.length === 0) {
        alert('Please select at least one image to upload.');
        return;
    }
    document.getElementById('uploadIcon').src = 'Images/upload.png';
    document.getElementById('uploadIcon').style.display = 'none';
    document.getElementById('imageUpload').value = '';
}
