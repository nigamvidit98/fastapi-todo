import React, { useState } from "react";

function AddTodo({ onAdd }) {
  const [task, setTask] = useState("");

  const handleSubmit = () => {
    if (!task.trim()) return;
    onAdd(task);
    setTask("");
  };

  return (
    <div className="mb-3">
      <input
        className="form-control"
        value={task}
        onChange={(e) => setTask(e.target.value)}
        placeholder="Enter task"
      />
      <button className="btn btn-primary mt-2" onClick={handleSubmit}>
        Add Task
      </button>
    </div>
  );
}

export default AddTodo;