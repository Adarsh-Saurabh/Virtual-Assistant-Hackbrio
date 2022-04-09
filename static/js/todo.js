console.log("This is todo list");

const addTodoBtn = document.getElementById("addTodoBtn");

addTodoBtn.addEventListener("click", (e) => {
  e.preventDefault();

  const title = document.getElementById("title").value;
  const text = document.getElementById("textArea").value;

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
