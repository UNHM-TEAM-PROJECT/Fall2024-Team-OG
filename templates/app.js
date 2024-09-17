const chatWindow = document.getElementById('chat-messages');
const chatInput = document.getElementById('user-input');
const chatSendButton = document.getElementById('send-button');

chatSendButton.addEventListener('click', sendMessage);
chatInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

// Function to display a message in the chat window
function displayMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', `message--${sender}`);
    messageElement.textContent = message;
    chatWindow.appendChild(messageElement);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function sendMessage() {
    const userInput = chatInput.value.trim();
    if (userInput) {
        displayMessage('user', userInput);
        chatInput.value = '';
        fetchChatResponse(userInput);
    }
}

function fetchChatResponse(userInput) {
    fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        displayMessage('bot', data.response);
    })
    .catch(error => {
        console.error('Error fetching chat response:', error);
        displayMessage('bot', 'Oops, something went wrong. Please try again later.');
    });
}
