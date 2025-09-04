# app.py - Simple Weather Forecast (Gradio Demo)
# This app simulates a weather forecast for a given city and day.
# No API key or external services required — outputs are generated locally.

import gradio as gr
import random
import datetime

# Predefined example weather conditions
CONDITIONS = ["Sunny ☀️", "Partly Cloudy ⛅", "Cloudy ☁️", "Rainy 🌧️", "Stormy ⛈️", "Snowy ❄️", "Windy 🌬️"]

def fake_forecast(city: str, days: int):
    """
    Generate a fake forecast for a given city and number of days.
    Args:
        city: name of the city
        days: number of days (1–7)
    Returns:
        Markdown text with forecast info
    """
    if not city.strip():
        return "❌ Please enter a valid city name."
    if days < 1 or days > 7:
        return "❌ Please choose between 1 and 7 days."

    today = datetime.date.today()
    lines = [f"### 📍 Weather Forecast for **{city.title()}**", ""]
    for i in range(days):
        date = today + datetime.timedelta(days=i)
        condition = random.choice(CONDITIONS)
        temp_high = random.randint(15, 35)  # Celsius
        temp_low = temp_high - random.randint(3, 10)
        lines.append(f"**{date.strftime('%A %d %B %Y')}**: {condition}, {temp_low}°C – {temp_high}°C")

    return "\n".join(lines)

# Build Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🌦️ Simple Weather Forecast App\nEnter a city and choose number of days (1–7).")
    with gr.Row():
        city_input = gr.Textbox(label="City", placeholder="e.g., London")
        days_input = gr.Slider(1, 7, value=3, step=1, label="Days")
    forecast_btn = gr.Button("Get Forecast")
    output_md = gr.Markdown("")

    forecast_btn.click(fn=fake_forecast, inputs=[city_input, days_input], outputs=output_md)

# For Hugging Face Spaces, no need for share=True
if __name__ == "__main__":
    demo.launch(share=True)  # keep share=True if running in Colab
