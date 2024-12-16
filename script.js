document.getElementById('translationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let inputText = document.getElementById('inputText').value;

    fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('detectedLanguage').textContent = data.detectedLanguage;
        document.getElementById('translatedText').textContent = data.translatedText;
    })
    .catch(error => console.error('Error:', error));
});
