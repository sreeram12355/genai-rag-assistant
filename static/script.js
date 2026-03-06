let sessionId = localStorage.getItem("sessionId");

if (!sessionId) {
    sessionId = crypto.randomUUID();
    localStorage.setItem("sessionId", sessionId);
}

async function sendMessage() {

    const input = document.getElementById("user-input");
    const message = input.value;

    if (!message) return;

    addMessage("User", message);

    input.value = "";

    try {

        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                sessionId: sessionId,
                message: message
            })
        });

        const data = await response.json();

        addMessage("Assistant", data.reply);

    } catch (error) {

        addMessage("Assistant", "Error getting response from server.");

        console.error(error);
    }
}

function addMessage(sender, text) {

    const messageDiv = document.createElement("div");

    messageDiv.className = "message";

    messageDiv.innerHTML = `<b>${sender}:</b> ${text}`;

    document.getElementById("messages").appendChild(messageDiv);

    document.getElementById("messages").scrollTop =
        document.getElementById("messages").scrollHeight;
}