document.addEventListener('DOMContentLoaded', function() {
  const chatInput = document.querySelector('.chat-input');
  const chatSendButton = document.querySelector('.chat-send');
  const chatMessages = document.querySelector('.chat-messages');

  chatSendButton.addEventListener('click', sendMessage);
  chatInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
      sendMessage();
    }
  });

  function sendMessage() {
    const userInput = chatInput.value.trim();
    if (userInput) {
      displayMessage('user', userInput);
      chatInput.value = '';
      fetchChatResponse(userInput);
    }
  }

  function displayMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', `message--${sender}`);
    messageElement.textContent = message;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function fetchChatResponse(userInput) {
    fetch('/chat', {
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
});
