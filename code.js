const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');
const messages = document.getElementById('messages');
const url = "https://27f7-2600-1003-b039-7f53-acf4-491-d49f-91a1.ngrok-free.app/texts";
const pattern = "\('(.*)', \"(.*)\"\)";


/*
messageInput.addEventListener('keydown', function(e) {
  if (e.key === 'Enter' && messageInput.value.trim() !== '') {
    const message = document.createElement('li');
    message.classList.add('message-sent');
    message.textContent = messageInput.value;
    messages.appendChild(message);
    messageInput.value = '';
    loadReply();
  }
});
function loadReply() {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          const reply = xhr.responseText;
          const messages = document.getElementById("messages");
          const li = document.createElement("li");
          li.className = "reply";
          li.innerHTML = reply;
          messages.appendChild(li);
        } else {
          console.error(xhr.statusText);
        }
      }
    };
    xhr.open("GET", "reply.txt");
    xhr.send();
}
*/


function displayMessages() {
  fetch(url)
    .then(response => response.text())
    .then(data => {
        console.log(data)
      data = "(\'Hi\', \'Hi there! How can I help you?\')";
      const result = data.match(pattern);
      const send_msg = result[1];
      const reply_msg = result[2];
      let info = [result[1],result[2]]
    
      //return [send_msg, reply_msg]; // return messages in an array
      const messages = document.getElementById('messages');
      for (let i = 0; i < info.length; i++) {
        const message = document.createElement('li');
        message.textContent = info[i];
        if (i % 2 === 0) {
          message.classList.add('message-sent');
          messages.appendChild(message);
        } else {
          message.classList.add('reply');
          setTimeout(function() {
              messages.appendChild(message);
            }, 1000);
        }
      }
    })
    .catch(error => console.error(error));
} 
/*
function displayMessages() {
    const request = new XMLHttpRequest();
    request.open('GET', url);
    request.onload = function() {
      if (request.status === 200) {
        const data = request.responseText;
        console.log(data);
        data = "(\'Hi\', \'Hi there! How can I help you?\')";
        const result = data.match(pattern);
        const send_msg = result[1];
        const reply_msg = result[2];
        let info = [result[1],result[2]];
        const messages = document.getElementById('messages');
        for (let i = 0; i < info.length; i++) {
          const message = document.createElement('li');
          message.textContent = info[i];
          if (i % 2 === 0) {
            message.classList.add('message-sent');
            messages.appendChild(message);
          } else {
            message.classList.add('reply');
            setTimeout(function() {
                messages.appendChild(message);
              }, 1000);
          }
        }
      } else {
        console.error('Error');
      }
    }
    request.onerror = function() {
      console.error('Error');
    }
    request.send();
  }
  */

window.onload = function() {
    displayMessages();
};

// for testing, not really calling url
/*
function getInfo() {
        data = "(\'Hi\', \'Hi there! How can I help you?\')";
        const result = data.match(pattern);
        const send_msg = result[1];
        const reply_msg = result[2];
        //console.log([send_msg, reply_msg]);
        return [send_msg, reply_msg]; // return messages in an array
}
function displayMessage() {
    const messages = document.getElementById('messages');
    let info = getInfo();
    console.log(info)
    // Loop through each message in the info array
    for (let i = 0; i < info.length; i++) {
      const message = document.createElement('li');
      message.textContent = info[i];
      if (i % 2 === 0) {
        message.classList.add('message-sent');
        messages.appendChild(message);
      } else {
        message.classList.add('reply');
        setTimeout(function() {
            messages.appendChild(message);
          }, 1000);
      }
    }
  }
*/