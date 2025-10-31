const searchButton = document.getElementsByClassName("search-btn")[0]


const taskList = document.getElementById("tasks")
searchButton.addEventListener("click", () => {
    const input = document.getElementsByClassName("search-in")[0];
    const searchQuery = input.value.toLowerCase();
    const tasks = taskList.getElementsByClassName("task");

    for (let task of tasks) {
        const taskTextElement = task.querySelector(".task-text");
        if (!taskTextElement) continue; // skip if task is being edited

        const taskText = taskTextElement.innerText.toLowerCase();
        if (!taskText.includes(searchQuery)) {
            task.style.display = "none";
        } else {
            task.style.display = "flex";
        }
    }
});

taskList.addEventListener("click", (e) => {
    const task = e.target.closest(".task");
    if (!task) return;

    if (e.target.classList.contains("edit-task")) {
        let editing = task.classList.contains("editing");
        const currentTextElement = task.querySelector(".task-text");

        if (!editing) {
            // Start editing
            const input = document.createElement("input");
            input.type = "text";
            input.value = currentTextElement.innerText;
            input.className = "edit-input";
            task.replaceChild(input, currentTextElement);
            input.focus();
            e.target.textContent = "Save";
            task.classList.add("editing");

            input.addEventListener("keydown", (event) => {
                if (event.key === "Enter") saveEdit();
                else if (event.key === "Escape") cancelEdit();
            });

            const cancelEdit = () => {
                task.replaceChild(currentTextElement, input);
                e.target.textContent = "Edit";
                task.classList.remove("editing");
            };

            const saveEdit = () => {
                if (input.value.trim() !== "") {
                    const newSpan = document.createElement("span");
                    newSpan.className = "task-text";
                    newSpan.innerText = input.value.trim();
                    task.replaceChild(newSpan, input);
                    e.target.textContent = "Edit";
                    task.classList.remove("editing");
                } else {
                    alert("Task text cannot be empty.");
                }
            };
        } else {
            // Already editing → save
            const input = task.querySelector("input.edit-input");
            if (input.value.trim() !== "") {
                const newSpan = document.createElement("span");
                newSpan.className = "task-text";
                newSpan.innerText = input.value.trim();
                task.replaceChild(newSpan, input);
                e.target.textContent = "Edit";
                task.classList.remove("editing");
            } else {
                alert("Task text cannot be empty.");
            }
        }

    } else if (e.target.classList.contains("delete-task")) {
        if (confirm("Are you sure you want to delete this task?")) {
            task.remove();
        }
    }
});

const addButton = document.getElementById("add-task-button")
addButton.addEventListener("click", () => {
    const input = document.getElementById("new-task-input")
    const taskText = input.value
    if (taskText.trim() === "") {
        alert("Task text cannot be empty.")
        return
    }
    const newTask = document.createElement("li")
    newTask.className = "task"
    newTask.innerHTML = `
        <span class="task-text">${taskText}</span>
        <button class="edit-task">Edit</button>
        <button class="delete-task">Delete</button>
    `
    taskList.appendChild(newTask)
    input.value = ""
})


