function handleImageUpload(event) {
    try {
        const files = event.target.files;
        
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            const reader = new FileReader();
            
            reader.onload = function() {
                try {
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

                    // Create a WebSocket connection
                    const socket = new WebSocket('ws://localhost:8000/ws/socket-server/');

                    // Send the image data over the WebSocket connection
                    socket.send(JSON.stringify({
                        image: imageSrc.split(',')[1]  // Remove the data URL prefix
                    }));

                    // Handle incoming messages from the WebSocket connection
                    socket.onmessage = function(event) {
                        try {
                            const data = JSON.parse(event.data);

                            // Clear the output container
                            outputContainer.innerHTML = '';

                            // Create a new div for the output
                            const outputDiv = document.createElement('div');
                            outputDiv.textContent = JSON.stringify(data);

                            // Add the output div to the output container
                            outputContainer.appendChild(outputDiv);
                        } catch (error) {
                            console.error('Error handling WebSocket message:', error);
                        }
                    };

                    socket.onerror = function(error) {
                        // Handle the error here
                        console.error('WebSocket error:', error);
                    };
                } catch (error) {
                    console.error('Error in reader.onload:', error);
                }
            };
            
            reader.readAsDataURL(file);
        }
    } catch (error) {
        console.error('Error in handleImageUpload:', error);
    }
}

function handleSubmit(event) {
    try {
        event.preventDefault();
        
        const images = document.querySelectorAll('.uploaded-image');
    } catch (error) {
        console.error('Error in handleSubmit:', error);
    }
}