const chatbox = document.querySelector('.chatbox');
const chatInput = document.querySelector('.chat-input textarea');
const sendButton = document.getElementById('sendBTN');

// Replace with your actual Gemini API key
const GEMINI_API_KEY = 'AIzaSyC_Z4P0a4iqwA9Win51W-BQICYCnHdnBqM';

// Function to add a message to the chat
function addMessage(message, isOutgoing = false) {
    const li = document.createElement('li');
    li.classList.add(isOutgoing ? 'outgoing' : 'incoming');
    li.textContent = message;
    chatbox.appendChild(li);
    chatbox.scrollTop = chatbox.scrollHeight;
}

// Function to handle sending messages
async function handleSendMessage() {
    const message = chatInput.value.trim();
    if (!message) return;

    // Add user message to chat
    addMessage(message, true);
    chatInput.value = '';

    try {
        // Update the URL to match your Flask server
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  // Add this for local development
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();
        addMessage(data.response);
    } catch (error) {
        console.error('Error:', error);
        addMessage('Sorry, I encountered an error. Please try again.');
    }
}

// Event listeners
sendButton.addEventListener('click', handleSendMessage);

chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleSendMessage();
    }
});

// Function to handle the close button
function cancel() {
    chatbox.innerHTML = '';
    chatInput.value = '';
}
