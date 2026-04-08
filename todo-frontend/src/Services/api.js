const API_URL = "/api";

export const getTodos = async () => {
  try {
    const res = await fetch(`${API_URL}/todos`);

    if (!res.ok) {
      console.error("Failed to fetch todos");
      return [];
    }

    const data = await res.json();
    return Array.isArray(data) ? data : [];
  } catch (err) {
    console.error("Error fetching todos:", err);
    return [];
  }
};

export const addTodo = async (task) => {
  const res = await fetch(`${API_URL}/todos`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ task }),
  });
  return res.json();
};

export const deleteTodo = async (id) => {
  await fetch(`${API_URL}/todos/${id}`, {
    method: "DELETE",
  });
};

export const updateTodo = async (id, task) => {
  const res = await fetch(`${API_URL}/todos/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ task }),
  });
  return res.json();
};