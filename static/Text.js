function output() {
    const inputText = document.getElementById('translation').value;
    const outputDiv = document.getElementById('output');
    const newOutput = document.createElement('div');
    newOutput.textContent = inputText;
    newOutput.classList.add('output-item');
    outputDiv.appendChild(newOutput);
    outputDiv.scrollTop = outputDiv.scrollHeight;
    document.getElementById('translation').value = '';
}
document.getElementById('translation').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        output();
    }
});
