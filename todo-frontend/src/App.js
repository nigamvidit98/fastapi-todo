import React, { useEffect, useState } from "react";
import AddTodo from "./components/AddTodo";
import TodoList from "./components/TodoList";
import {
  getTodos,
  addTodo,
  deleteTodo,
  updateTodo,
} from "./Services/api";

import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [todos, setTodos] = useState([]);

  const fetchData = async () => {
    const data = await getTodos();
    setTodos(data);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleAdd = async (task) => {
    await addTodo(task);
    fetchData();
  };

  const handleDelete = async (id) => {
    await deleteTodo(id);
    fetchData();
  };

  const handleUpdate = async (id, task) => {
    await updateTodo(id, task);
    fetchData();
  };

  return (
    <div className="container mt-5">
      <h2 className="text-center">Todo App</h2>

      <AddTodo onAdd={handleAdd} />

      <TodoList
        todos={todos}
        onDelete={handleDelete}
        onUpdate={handleUpdate}
      />
    </div>
  );
}

export default App;
