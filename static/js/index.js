console.log("This is working");

const checkBtn = document.getElementById("checkBtn");
const speakBtn = document.getElementById("openMic");

speakBtn.addEventListener('click', () => {
    var speech = true;
    window.SpeechRecognition = window.SpeechRecognition
        || window.webkitSpeechRecognition;

    const recognition = new SpeechRecognition();
    recognition.interimResults = true;
    const words = document.querySelector('.words');
    words.appendChild(p);

    recognition.addEventListener('result', e => {
        const transcript = Array.from(e.results)
            .map(result => result[0])
            .map(result => result.transcript)
            .join('')

        document.getElementById("p").innerHTML = transcript;

        if (transcript === 'Click me.')
            checkBtn.click();
        // console.log(transcript);
    });

    if (speech == true) {
        recognition.start();
        recognition.addEventListener('end', recognition.start);
    }
})



checkBtn.addEventListener("click", () => {
    console.log("Button is clicked");
})

const CLIENT_ID = '278594338975-mv9fj5kpdq723si0sr81pb51acjpup3d.apps.googleusercontent.com';