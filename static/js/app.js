document.addEventListener('DOMContentLoaded', function() {
    const chatInput = document.querySelector('#user-input');
    const chatSendButton = document.querySelector('#send-button');
    const chatMessages = document.querySelector('#chat-messages');

    chatSendButton.addEventListener('click', function() {
        sendMessage();
    });

    chatInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault(); // Avoid newline in textarea
            sendMessage();
        }
    });

    function sendMessage() {
        const userInput = chatInput.value.trim();
        if (userInput) {
            displayMessage('user', userInput);
            chatInput.value = '';  // Clear input
            fetchChatResponse(userInput);
        }
    }

    function displayMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `message--${sender}`);
        messageElement.setAttribute('data-sender', sender === 'user' ? 'you :' : 'chatbot :');
        messageElement.textContent = message;
        chatMessages.appendChild(messageElement);
        // Scroll to latest message
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function fetchChatResponse(userInput) {
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_input: userInput }), // Send user
            // Send user input as JSON
            body: JSON.stringify({ user_input: userInput })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not okay');
            }
            return response.json();
        })
        .then(data => {
            if (data.response) {
                displayMessage('bot', data.response);  // Display bot response
            } else {
                displayMessage('bot', 'No response from the bot.'); // Handle empty response
            }
        })
        .catch(error => {
            console.error('Error fetching chat response:', error);
            displayMessage('bot', 'Oops, something went wrong. Please try again later.'); // Handle fetch error
        });
    }
});
