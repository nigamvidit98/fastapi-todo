const API_URL = "http://localhost:8000";

export const getTodos = async () => {
  const res = await fetch(`${API_URL}/todos`);
  return res.json();
};

export const addTodo = async (task) => {
  await fetch(`${API_URL}/todos?task=${task}`, {
    method: "POST",
  });
};

export const deleteTodo = async (id) => {
  await fetch(`${API_URL}/todos/${id}`, {
    method: "DELETE",
  });
};

export const updateTodo = async (id, task) => {
  await fetch(`${API_URL}/todos/${id}?task=${task}`, {
    method: "PUT",
  });
};