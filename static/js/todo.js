const addTodoBtn = document.getElementById("addTodoBtn");
const transcript = document.getElementById('p');

const titleInput = document.getElementById("title");
const textInput = document.getElementById("textArea");

console.log(transcript);

const checkSpeech = setInterval(() => {
  if (transcript.value)
  {
    if (transcript.value.includes("title"))
    {
      titleInput.value = transcript.value.replace("title", "");
    }
    else if (transcript.value.includes("text"))
    {
      textInput.value = transcript.value.replace("text", "");
    }
    else if (transcript.value.includes("add"))
    {
      addTodoBtn.click();
      transcript.value = null;
    }
  }

}, 100);


addTodoBtn.addEventListener("click", (e) => {
  e.preventDefault();

  title = titleInput.value;
  text = textInput.value;

  fetch("/todo/add", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    // secret_key: secret_key,
    body: JSON.stringify({
      title,
      text,
    }),
  });
});
