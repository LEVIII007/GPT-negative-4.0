function output() {
    const inputText = document.getElementById('translation').value;
    // code for ml logic 
    const answerdiv = document.createElement('div');
    const outputDiv = document.getElementById('output');
    const newOutput = document.createElement('div');
    newOutput.textContent = inputText;
    newOutput.classList.add('output-item');
    outputDiv.appendChild(newOutput);
    answerdiv.textContent = "Your answer is here we know that";
    answerdiv.classList.add('ans-item');
    outputDiv.appendChild(answerdiv);
    outputDiv.scrollTop = outputDiv.scrollHeight;
    document.getElementById('translation').value = '';
}
document.getElementById('translation').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        output();
    }
});

