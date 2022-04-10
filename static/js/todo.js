const addTodoBtn = document.getElementById("addTodoBtn");

const titleInput = document.getElementById("title");
const textInput = document.getElementById("textArea");


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
