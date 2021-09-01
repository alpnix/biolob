var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList;

var grammar = '#JSGF V1.0;'

var recognition = new SpeechRecognition();
var speechRecognitionList = new SpeechGrammarList();
speechRecognitionList.addFromString(grammar, 1);
recognition.grammars = speechRecognitionList;
recognition.lang = 'en-US';
recognition.interimResults = false;

recognition.onresult = function(event) {
    var last = event.results.length - 1;
    var command = event.results[last][0].transcript;
    $.ajax({
        type:"POST",
        data:{
          content: command,
          csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        success: function(data) {
  
          $(".chat-messages").append(data);
          var chatMessages = document.querySelector(".chat-messages");
          chatMessages.scrollTop = chatMessages.scrollHeight;
        }
      })
};

recognition.onspeechend = function() {
    recognition.stop();
};

recognition.onerror = function(event) {
    console.log('Error occurred in recognition: ' + event.error);
    var error = "Sorry, I could not understand your voice! Can you speak in a more audible way into your microfone?";
    var error_message = `<div class="message">
        <p class="meta">BioBot <span></span></p>
        <p class="text text-danger">
        ${error}
        </p>
      </div>`
    $(".chat-messages").append(error_message);
    var chatMessages = document.querySelector(".chat-messages");
    chatMessages.scrollTop = chatMessages.scrollHeight;
}        

document.querySelector('#voice').addEventListener('click', function(){
    recognition.start();
});

