import React from "react";

function TodoItem({ todo, onDelete, onUpdate }) {
  return (
    <li className="list-group-item d-flex justify-content-between">
      <span>
        {todo.id}: {todo.task}
      </span>

      <div>
        <button
          className="btn btn-warning btn-sm me-2"
          onClick={() => {
            const newTask = prompt("Update task:");
            if (newTask) onUpdate(todo.id, newTask);
          }}
        >
          Update
        </button>

        <button
          className="btn btn-danger btn-sm"
          onClick={() => onDelete(todo.id)}
        >
          Delete
        </button>
      </div>
    </li>
  );
}

export default TodoItem;