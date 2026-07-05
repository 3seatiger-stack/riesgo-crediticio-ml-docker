const form = document.getElementById("risk-form");
const result = document.getElementById("result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  result.classList.remove("hidden", "error");
  result.innerHTML = "<p>Evaluando solicitud...</p>";

  const values = Object.fromEntries(new FormData(form).entries());
  const integerFields = new Set(["historial_moras", "consultas_buro"]);
  const payload = {};

  for (const [key, value] of Object.entries(values)) {
    payload[key] = integerFields.has(key) ? Number.parseInt(value, 10) : Number(value);
  }

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(JSON.stringify(data.detail ?? data));
    }

    const percent = (data.probabilidad_incumplimiento * 100).toFixed(1);
    result.innerHTML = `
      <h2>Resultado de evaluación</h2>
      <p class="metric">${percent}%</p>
      <p><strong>${data.clasificacion}</strong></p>
      <p>Umbral de decisión: ${(data.umbral_decision * 100).toFixed(0)}%</p>
      <p>${data.recomendacion}</p>
      <small>Modelo: ${data.modelo}</small>
    `;
  } catch (error) {
    result.classList.add("error");
    result.innerHTML = `
      <h2>No fue posible evaluar</h2>
      <p>Revise los valores ingresados y vuelva a intentar.</p>
      <small>${error.message}</small>
    `;
  }
});
